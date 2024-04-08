from typing import TypeVar
from uuid import UUID

from psycopg import Connection
from psycopg.rows import class_row
from pydantic import BaseModel

from src.models import *
from src.statements import *


__all__ = [
    'CRUD'
]


T = TypeVar('T')


class CRUD:

    def __init__(self, conn: Connection):
        self.conn = conn

    def _insert_resource(self, stmt: str, input: BaseModel) -> UUID:
        with self.conn.cursor() as cursor:
            cursor.execute(stmt, input.model_dump())
            return cursor.fetchone()[0]

    def _get_resource(self, stmt: str, model_class: type[T], **kwargs) -> T | None:
        with self.conn.cursor(row_factory=class_row(model_class)) as cursor:
            cursor.execute(stmt, kwargs)
            return cursor.fetchone()

    def _update_resource(self, stmt: str, update: BaseModel, **kwargs) -> UUID | None:
        with self.conn.cursor() as cursor:
            kwargs.update(update.model_dump())
            cursor.execute(stmt, kwargs)
            return cursor.fetchone()[0]

    def _delete_resource(self, stmt: str, **kwargs) -> None:
        with self.conn.cursor() as cursor:
            cursor.execute(stmt, kwargs)

    def insert_user(self, input: UserInput) -> UUID:
        return self._insert_resource(insert_user_stmt, input)

    def get_user(self, id: UUID) -> User | None:
        return self._get_resource(get_user_stmt, User, id=id)

    def update_user(self, id: UUID, update: UserUpdate) -> UUID | None:
        return self._update_resource(update_user_stmt, update, id=id)

    def delete_user(self, id: UUID) -> None:
        return self._delete_resource(delete_user_stmt, id=id)
