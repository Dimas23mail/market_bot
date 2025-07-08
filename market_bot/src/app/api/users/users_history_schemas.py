import datetime

from pydantic import BaseModel, ConfigDict


class UserHistoryBase(BaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: int
    request_history: str
    order_history: str


class CreateUserHistory(UserHistoryBase):
    pass


class UserHistory(UserHistoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class UpdateUserHistory(CreateUserHistory):
    pass


class UserHistoryUpdatePartial(CreateUserHistory):
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
    request_history: str | None = None
    order_history: str | None = None
