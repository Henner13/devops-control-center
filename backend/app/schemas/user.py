import re

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )

    role_id: int

    @field_validator("password")
    @classmethod
    def validate_password(
        cls,
        password: str
    ) -> str:

        if not re.search(r"[A-Z]", password):
            raise ValueError(
                "Password must contain at least one uppercase letter"
            )

        if not re.search(r"[a-z]", password):
            raise ValueError(
                "Password must contain at least one lowercase letter"
            )

        if not re.search(r"\d", password):
            raise ValueError(
                "Password must contain at least one number"
            )

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password):
            raise ValueError(
                "Password must contain at least one special character"
            )

        return password

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role_id: int

    model_config = {
        "from_attributes": True
    }


class UserLogin(BaseModel):
    email: EmailStr
    password: str