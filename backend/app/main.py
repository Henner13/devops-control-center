from fastapi import FastAPI

from app.core.config import settings
from app.db.base import Base
from app.db.database import engine


app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "status": "running"
    }