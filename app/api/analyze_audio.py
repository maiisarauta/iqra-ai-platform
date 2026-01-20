from fastapi import APIRouter, Form, UploadFile, File
from app.core.security import enforce_submission_limit
from app.core.controller import analyze_audio
from app.schemas.request import AnalyzeAudioRequest
from app.schemas.response import AnalyzeResponse

router = APIRouter()


@router.post("/analyze/audio", response_model=AnalyzeResponse)
def analyze_audio(
    payload: AnalyzeAudioRequest,
    audio: UploadFile = File(...)
):
    return {
        "engine": "mock-audio",
        "confidence_score": 0.88,
        "mistakes": [],
        "corrections": []
    }
