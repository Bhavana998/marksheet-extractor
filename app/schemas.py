from pydantic import BaseModel
from typing import List, Optional

class Field(BaseModel):
    value: Optional[str]
    confidence: float

class CandidateDetails(BaseModel):
    name: Field
    father_or_mother_name: Field
    roll_no: Field
    registration_no: Field
    dob: Field
    exam_year: Field
    board_or_university: Field
    institution: Field

class Subject(BaseModel):
    subject: Field
    max_marks_or_credits: Field
    obtained_marks_or_credits: Field
    grade: Field

class OverallResult(BaseModel):
    result_or_division: Field

class IssueDetails(BaseModel):
    issue_date: Field
    issue_place: Field

class MarksheetResponse(BaseModel):
    candidate_details: CandidateDetails
    subjects: List[Subject]
    overall_result: OverallResult
    issue_details: IssueDetails
