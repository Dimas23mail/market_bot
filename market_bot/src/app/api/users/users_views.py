from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper
from .users_schemas import User, CreateUser, UpdateUser, UserUpdatePartial
from .dependencies import user_by_id
from . import users_crud


router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[User])
async def get_users(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_crud.get_users(session=session)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
        user_in: CreateUser,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_crud.create_user(session=session, user_in=user_in)


@router.get("/{user_id}/", response_model=User)
async def get_user_by_id(user: User = Depends(user_by_id)):
    return user


@router.put("/{user_id}/")
async def update_user(
        user_update: UpdateUser,
        user: User = Depends(user_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_crud.update_user(session=session, user=user, user_update=user_update)


@router.patch("/{user_id}/")
async def update_user_partial(
        user_update: UserUpdatePartial,
        user: User = Depends(user_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        user: User = Depends(user_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

) -> None:
    await users_crud.delete_user(session=session, user=user)
