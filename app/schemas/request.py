from pydantic import BaseModel, Field
from typing import Optional


class AnalyzeTextRequest(BaseModel):
    ayah_reference: str = Field(
        ..., example="1:1", description="Surah:Ayah reference"
    )
    text: str = Field(
        ..., description="Student written Quran text"
    )


class AnalyzeAudioRequest(BaseModel):
    ayah_reference: str = Field(
        ..., example="1:1", description="Surah:Ayah reference"
    )
    audio_duration_seconds: int = Field(
        ..., ge=10, le=1800, description="Audio length between 10s and 30min"
    )
