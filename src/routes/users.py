from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Path, status

from src.crud import CRUD
from src.dependencies import get_crud
from src.models import *


__all__ = [
    'router',
]


router = APIRouter(
    tags=['Users'],
    prefix='/users',
)


@router.post(path='', response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(
        crud: Annotated[CRUD, Depends(get_crud)],
        input: Annotated[UserInput, Body(...)],
) -> User:
    user_id = crud.insert_user(input)
    return crud.get_user(user_id)


@router.get(path='/{user_id}', response_model=User, status_code=status.HTTP_200_OK)
def get_user(
        crud: Annotated[CRUD, Depends(get_crud)],
        user_id: Annotated[UUID, Path(...)],
) -> User:
    return crud.get_user(user_id)


@router.put(path='/{user_id}', response_model=User, status_code=status.HTTP_200_OK)
def update_user(
        crud: Annotated[CRUD, Depends(get_crud)],
        user_id: Annotated[UUID, Path(...)],
        update: Annotated[UserUpdate, Body(...)],
) -> User:
    user_id = crud.update_user(user_id, update)
    return crud.get_user(user_id)


@router.delete(path='/{user_id}', response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def update_user(
        crud: Annotated[CRUD, Depends(get_crud)],
        user_id: Annotated[UUID, Path(...)],
) -> None:
    crud.delete_user(user_id)
