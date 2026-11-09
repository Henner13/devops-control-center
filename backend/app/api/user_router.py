from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.user import User
from app.db.dependencies import get_db
from app.core.roles import require_admin

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id
)

from app.core.auth import (
    get_current_user
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
    "/me"
)
def get_me(
    current_user = Depends(
        get_current_user
    )
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role_id": current_user.role_id,
        "role_name": current_user.role.name
    }

@router.get("/admin-test")
def admin_test(
    current_user: User = Depends(
        require_admin
    )
):
    return {
        "message": "Admin access granted",
        "username": current_user.username
    }

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

