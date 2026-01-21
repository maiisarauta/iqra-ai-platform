from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import enforce_submission_limit
from app.core.controller import analyze_text
from app.schemas.request import AnalyzeTextRequest
from app.schemas.response import AnalyzeResponse
from app.scoring.confidence import calculate_confidence

router = APIRouter()


@router.post("/analyze/text", response_model=AnalyzeResponse)
def analyze_text(payload: AnalyzeTextRequest):
    mistakes = []

    confidence = calculate_confidence(mistakes)

    return {
        "engine": "mock-text",
        "confidence_score": confidence,
        "mistakes": mistakes,
        "corrections": []
    }
