"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import User

from .users_schemas import CreateUser, UpdateUser, UserUpdatePartial


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: CreateUser) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(
        session: AsyncSession,
        user: User,
        user_update: UpdateUser | UserUpdatePartial,
        partial: bool = False
) -> User:
    for key, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, key, value)
    await session.commit()
    return user


async def delete_user(
        session: AsyncSession,
        user: User) -> None:
    await session.delete(user)
    await session.commit()
