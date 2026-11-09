from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.server import Server

from app.schemas.server import (
    ServerCreate,
    ServerUpdate
)


def create_server(
    db: Session,
    server_data: ServerCreate,
    user_id: int
):
    existing_ip = db.query(Server).filter(
        Server.ip_address == str(server_data.ip_address)
    ).first()

    if existing_ip:
        raise HTTPException(
            status_code=409,
            detail="IP address already exists"
        )

    existing_hostname = db.query(Server).filter(
        Server.hostname == server_data.hostname
    ).first()

    if existing_hostname:
        raise HTTPException(
            status_code=409,
            detail="Hostname already exists"
        )

    server = Server(
        name=server_data.name,
        hostname=server_data.hostname,
        ip_address=str(server_data.ip_address),
        os_name=server_data.os_name,
        os_version=server_data.os_version,
        environment=server_data.environment.value,
        status="unknown",
        description=server_data.description,
        created_by=user_id
    )

    db.add(server)

    db.commit()

    db.refresh(server)

    return server


def get_servers(
    db: Session
):
    return db.query(Server).all()


def get_server_by_id(
    db: Session,
    server_id: int
):
    server = db.query(Server).filter(
        Server.id == server_id
    ).first()

    if not server:
        raise HTTPException(
            status_code=404,
            detail="Server not found"
        )

    return server


def update_server(
    db: Session,
    server_id: int,
    server_data: ServerUpdate
):
    server = get_server_by_id(
        db,
        server_id
    )

    update_data = server_data.model_dump(
        exclude_unset=True
    )

    if "ip_address" in update_data:

        existing_ip = db.query(Server).filter(
            Server.ip_address == str(update_data["ip_address"]),
            Server.id != server_id
        ).first()

        if existing_ip:
            raise HTTPException(
                status_code=409,
                detail="IP address already exists"
            )

        update_data["ip_address"] = str(
            update_data["ip_address"]
        )

    if "hostname" in update_data:

        existing_hostname = db.query(Server).filter(
            Server.hostname == update_data["hostname"],
            Server.id != server_id
        ).first()

        if existing_hostname:
            raise HTTPException(
                status_code=409,
                detail="Hostname already exists"
            )

    if "environment" in update_data:
        update_data["environment"] = (
            update_data["environment"].value
        )

    if "status" in update_data:
        update_data["status"] = (
            update_data["status"].value
        )

    for field, value in update_data.items():
        setattr(
            server,
            field,
            value
        )

    db.commit()

    db.refresh(server)

    return server


def delete_server(
    db: Session,
    server_id: int
):
    server = get_server_by_id(
        db,
        server_id
    )

    db.delete(server)

    db.commit()

    return {
        "message": "Server deleted successfully"
    }
