import datetime

from pydantic import BaseModel, ConfigDict


class PromoBase(BaseModel):
    title: str
    percent: int
    fix_price: int
    date_of_finish: datetime.datetime


class PromoCreate(PromoBase):
    pass


class Promo(PromoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class PromoUpdate(PromoCreate):
    pass


class PromoUpdatePartial(PromoCreate):
    title: str | None = None
    percent: int | None = None
    fix_price: int | None = None
    date_of_finish: datetime.datetime | None = None
