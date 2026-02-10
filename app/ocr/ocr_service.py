from fastapi import FastAPI, UploadFile, File
import pytesseract
from PIL import Image
import io

app = FastAPI()

# Explicit Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file: UploadFile):
    try:
        image = Image.open(io.BytesIO(file.file.read()))
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        raise RuntimeError(f"OCR failed: {str(e)}")


@app.post("/ocr")
async def ocr_image(file: UploadFile = File(...)):
    text = extract_text(file)
    return {"extracted_text": text}
