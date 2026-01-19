from fastapi import APIRouter
from pydantic import BaseModel
from app.core.security import enforce_submission_limit
from app.core.controller import analyze_text

router = APIRouter()

class TextRequest(BaseModel):
    text: str
    ayah_ref: str
    submission_count: int


@router.post("/text")
async def analyze_text_endpoint(payload: TextRequest):
    enforce_submission_limit(payload.submission_count)
    result = await analyze_text(
        text=payload.text,
        ayah_ref=payload.ayah_ref
    )
    return result
