"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import MainRoom

from .rooms_schemas import RoomCreate, RoomUpdate


async def get_rooms(session: AsyncSession) -> list[MainRoom]:
    stmt = select(MainRoom).order_by(MainRoom.id)
    result: Result = await session.execute(stmt)
    rooms = result.scalars().all()
    return list(rooms)


async def get_room(session: AsyncSession, room_id: int) -> MainRoom | None:
    return await session.get(MainRoom, room_id)


async def create_room(session: AsyncSession, room_in: RoomCreate) -> MainRoom:
    room = MainRoom(**room_in.model_dump())
    session.add(room)
    await session.commit()
    await session.refresh(room)
    return room


async def update_room(
        session: AsyncSession,
        room: MainRoom,
        room_update: RoomUpdate,
        partial: bool = False
) -> MainRoom:
    for key, value in room_update.model_dump(exclude_unset=partial).items():
        setattr(room, key, value)
    await session.commit()
    return room


async def delete_room(
        session: AsyncSession,
        room: MainRoom) -> None:
    await session.delete(room)
    await session.commit()
