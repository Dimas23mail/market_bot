from pydantic import BaseModel, ConfigDict


class RoomBase(BaseModel):

    room: str


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class RoomUpdate(RoomCreate):
    pass
