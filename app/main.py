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

    pattern = r"([A-Za-z ]+)\s+(\d{1,3})"

    for match in re.finditer(pattern, text):
        subject = match.group(1).strip()
        marks = int(match.group(2))

        if 0 <= marks <= 100:
            subjects.append({
                "subject": subject,
                "marks": marks
            })
            total += marks

    result = "PASS" if total > 0 else "FAIL"

    return {
        "subjects": subjects,
        "total_marks": total,
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