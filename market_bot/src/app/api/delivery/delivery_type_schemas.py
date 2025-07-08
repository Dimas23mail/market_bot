from pydantic import BaseModel, ConfigDict


class DeliveryTypeBase(BaseModel):
    type: str
    delivery_floor: int
    delivery_price: int
    price_for_floor: int


class DeliveryTypeCreate(DeliveryTypeBase):
    pass


class DeliveryType(DeliveryTypeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class DeliveryTypeUpdate(DeliveryTypeCreate):
    pass


class DeliveryTypeUpdatePartial(DeliveryTypeCreate):
    type: str | None = None
    delivery_floor: int | None = None
    delivery_price: int | None = None
    price_for_floor: int | None = None
