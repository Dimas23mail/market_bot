from pydantic import BaseModel, ConfigDict


class DeliveryStatusBase(BaseModel):
    status: str


class DeliveryStatusCreate(DeliveryStatusBase):
    pass


class DeliveryStatus(DeliveryStatusBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class DeliveryStatusUpdate(DeliveryStatusCreate):
    pass


class DeliveryStatusUpdatePartial(DeliveryStatusCreate):
    status: str | None = None
