import datetime

from typing import List
from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    order_date: datetime.datetime
    user_id: int
    products_id: List[int]
    promo_id: str | None
    user_name: str | None
    delivery_type_id: int
    delivery_address: str | None
    user_phone: str
    user_email: str | None
    order_confirmation_by_admin: bool
    order_payment: bool
    order_delivery_status: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class OrderUpdate(OrderCreate):
    pass


class OrderUpdatePartial(OrderCreate):
    order_date: datetime.datetime | None = None
    user_id: int | None = None
    products_id: List[int] | None = None
    promo_id: str | None
    user_name: str | None
    delivery_type_id: int | None = None
    delivery_address: str | None
    user_phone: str | None = None
    user_email: str | None
    order_confirmation_by_admin: bool | None = None
    order_payment: bool | None = None
    order_delivery_status: str | None = None
