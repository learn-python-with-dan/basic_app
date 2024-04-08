from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, computed_field


__all__ = [
    'User',
    'UserInput',
    'UserUpdate',
]


class User(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    last_updated_at: datetime | None = None


class UserInput(BaseModel):
    name: str

    @computed_field
    def id(self) -> UUID:
        return uuid4()

    @computed_field
    def created_at(self) -> datetime:
        return datetime.now()


class UserUpdate(BaseModel):
    name: str

    @computed_field
    def last_updated_at(self) -> datetime:
        return datetime.now()
