from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "",
    response_model=UserResponse,
    status_code=201
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        db,
        user
    )

@router.get(
    "",
    response_model=list[UserResponse]
)
def list_users(
    db: Session = Depends(get_db)
):
    return get_users(db)

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user
