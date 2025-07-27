from flask import render_template, request, send_from_directory, abort
import os
import shutil
from app.utils import perform_analysis
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename

    if not (filename.endswith('.csv') or filename.endswith('.xlsx')):
        return "نوع الملف غير مدعوم. يرجى رفع ملف CSV أو Excel."

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    questions = request.form['questions']
    hypotheses = request.form['hypotheses']

    # إجراء التحليل
    perform_analysis(file_path, questions, hypotheses)

    # جمع الرسوم البيانية من output/charts
    charts_folder = os.path.join(app.config['OUTPUT_FOLDER'], 'charts')
    images = []
    if os.path.exists(charts_folder):
        images = [f for f in os.listdir(charts_folder) if f.endswith('.png')]

        # نسخها إلى app/static/charts
        static_charts = os.path.join('app', 'static', 'charts')
        os.makedirs(static_charts, exist_ok=True)
        for img in images:
            src = os.path.join(charts_folder, img)
            dst = os.path.join(static_charts, img)
            try:
                shutil.copy(src, dst)
            except Exception as e:
                print(f"خطأ في نسخ الصورة {img}: {e}")

    return render_template('results.html', images=images)

@app.route('/download/<filename>')
def download_file(filename):
    output_path = app.config['OUTPUT_FOLDER']
    full_path = os.path.join(output_path, filename)
    if os.path.exists(full_path):
        return send_from_directory(output_path, filename, as_attachment=True)
    else:
        return f"الملف {filename} غير موجود في {output_path}", 404
