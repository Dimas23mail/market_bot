import datetime

from pydantic import BaseModel, ConfigDict
from annotated_types import MinLen, MaxLen
from typing import Annotated


class UserBase(BaseModel):
    user_name: Annotated[str, MinLen(3), MaxLen(20)] | None
    telegram_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class CreateUser(User):
    pass


class UpdateUser(CreateUser):
    pass


class UserUpdatePartial(CreateUser):
    user_name: str | None = None
    telegram_id: int | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
