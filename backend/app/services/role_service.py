from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.role import Role
from app.schemas.role import RoleCreate

from fastapi import HTTPException

def create_role(
        db: Session,
        role_data: RoleCreate
):
    existing_role = db.query(Role).filter(
        Role.name == role_data.name
    ).first()

    if existing_role:
        raise HTTPException(
            status_code=409,
            detail="Role already exists"
        )

    role = Role(
        name=role_data.name,
        description=role_data.description
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role

def get_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(
        db: Session,
        role_id: int
):
    return db.query(Role).filter(
        Role.id == role_id
    ).first()
