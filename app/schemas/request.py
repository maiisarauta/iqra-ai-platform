from pydantic import BaseModel, Field


class TextAnalysisRequest(BaseModel):
    surah: int = Field(..., ge=1, le=114)
    ayah: int = Field(..., ge=1)
    text: str


class AudioAnalysisRequest(BaseModel):
    surah: int = Field(..., ge=1, le=114)
    ayah: int = Field(..., ge=1)
