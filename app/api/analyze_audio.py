from fastapi import APIRouter, UploadFile, File, Form
from app.schemas.response import AnalysisResponse
from app.core.controller import analyze_audio_controller

router = APIRouter()


@router.post("/audio", response_model=AnalysisResponse)
async def analyze_audio(
    surah: int = Form(...),
    ayah: int = Form(...),
    audio: UploadFile = File(...)
):
    audio_bytes = await audio.read()

    return analyze_audio_controller(
        surah=surah,
        ayah=ayah,
        audio_bytes=audio_bytes
    )
