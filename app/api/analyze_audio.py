from fastapi import APIRouter, Form, UploadFile, File
from app.core.security import enforce_submission_limit
from app.core.controller import analyze_audio
from app.schemas.request import AnalyzeAudioRequest
from app.schemas.response import AnalyzeResponse

router = APIRouter()


@router.post("/analyze/audio", response_model=AnalyzeResponse)
def analyze_audio_endpoint(payload: AnalyzeAudioRequest):
    result = analyze_audio(
        duration=payload.audio_duration_seconds,
        ayah_reference=payload.ayah_reference
    )

    return {
        "engine": "mock-audio",
        "confidence_score": result["confidence"],
        "mistakes": result.get("tajweed_errors", []),
        "corrections": []
    }
