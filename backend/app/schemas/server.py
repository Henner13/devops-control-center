import re

from enum import Enum

from pydantic import (
    BaseModel,
    Field,
    IPvAnyAddress,
    field_validator
)


class EnvironmentEnum(str, Enum):
    development = "development"
    preproduction = "preproduction"
    production = "production"


class StatusEnum(str, Enum):
    online = "online"
    offline = "offline"
    unknown = "unknown"


def validate_hostname_value(
    hostname: str
) -> str:

    hostname = hostname.strip().lower()

    pattern = (
        r"^(?!-)"
        r"[a-z0-9-]+"
        r"(\.[a-z0-9-]+)*"
        r"(?<!-)$"
    )

    if not re.match(pattern, hostname):
        raise ValueError(
            "Invalid hostname format"
        )

    return hostname


class ServerCreate(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100
    )

    hostname: str = Field(
        min_length=3,
        max_length=255
    )

    ip_address: IPvAnyAddress

    os_name: str = Field(
        min_length=2,
        max_length=50
    )

    os_version: str = Field(
        min_length=1,
        max_length=50
    )

    environment: EnvironmentEnum

    description: str | None = Field(
        default=None,
        max_length=255
    )

    @field_validator("hostname")
    @classmethod
    def validate_hostname(
        cls,
        hostname: str
    ) -> str:
        return validate_hostname_value(hostname)


class ServerUpdate(BaseModel):

    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    hostname: str | None = Field(
        default=None,
        min_length=3,
        max_length=255
    )

    ip_address: IPvAnyAddress | None = None

    os_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    os_version: str | None = Field(
        default=None,
        min_length=1,
        max_length=50
    )

    environment: EnvironmentEnum | None = None

    status: StatusEnum | None = None

    description: str | None = Field(
        default=None,
        max_length=255
    )

    @field_validator("hostname")
    @classmethod
    def validate_hostname(
        cls,
        hostname: str | None
    ) -> str | None:

        if hostname is None:
            return None

        return validate_hostname_value(hostname)


class ServerResponse(BaseModel):

    id: int

    name: str

    hostname: str

    ip_address: IPvAnyAddress

    os_name: str

    os_version: str

    environment: EnvironmentEnum

    status: StatusEnum

    description: str | None

    created_by: int

    model_config = {
        "from_attributes": True
    }
