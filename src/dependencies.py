from typing import Annotated

from fastapi import Depends, Request
from psycopg import Connection

from src.crud import CRUD


__all__ = [
    'get_conn',
    'get_crud',
]


def get_conn(request: Request) -> Connection:
    with request.state.conn_pool.connection() as conn:
        yield conn


def get_crud(conn: Annotated[Connection, Depends(get_conn)]) -> CRUD:
    return CRUD(conn)
