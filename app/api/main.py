from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.file_handler import validate_file
from app.ocr.ocr_service import extract_text
from app.llm.parser import parse_marksheet
from app.schemas import MarksheetResponse

# ✅ DEFINE router FIRST
router = APIRouter(
    prefix="/extract",
    tags=["Marksheet Extraction"]
)

@router.post("/", response_model=MarksheetResponse)
async def extract_marksheet(file: UploadFile = File(...)):
    try:
        validate_file(file)
        ocr_text = extract_text(file)
        result = parse_marksheet(ocr_text)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
