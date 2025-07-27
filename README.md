
# 📊 محلل الإحصاءات الذكي - Smart Statistical Analyst

هذا المشروع هو تطبيق ويب مبني باستخدام Python وFlask لتحليل بيانات الاستبيانات الأكاديمية (بصيغة CSV أو Excel) وتوليد مخرجات احترافية تشمل:

- تقرير Word تلقائي يحتوي على الإحصاءات والأسئلة والفرضيات.
- ملخص إحصائي في ملف Excel.
- ملف بيانات SPSS جاهز للتحليل الإحصائي المتقدم.
- رسوم بيانية تلقائية تعرض التوزيعات.

---

## 🎯 الهدف من المشروع

يهدف المشروع إلى تمكين الباحثين وطلاب الدراسات العليا من تحليل بيانات الاستبيانات بسهولة، دون الحاجة إلى كتابة كود، مع الحصول على مخرجات احترافية قابلة للاستخدام مباشرة في التقارير العلمية.

---

## 🧰 المجلدات والهيكلية

```
smart_stat_analyst/
│
├── app/                      ← ملفات التطبيق الأساسية
│   ├── templates/            ← ملفات HTML
│   ├── static/               ← ملفات CSS والرسوم
│   ├── routes.py             ← المسارات والتحكم في الطلبات
│   ├── utils.py              ← دوال التحليل والتوليد
│   └── __init__.py           ← تهيئة تطبيق Flask
│
├── output/                   ← مخرجات التحليل (تُنشأ تلقائيًا)
│
├── run.py                    ← نقطة تشغيل التطبيق
├── requirements.txt          ← المكتبات المطلوبة
└── README.md                 ← هذا الملف
```

---

## ⚙️ متطلبات التشغيل

لضمان تشغيل المشروع بشكل سليم، يُرجى تثبيت المتطلبات التالية:

```bash
pip install -r requirements.txt
```

> تأكد من أنك تستخدم Python 3.8 أو أحدث.

---

## 🚀 طريقة الاستخدام

1. شغّل التطبيق:
   ```bash
   python run.py
   ```

2. افتح المتصفح وتوجه إلى:
   ```
   http://127.0.0.1:5000/
   ```

3. ارفع ملف الاستبيان (CSV أو Excel).

4. أدخل أسئلة البحث والفرضيات.

5. اضغط "ابدأ التحليل".

6. بعد انتهاء المعالجة، سيتم عرض:
   - روابط تحميل الملفات.
   - الرسوم البيانية مباشرة على الصفحة.

---

## 📌 ملاحظات

- تأكد أن أسماء الأعمدة في ملف البيانات لا تحتوي على رموز غريبة أو فراغات طويلة.
- يتم تلقائيًا تعديل أسماء الأعمدة لتكون متوافقة مع تنسيق SPSS.

---

## 📄 الترخيص

هذا المشروع تعليمي ومفتوح المصدر، ويمكن تعديله بحرية للأغراض الأكاديمية.


📊 Smart Statistical Analyst
This project is a web application built using Python and Flask to analyze academic survey data (in CSV or Excel format) and generate professional outputs, including:

* An automated Word report containing statistics, questions, and hypotheses.
* A statistical summary in an Excel file.
* An SPSS data file ready for advanced statistical analysis.
* Automatically generated charts displaying distributions.

🎯 Project Goal
The project aims to enable researchers and graduate students to easily analyze survey data without the need to write code, providing professional outputs that are ready to be used directly in scientific reports.

🧰 Folders and Structure
smart\_stat\_analyst/
│
├── app/                      ← Core application files
│   ├── templates/            ← HTML files
│   ├── static/               ← CSS and graphics files
│   ├── routes.py             ← Routes and request handling
│   ├── utils.py              ← Analysis and generation functions
│   └── **init**.py           ← Flask application initialization
│
├── output/                   ← Generated analysis outputs
│
├── run.py                    ← Application entry point
├── requirements.txt          ← Required libraries
└── README.md                 ← This file

⚙️ System Requirements
To ensure the project runs correctly, please install the following dependencies:

```
pip install -r requirements.txt
```

Make sure you're using Python 3.8 or newer.

🚀 How to Use
Run the application:

```
python run.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

Upload the survey file (CSV or Excel).
Enter the research questions and hypotheses.
Click "Start Analysis."

After processing, the following will be displayed:

* Links to download the files.
* Charts directly on the page.

📌 Notes
Make sure the column names in the data file don't contain strange characters or long spaces.
Column names will be automatically adjusted to match the SPSS format.

📄 License
This project is educational and open-source, and can be freely modified for academic purposes.

