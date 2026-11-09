from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import (
    verify_password,
    create_access_token
)

def login_user(
    db: Session,
    username: str,
    password: str
):
    user = db.query(User).filter(
        User.email == username
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    if not verify_password(
        password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        {
            "sub": user.email,
            "user_id": user.id,
            "role_id": user.role_id
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }