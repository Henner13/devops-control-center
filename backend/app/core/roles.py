from fastapi import Depends
from fastapi import HTTPException

from app.core.auth import get_current_user

from app.models.user import User

def require_admin(
    current_user: User = Depends(
        get_current_user
    )
) -> User:

    if current_user.role.name != "Administrator":
        raise HTTPException(
            status_code=403,
            detail="Admin privileges required"
        )

    return current_user

def require_operator(
    current_user: User = Depends(
        get_current_user
    )
) -> User:

    allowed_roles = [
        "Administrator",
        "Operator"
    ]

    if current_user.role.name not in allowed_roles:
        raise HTTPException(
            status_code=403,
            detail="Operator privileges required"
        )

    return current_user
