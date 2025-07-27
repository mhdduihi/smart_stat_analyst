from flask import Flask
import os

app = Flask(__name__)

# تحديد المسارات المطلقة للمجلدات
app.config['UPLOAD_FOLDER'] = os.path.abspath('Uploads')
app.config['OUTPUT_FOLDER'] = os.path.abspath('output')

# التأكد من إنشاء المجلدات إذا لم تكن موجودة
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(os.path.join(app.config['OUTPUT_FOLDER'], 'charts'), exist_ok=True)

from app import routes
