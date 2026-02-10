from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/api", tags=["Marksheet Extractor"])

def extract_marksheet_logic(image):
    # OCR + LLM logic here
    return {
        "name": "Student Name",
        "roll_no": "12345",
        "marks": {
            "Maths": 85,
            "Science": 90
        }
    }

@router.post("/extract/")
async def extract_marksheet(file: UploadFile = File(...)):
    return extract_marksheet_logic(file)