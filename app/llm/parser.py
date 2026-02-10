import json
from app.llm.llm_service import call_llm

SYSTEM_PROMPT = """
You are an AI that extracts structured marksheet data.

Return JSON strictly in this format:
{
  "candidate_details": {
    "name": {"value": "", "confidence": 0},
    "father_or_mother_name": {"value": "", "confidence": 0},
    "roll_no": {"value": "", "confidence": 0},
    "registration_no": {"value": "", "confidence": 0},
    "dob": {"value": "", "confidence": 0},
    "exam_year": {"value": "", "confidence": 0},
    "board_or_university": {"value": "", "confidence": 0},
    "institution": {"value": "", "confidence": 0}
  },
  "subjects": [],
  "overall_result": {
    "result": {"value": "", "confidence": 0}
  }
}
"""

def parse_marksheet(text: str):
    response = call_llm(SYSTEM_PROMPT, text)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        raise RuntimeError("LLM did not return valid JSON")
