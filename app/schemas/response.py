from pydantic import BaseModel, Field
from typing import List


class AnalysisResponse(BaseModel):
    surah: int
    ayah: int
    confidence: float = Field(ge=0.0, le=1.0)
    mistakes: List[str]
    corrections: List[str]
