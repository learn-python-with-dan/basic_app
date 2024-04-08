from contextlib import asynccontextmanager

from fastapi import FastAPI
from psycopg.conninfo import make_conninfo
from psycopg_pool import ConnectionPool


__all__ = [
    'lifespan'
]


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:

    conn_info = make_conninfo(host='localhost', port=5432, dbname='postgres')
    params = {'options': '-c search_path=demo'}

    with ConnectionPool(conninfo=conn_info, kwargs=params) as conn_pool:
        yield {'conn_pool': conn_pool}
