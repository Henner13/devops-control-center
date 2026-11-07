from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app.api.role_router import router as role_router

app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

app.include_router(role_router)

@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "status": "running"
    }