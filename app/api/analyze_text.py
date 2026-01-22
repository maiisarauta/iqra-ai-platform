from fastapi import APIRouter
from app.schemas.request import AnalyzeTextRequest
from app.schemas.response import AnalysisResponse
from app.core.controller import AnalysisController

router = APIRouter()


@router.post("/analyze/text", response_model=AnalysisResponse)
def analyze_text(payload: AnalyzeTextRequest):
    return AnalysisController.analyze_text(
        text=payload.text,
        ayah_reference=payload.ayah_reference
    )
