from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.dao.base import intpk, Base


class DeliveryStatus(Base):
    __tablename__ = "delivery_status"

    id: Mapped[intpk]
    status: Mapped[str] = mapped_column(String)


class DeliveryType(Base):
    __tablename__ = "delivery_types"

    id: Mapped[intpk]
    type: Mapped[str]
    delivery_floor: Mapped[int]
    delivery_price: Mapped[int]
    price_for_floor: Mapped[int]
