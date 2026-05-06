📄 AI-Powered Marksheet Extractor (OCR + Intelligent Parsing)

An end-to-end Document Intelligence System that automatically extracts structured academic data (Name, Subjects, Marks, CGPA) from marksheets using OCR and intelligent parsing.

---

🚀 Overview

This project transforms unstructured marksheet documents into structured, machine-readable data. It reduces manual effort in academic verification workflows and enables automation in applications like student onboarding, result processing, and analytics.

---

❗ Problem Statement

Manual entry of marksheet data is:

- ⏳ Time-consuming
- ❌ Error-prone
- 📉 Inefficient at scale

Organizations handling large volumes of student data require an automated, accurate, and scalable solution.

## frontend deploy link:https://marksheet-extractor-1-x81n.onrender.com

## backend deploy link: https://marksheet-extractor-ludc.onrender.com/docs
---

💡 Solution

This system automates the entire pipeline:

- 📤 Upload marksheet (image/PDF)
- 🔍 Extract text using OCR
- 🧠 Identify and parse key academic fields
- 📊 Convert into structured output (JSON/CSV)

---

🧠 System Architecture

Input Image/PDF
        ↓
Image Preprocessing (Noise Removal, Enhancement)
        ↓
OCR Engine (Tesseract / EasyOCR)
        ↓
Text Cleaning & Parsing
        ↓
Field Extraction (Name, Subjects, Marks, CGPA)
        ↓
Structured Output (JSON / CSV)

## ⚙️ How It Works

1. Image Upload
2. Image Preprocessing (OpenCV)
3. OCR Extraction (Tesseract)
4. Text Parsing
5. Structured JSON Output

---

⚙️ Tech Stack

- Programming: Python
- OCR: Tesseract OCR / EasyOCR
- Image Processing: OpenCV
- Data Processing: Pandas, NumPy
- Interface (Optional): Streamlit

---

✨ Key Features

- 📄 Supports scanned marksheets (images/PDFs)
- 🔍 Automated text extraction
- 🧠 Intelligent parsing of academic fields
- 📊 Structured data output (JSON/CSV)
- ⚡ Fast and efficient processing pipeline
- 🔄 Adaptable to different marksheet formats

---

🖥️ Demo

📥 Input Marksheet

(Add screenshot here)

📤 Extracted Output

(Add screenshot here)

📊 Structured Data

{
  "name": "Student Name",
  "subjects": {
    "Math": 95,
    "Physics": 90
  },
  "cgpa": 9.2
}

---

📊 Results

- ✅ Successfully extracts:
  
  - Student Name
  - Subject-wise marks
  - CGPA

- 📈 Works across multiple basic marksheet formats

- ⚡ Reduces manual data entry effort significantly

(Add accuracy metrics if available)

---

📌 Key Highlights

- Built an end-to-end OCR + parsing pipeline
- Converted unstructured academic documents into structured data
- Designed for real-world academic automation use cases
- Demonstrates document intelligence system design

---

⚡ How to Run

git clone https://github.com/Bhavana998/marksheet-extractor
cd marksheet-extractor
pip install -r requirements.txt
python app.py

---

🚀 Future Improvements

- 🌐 Multi-language OCR support
- 🧠 Deep learning-based OCR (PaddleOCR)
- 📊 Table detection for complex marksheets
- 🤖 LLM-based intelligent data extraction
- ☁️ API deployment using FastAPI
- 🖥️ Interactive web interface

---

🎯 Use Cases

- 🎓 Student admission systems
- 🏫 Academic record management
- 📊 Educational analytics
- 🧾 Automated verification systems

---
## 📄 Output Format

The API returns a structured JSON response:

```json
{
  "status": "string",
  "data": {
    "student_name": "string",
    "roll_number": "string",
    "subjects": [
      {
        "subject": "string",
        "marks_obtained": "integer",
        "max_marks": "integer",
        "status": "PASS | FAIL"
      }
    ],
    "total_marks": "integer",
    "maximum_marks": "integer",
    "percentage": "float",
    "result": "PASS | FAIL"
  }
}
```
---

📊 Field Details

- status
  Indicates request status
  
  - ""success"" → extraction successful
  - ""error"" → extraction failed

- student_name
  Full name of the student extracted from marksheet

- roll_number
  Unique identification number of the student

- subjects
  List of subjects with marks and status

- subject
  Name of the subject

- marks_obtained
  Marks scored in the subject

- max_marks
  Maximum marks for the subject (default: 100)

- status (per subject)
  
  - ""PASS"" if marks ≥ 33
  - ""FAIL"" if marks < 33

- total_marks
  Sum of marks obtained in all subjects

- maximum_marks
  Total possible marks (subjects × max_marks)

- percentage
  Calculated percentage of total marks

- result
  Final result
  
  - ""PASS"" → all subjects passed
  - ""FAIL"" → any subject failed

---

👩‍💻 Author
Bhavana 

---

⭐ If you found this useful

Give it a ⭐ on GitHub and support the project!
