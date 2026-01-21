from pydantic import BaseModel, Field


class AnalyzeTextRequest(BaseModel):
    ayah_reference: str = Field(
        ...,
        description="Surah:Ayah reference",
        json_schema_extra={
            "example": "1:1"
        }
    )

    text: str = Field(
        ...,
        description="Student written Quran text"
    )


class AnalyzeAudioRequest(BaseModel):
    ayah_reference: str = Field(
        ...,
        description="Surah:Ayah reference",
        json_schema_extra={
            "example": "1:1"
        }
    )

    audio_duration_seconds: int = Field(
        ...,
        ge=10,
        le=1800,
        description="Audio length between 10s and 30min"
    )
