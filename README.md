📄 AI Marksheet Extractor using OCR

An intelligent document processing system that automatically extracts structured information (Name, Subjects, Marks, CGPA) from academic marksheets using Optical Character Recognition (OCR) and data parsing techniques.

## frontend deploy link:https://marksheet-extractor-1-x81n.onrender.com
## backend deploy link: https://marksheet-extractor-ludc.onrender.com/docs

🚀 Problem Statement

Educational institutions and organizations often require students to manually enter marks from their marksheets into online forms. This process is:

- Time-consuming
- Error-prone
- Inefficient for large-scale applications

Manual entry can lead to incorrect data submission and delays in processing.

---

💡 Solution

This project automates marksheet data extraction by:

- Uploading marksheet images or PDFs
- Extracting text using OCR
- Parsing and structuring relevant fields (Name, Roll No, Marks, etc.)
- Converting unstructured data into usable structured format (JSON/CSV)

Such systems are widely used in real-world applications to reduce manual effort and improve accuracy in document verification workflows

---

⚙️ Tech Stack

- Python
- OpenCV
- Tesseract OCR / EasyOCR
- NumPy / Pandas
- Streamlit (for UI - if added)

---

🧠 System Architecture

1. Input: Marksheet image / PDF
2. Preprocessing:
   - Noise removal
   - Image enhancement
3. OCR Processing:
   - Extract raw text from document
4. Data Parsing:
   - Identify key fields (Name, Subjects, Marks)
5. Output:
   - Structured JSON / CSV

---

📊 Features

- 📄 Supports scanned marksheets (images/PDFs)
- 🔍 Automatic text extraction using OCR
- 📊 Structured output generation
- ⚡ Fast and automated processing
- 🧠 Intelligent parsing of academic data

---

🖥️ Demo

(Add screenshots here)

- Input marksheet
- Extracted text
- Structured output

---

📊 Results

- Successfully extracts:
  - Student Name
  - Subjects
  - Marks
- Works on multiple marksheet formats (basic support)

(Add accuracy % if available)

---

⚡ How to Run

git clone https://github.com/Bhavana998/marksheet-extractor
cd marksheet-extractor
pip install -r requirements.txt
python app.py

---

🚀 Future Improvements

- 📌 Multi-language support
- 📌 Deep learning-based OCR (PaddleOCR)
- 📌 Table detection for complex marksheets
- 📌 Integration with web applications
- 📌 Real-time API deployment

---

📌 Key Highlights

- Built an end-to-end OCR pipeline
- Automated document data extraction
- Reduced manual effort in marksheet processing
- Designed for real-world academic workflows

---

👩‍💻 Author
Bhavana
