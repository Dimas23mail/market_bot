import datetime
from typing import List, Optional

from sqlalchemy import text, ForeignKey, PickleType, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.base import intpk, Base


class Order(Base):
    __tablename__ = "orders"

    order_date: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    products_id: Mapped[List[int]] = mapped_column(PickleType)
    promo_id: Mapped[Optional[str]] = mapped_column(ForeignKey("promo_action.id"))
    user_name: Mapped[Optional[str]] = mapped_column(String)
    delivery_type_id: Mapped[int] = mapped_column(ForeignKey("delivery_types.id"))
    delivery_address: Mapped[Optional[str]] = mapped_column(Text)
    user_phone: Mapped[str] = mapped_column(String)
    user_email: Mapped[Optional[str]] = mapped_column(String)
    order_confirmation_by_admin: Mapped[bool] = mapped_column(Boolean(), default=False)
    order_payment: Mapped[bool] = mapped_column(Boolean(), default=False)
    order_delivery_status: Mapped[str] = mapped_column(String)
