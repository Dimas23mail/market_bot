from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import db_helper
from .users_schemas import User
from . import users_crud
from .users_history_schemas import UserHistory
from . import users_history_crud


async def user_by_id(
        user_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> User:
    user = await users_crud.get_user(session=session, user_id=user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found!"
    )


async def user_history_by_id(
        user_history_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> UserHistory:
    user_history = await users_history_crud.get_user_history(session=session, user_history_id=user_history_id)
    if user_history:
        return user_history
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_history_id} not found!"
    )