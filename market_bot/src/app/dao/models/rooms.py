from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.base import intpk, Base


class MainRoom(Base):
    __tablename__ = "main_rooms"

    id: Mapped[intpk]
    room: Mapped[str] = mapped_column(String)
