"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import Order

from .orders_schemas import OrderCreate, OrderUpdate, OrderUpdatePartial


async def get_orders(session: AsyncSession) -> list[Order]:
    stmt = select(Order).order_by(Order.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()
    return list(orders)


async def get_order(session: AsyncSession, order_id: int) -> Order | None:
    return await session.get(Order, order_id)


async def create_oder(session: AsyncSession, oder_in: OrderCreate) -> Order:
    order = Order(**oder_in.model_dump())
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


async def update_order(
        session: AsyncSession,
        order: Order,
        order_update: OrderUpdate | OrderUpdatePartial,
        partial: bool = False
) -> Order:
    for key, value in order_update.model_dump(exclude_unset=partial).items():
        setattr(order, key, value)
    await session.commit()
    return order


async def delete_order(
        session: AsyncSession,
        order: Order) -> None:
    await session.delete(order)
    await session.commit()
