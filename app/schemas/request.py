from pydantic import BaseModel, Field


class AnalyzeTextRequest(BaseModel):
    ayah_reference: str = Field(
        ..., description="Surah:Ayah reference, e.g. 1:1"
    )
    text: str = Field(
        ..., description="Student-written Qur'an text (Arabic)"
    )


class AnalyzeAudioRequest(BaseModel):
    ayah_reference: str = Field(
        ..., description="Surah:Ayah reference, e.g. 1:1"
    )
