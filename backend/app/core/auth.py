from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.models.user import User

from app.core.security import (
    decode_access_token,
    oauth2_scheme
)

def get_current_user(
    token: str = Depends(
        oauth2_scheme
    ),
    db: Session = Depends(get_db)
) -> User:
    payload = decode_access_token(
        token
    )

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
    user_id = payload.get(
        "user_id"
    )

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
