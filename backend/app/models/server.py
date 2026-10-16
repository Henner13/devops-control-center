from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Server(Base):
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    hostname: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    ip_address: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    os_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    os_version: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    environment: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="unknown"
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    creator = relationship(
        "User",
        back_populates="servers"
    )
