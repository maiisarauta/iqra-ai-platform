from fastapi import APIRouter
from app.schemas.request import TextAnalysisRequest
from app.schemas.response import AnalysisResponse
from app.core.controller import analyze_text_controller

router = APIRouter()


@router.post("/text", response_model=AnalysisResponse)
def analyze_text(payload: TextAnalysisRequest):
    return analyze_text_controller(
        surah=payload.surah,
        ayah=payload.ayah,
        text=payload.text
    )
