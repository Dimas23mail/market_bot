from typing import List

from sqlalchemy import String, Text, Integer, PickleType, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.dao.base import intpk, Base


class Product(Base):
    __tablename__ = "products"

    title: Mapped[str]
    price: Mapped[int]
    imageURL: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    availability: Mapped[int]
    allImagesURL: Mapped[List[str]] = mapped_column(PickleType)
    color: Mapped[str]
    room_id: Mapped[int] = mapped_column(ForeignKey("main_rooms.id"))
    product_type_id: Mapped[int] = mapped_column(ForeignKey("products_types.id"))


class ProductType(Base):
    __tablename__ = "products_types"

    title: Mapped[str] = mapped_column(String)
    word: Mapped[str] = mapped_column(String)
    imageURL: Mapped[str] = mapped_column(String)
