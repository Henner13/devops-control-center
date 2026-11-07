from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password

from app.models.user import User
from app.models.role import Role

from app.schemas.user import UserCreate

# crear el usuario
def create_user(
    db: Session,
    user_data: UserCreate
):
    # Comprobar que el usuario no esta duplicado
    existing_username = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if existing_username:
        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )
    
    # Comprobar no email duplicado
    existing_email = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    # Comprobar si existe el rol
    role = db.query(Role).filter(
        Role.id == user_data.role_id
    ).first()

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    # Crear hash
    print(f"PASSWORD: {user_data.password}")
    print(f"LEN: {len(user_data.password)}")
    
    password_hash = hash_password(
        user_data.password
    )

    # Crear usuario
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=password_hash,
        role_id=user_data.role_id
    )

    # Guardar en la db
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_users(
    db: Session
):
    return db.query(User).all()


def get_user_by_id(
    db: Session,
    user_id: int
):
    return db.query(User).filter(
        User.id == user_id
    ).first()
