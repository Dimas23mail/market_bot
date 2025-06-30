import datetime
from decimal import Decimal
from typing import Optional, List
from sqlalchemy import Integer, Text, ForeignKey, DateTime, text, String, Numeric, PickleType, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..dao.base import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)

    history: Mapped["UserHistory"] = relationship(
        "UserHistory",
        back_populates="user",
        lazy="joined"
    )
    orders: Mapped["Order"] = relationship(
        "Order",
        back_populates="user",
        lazy="joined"
    )


class UserHistory(Base):
    __tablename__ = "users_history"

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.UTC,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), server_default=text("1"))
    request_history: Mapped[List[str]] = mapped_column(PickleType)
    order_history: Mapped[List[str]] = mapped_column(PickleType)

    user: Mapped["User"] = relationship(
        "User",
        back_populates="history",
        lazy="joined"
    )


class PromoAction(Base):
    __tablename__ = "promo_action"

    title: Mapped[str] = mapped_column(String)
    percent: Mapped[int] = mapped_column(Integer)
    fix_price: Mapped[int] = mapped_column(Integer)
    date_of_finish: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.UTC
    )

    orders: Mapped["Order"] = relationship(
        "Order",
        back_populates="promo",
        lazy="joined"
    )
    orders_promo: Mapped["Order"] = relationship(
        "Order",
        back_populates="promos",
        lazy="joined"
    )


class MainRoom(Base):
    __tablename__ = "main_rooms"

    room: Mapped[str] = mapped_column(String)

    products: Mapped["Product"] = relationship(
        "Product",
        back_populates="room",
        lazy="joined"
    )


class MenuItem(Base):
    __tablename__ = "menu_items"

    title: Mapped[str] = mapped_column(String)
    word: Mapped[str] = mapped_column(String)
    imageURL: Mapped[str] = mapped_column(String)


class Product(Base):
    __tablename__ = "products_list"

    title: Mapped[str] = mapped_column(String)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    imageURL: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    availability: Mapped[int] = mapped_column(Integer)
    allImagesURL: Mapped[List[str]] = mapped_column(PickleType)
    color: Mapped[str] = mapped_column(String)
    room_id: Mapped[int] = mapped_column(ForeignKey("MainRoom.id"))
    item_type_id: Mapped[int] = mapped_column(ForeignKey("ProductType.id"))

    orders: Mapped["Order"] = relationship(
        "Order",
        back_populates="products",
        lazy="joined"
    )
    room: Mapped["MainRoom"] = relationship(
        "MainRoom",
        back_populates="products",
        lazy="joined"
    )
    product_type: Mapped["ProductType"] = relationship(
        "ProductType",
        back_populates="products",
        lazy="joined"
    )


class Order(Base):
    __tablename__ = "orders"

    order_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.UTC,
        nullable=False
    )
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

    products: Mapped["Product"] = relationship(
        "Product",
        back_populates="orders",
        lazy="joined"
    )
    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders",
        lazy="joined"
    )
    promo: Mapped["PromoAction"] = relationship(
        "PromoAction",
        back_populates="orders",
        lazy="joined"
    )
    delivery_status: Mapped["DeliveryStatus"] = relationship(
        "DeliveryStatus",
        back_populates="orders",
        lazy="joined"
    )
    delivery_type: Mapped["DeliveryType"] = relationship(
        "DeliveryType",
        back_populates="orders",
        lazy="joined"
    )


class DeliveryStatus(Base):
    __tablename__ = "delivery_status"

    status: Mapped[str] = mapped_column(String)

    orders: Mapped["Order"] = relationship(
        "Order",
        back_populates="delivery_status",
        lazy="joined"
    )


class DeliveryType(Base):
    __tablename__ = "delivery_types"

    type: Mapped[str] = mapped_column(String)

    orders: Mapped["Order"] = relationship(
        "Order",
        back_populates="delivery_type",
        lazy="joined"
    )


class ProductType(Base):
    __tablename__ = "products_types"

    type: Mapped[str] = mapped_column(String)

    products: Mapped["Product"] = relationship(
        "Product",
        back_populates="product_type",
        lazy="joined"
    )
