from fastapi import APIRouter, Form
from app.core.security import enforce_submission_limit
from app.core.controller import analyze_audio

router = APIRouter()

@router.post("/audio")
async def analyze_audio_endpoint(
    ayah_ref: str = Form(...),
    submission_count: int = Form(...)
):
    enforce_submission_limit(submission_count)
    result = await analyze_audio(ayah_ref=ayah_ref)
    return result
