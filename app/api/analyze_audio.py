from fastapi import APIRouter, UploadFile, File, Form
from app.schemas.request import AnalyzeAudioRequest
from app.schemas.response import AnalysisResponse
from app.core.controller import AnalysisController

router = APIRouter()


@router.post("/analyze/audio", response_model=AnalysisResponse)
async def analyze_audio_endpoint(
    ayah_reference: str = Form(...),
    audio: UploadFile = File(...)
):
    audio_bytes = await audio.read()

    return AnalysisController.analyze_audio(
        audio_bytes=audio_bytes,
        ayah_reference=ayah_reference
    )
