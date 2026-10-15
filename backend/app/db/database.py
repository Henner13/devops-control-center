from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

import app.models

engine = create_engine(
    settings.database_url
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
