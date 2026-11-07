from pydantic import BaseModel


class RoleCreate(BaseModel):
    name: str
    description: str

class RoleResponse(BaseModel):
    id: int
    name: str
    description: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }
