from fastapi import FastAPI
from app.api.router import router

app = FastAPI(
    title="Iqra AI",
    description="Qur'an Recitation Analysis Service",
    version="0.1.0"
)

app.include_router(router)
