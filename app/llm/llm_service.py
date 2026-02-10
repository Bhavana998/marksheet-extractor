def call_llm(system_prompt: str, user_text: str):
    return """
{
  "candidate_details": {
    "name": {"value": "Sample Name", "confidence": 0.85},
    "father_or_mother_name": {"value": "Sample Parent", "confidence": 0.80},
    "roll_no": {"value": "12345", "confidence": 0.90},
    "registration_no": {"value": "REG123", "confidence": 0.88},
    "dob": {"value": "01-01-2000", "confidence": 0.75},
    "exam_year": {"value": "2020", "confidence": 0.95},
    "board_or_university": {"value": "State Board", "confidence": 0.85},
    "institution": {"value": "ABC College", "confidence": 0.80}
  },
  "subjects": [],
  "overall_result": {
    "result": {"value": "PASS", "confidence": 0.95}
  }
}
"""
