import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.base import intpk, Base


class PromoAction(Base):
    __tablename__ = "promo_action"

    title: Mapped[str] = mapped_column(String)
    percent: Mapped[int] = mapped_column(Integer)
    fix_price: Mapped[int] = mapped_column(Integer)
    date_of_finish: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.UTC
    )
