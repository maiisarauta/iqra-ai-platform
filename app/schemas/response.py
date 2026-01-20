from pydantic import BaseModel
from typing import List


class Mistake(BaseModel):
    word: str
    expected: str
    type: str
    position: int


class Correction(BaseModel):
    word: str
    corrected: str


class AnalyzeResponse(BaseModel):
    engine: str
    confidence_score: float
    mistakes: List[Mistake]
    corrections: List[Correction]
