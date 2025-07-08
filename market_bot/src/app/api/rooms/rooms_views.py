from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper
from .rooms_schemas import Room, RoomCreate, RoomUpdate
from .dependencies import room_by_id
from . import rooms_crud


router = APIRouter(tags=["Main Rooms"])


@router.get("/", response_model=list[Room])
async def get_rooms(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await rooms_crud.get_rooms(session=session)


@router.post("/", response_model=Room, status_code=status.HTTP_201_CREATED)
async def create_room(
        room_in: RoomCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await rooms_crud.create_room(session=session, room_in=room_in)


@router.get("/{room_id}/", response_model=Room)
async def get_room_by_id(room: Room = Depends(room_by_id)):
    return room


@router.put("/{room_id}/")
async def update_room(room_update: RoomUpdate,
                      room: Room = Depends(room_by_id),
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await rooms_crud.update_room(session=session, room=room, room_update=room_update)


@router.delete("/{room_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_room(
        room: Room = Depends(room_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

) -> None:
    await rooms_crud.delete_room(session=session, room=room)
