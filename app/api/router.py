from fastapi import APIRouter
from app.api.health import router as health_router
from app.api.analyze_audio import router as audio_router
from app.api.analyze_text import router as text_router

router = APIRouter()

router.include_router(health_router)
router.include_router(text_router)
router.include_router(audio_router)
