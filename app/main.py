from fastapi import FastAPI
from app.api.router import router as api_router
from app.engines.quran.sqlite_loader import QuranSQLiteLoader
from app.core.quran_repo import QuranRepository

app = FastAPI(
    title="Iqra AI",
    description="Qur'an Recitation Analysis Service",
    version="0.1.0"
)

app.include_router(api_router)

quran_loader = QuranSQLiteLoader("data/quran.db")
quran_repo = QuranRepository(quran_loader)
