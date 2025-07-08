from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import db_helper
from .rooms_schemas import Room
from . import rooms_crud


async def room_by_id(
        room_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Room:
    room = await rooms_crud.get_room(session=session, room_id=room_id)
    if room:
        return room
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Room {room_id} not found!"
    )
