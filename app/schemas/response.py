from pydantic import BaseModel
from typing import List


class AnalysisResponse(BaseModel):
    engine: str
    mistakes: List[str]
    corrections: List[str]
    confidence_score: float
