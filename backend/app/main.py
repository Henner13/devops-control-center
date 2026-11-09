from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine
from app.api.role_router import router as role_router
from app.api.user_router import router as user_router
from app.api.auth_router import router as auth_router
from app.api.server_router import (
    router as server_router
)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

app.include_router(role_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(server_router)


@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "status": "running"
    }