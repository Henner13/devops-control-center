from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.schemas.role import (
    RoleCreate,
    RoleResponse
)

from app.services.role_service import(
    create_role,
    get_roles,
    get_role_by_id
)

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

# Endpoitn POST
@router.post(
    "",
    response_model=RoleResponse
)
def create_new_role(
    role: RoleCreate,
    db: Session = Depends(get_db)
):
    return create_role(db, role)

# Endpoint GET ALL
@router.get(
    "",
    response_model=list[RoleResponse]
)
def list_roles(
    db: Session = Depends(get_db)
):
    return get_roles(db)

# Endpoint GET BY ID
@router.get(
    "/{role_id}",
    response_model=RoleResponse
)
def get_role(
    role_id: int,
    db: Session = Depends(get_db)
):
    role = get_role_by_id(
        db,
        role_id
    )

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    return role
