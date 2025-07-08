from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper

from .users_history_schemas import UserHistory, CreateUserHistory, UpdateUserHistory, UserHistoryUpdatePartial
from .dependencies import user_history_by_id
from . import users_history_crud


router = APIRouter(tags=["Users History"])


@router.get("/", response_model=list[UserHistory])
async def get_users_history(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_history_crud.get_users_history(session=session)


@router.post("/", response_model=UserHistory, status_code=status.HTTP_201_CREATED)
async def create_user_history(
        user_history_in: CreateUserHistory,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_history_crud.create_user_history(session=session, user_history_in=user_history_in)


@router.get("/{user_id}/", response_model=UserHistory)
async def get_user_history_by_id(user_history: UserHistory = Depends(user_history_by_id)):
    return user


@router.put("/{user_history_id}/")
async def update_user(
        user_history_update: UpdateUserHistory,
        user_history: UserHistory = Depends(user_history_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_history_crud.update_user_history(session=session, user_history=user_history,
                                                        user_history_update=user_history_update)


@router.patch("/{user_history_id}/")
async def update_user_history_partial(
        user_history_update: UserHistoryUpdatePartial,
        user_history: UserHistory = Depends(user_history_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await users_history_crud.update_user_history(
        session=session,
        user_history=user_history,
        user_history_update=user_history_update,
        partial=True
    )


@router.delete("/{user_history_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_history(
        user_history: UserHistory = Depends(user_history_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

) -> None:
    await users_history_crud.delete_user_history(session=session, user_history=user_history)
