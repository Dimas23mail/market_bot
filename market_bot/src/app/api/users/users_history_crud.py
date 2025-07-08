"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import UserHistory

from .users_history_schemas import CreateUserHistory, UpdateUserHistory, UserHistoryUpdatePartial


async def get_users_history(session: AsyncSession) -> list[UserHistory]:
    stmt = select(UserHistory).order_by(UserHistory.id)
    result: Result = await session.execute(stmt)
    users_history = result.scalars().all()
    return list(users_history)


async def get_user_history(session: AsyncSession, user_history_id: int) -> UserHistory | None:
    return await session.get(UserHistory, user_history_id)


async def create_user_history(session: AsyncSession, user_history_in: CreateUserHistory) -> UserHistory:
    user_history = UserHistory(**user_history_in.model_dump())
    session.add(user_history)
    await session.commit()
    await session.refresh(user_history)
    return user_history


async def update_user_history(
        session: AsyncSession,
        user_history: UserHistory,
        user_history_update: UpdateUserHistory | UserHistoryUpdatePartial,
        partial: bool = False
) -> UserHistory:
    for key, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user_history, key, value)
    await session.commit()
    return user_history


async def delete_user_history(
        session: AsyncSession,
        user_history: UserHistory) -> None:
    await session.delete(user_history)
    await session.commit()
