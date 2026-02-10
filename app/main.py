from fastapi import FastAPI, UploadFile, File, HTTPException
import pytesseract
from PIL import Image
import re
import io

app = FastAPI(title="Marksheet OCR API")


# ---------------- OCR FUNCTION ----------------
def extract_text_from_image(file: UploadFile) -> str:
    image = Image.open(io.BytesIO(file.file.read()))
    text = pytesseract.image_to_string(image)
    return text


# ---------------- FORMAT FUNCTION ----------------
def format_marksheet(text: str):
    subjects = []
    total = 0
    max_total = 0

    # -------- Student Details --------
    name_match = re.search(r"Name\s*[:\-]?\s*([A-Za-z ]+)", text)
    roll_match = re.search(
        r"(Roll No|Roll Number|Hall Ticket No|Reg No)\s*[:\-]?\s*(\w+)", text
    )

    student_name = name_match.group(1).strip() if name_match else "Not Found"
    roll_number = roll_match.group(2).strip() if roll_match else "Not Found"

    # -------- Subject & Marks --------
    subject_pattern = r"([A-Za-z ]+)\s+(\d{1,3})\s*/?\s*(\d{1,3})?"

    for match in re.finditer(subject_pattern, text):
        subject = match.group(1).strip()
        marks = int(match.group(2))
        max_marks = int(match.group(3)) if match.group(3) else 100

        if 0 <= marks <= max_marks:
            subjects.append({
                "subject": subject,
                "marks_obtained": marks,
                "max_marks": max_marks,
                "status": "PASS" if marks >= 35 else "FAIL"
            })
            total += marks
            max_total += max_marks

    # -------- Final Result --------
    percentage = round((total / max_total) * 100, 2) if max_total > 0 else 0
    result = "PASS" if all(sub["status"] == "PASS" for sub in subjects) else "FAIL"

    return {
        "student_name": student_name,
        "roll_number": roll_number,
        "subjects": subjects,
        "total_marks": total,
        "maximum_marks": max_total,
        "percentage": percentage,
        "result": result
    }


# ---------------- API ENDPOINT ----------------
@app.post("/extract-text")
async def extract_text(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        raise HTTPException(
            status_code=400,
            detail="Only image files (.png, .jpg, .jpeg) are allowed"
        )

    raw_text = extract_text_from_image(file)
    formatted_data = format_marksheet(raw_text)

    return {
        "status": "success",
        "data": formatted_data
    }


# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {"message": "Marksheet Extractor API is running"}
