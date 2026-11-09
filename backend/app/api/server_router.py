from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.core.auth import get_current_user
from app.core.roles import (
    require_admin,
    require_operator
)

from app.models.user import User

from app.schemas.server import (
    ServerCreate,
    ServerUpdate,
    ServerResponse
)

from app.services.server_service import (
    create_server,
    get_servers,
    get_server_by_id,
    update_server,
    delete_server
)

router = APIRouter(
    prefix="/servers",
    tags=["Servers"]
)

@router.get(
    "",
    response_model=list[ServerResponse]
)
def list_servers(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_servers(db)

@router.get(
    "/{server_id}",
    response_model=ServerResponse
)
def get_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):
    return get_server_by_id(
        db,
        server_id
    )

@router.post(
    "",
    response_model=ServerResponse,
    status_code=201
)
def create_new_server(
    server: ServerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_operator
    )
):
    return create_server(
        db,
        server,
        current_user.id
    )

@router.put(
    "/{server_id}",
    response_model=ServerResponse
)
def update_existing_server(
    server_id: int,
    server_data: ServerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_operator
    )
):
    return update_server(
        db,
        server_id,
        server_data
    )

@router.delete(
    "/{server_id}"
)
def remove_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_admin
    )
):
    return delete_server(
        db,
        server_id
    )
