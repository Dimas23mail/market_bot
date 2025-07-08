"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import DeliveryType

from .delivery_type_schemas import DeliveryTypeCreate, DeliveryTypeUpdate, DeliveryTypeUpdatePartial


async def get_delivery_types(session: AsyncSession) -> list[DeliveryType]:
    stmt = select(DeliveryType).order_by(DeliveryType.id)
    result: Result = await session.execute(stmt)
    delivery_types = result.scalars().all()
    return list(delivery_types)


async def get_delivery_type(session: AsyncSession, delivery_type_id: int) -> DeliveryType | None:
    return await session.get(DeliveryType, delivery_type_id)


async def create_delivery_type(session: AsyncSession, delivery_type_in: DeliveryTypeCreate) -> DeliveryType:
    delivery_type = DeliveryType(**delivery_type_in.model_dump())
    session.add(delivery_type)
    await session.commit()
    await session.refresh(delivery_type)
    return delivery_type


async def update_delivery_type(
        session: AsyncSession,
        delivery_type: DeliveryType,
        delivery_type_update: DeliveryTypeUpdate | DeliveryTypeUpdatePartial,
        partial: bool = False
) -> DeliveryType:
    for key, value in delivery_type_update.model_dump(exclude_unset=partial).items():
        setattr(delivery_type, key, value)
    await session.commit()
    return delivery_type


async def delete_delivery_type(
        session: AsyncSession,
        delivery_type: DeliveryType) -> None:
    await session.delete(delivery_type)
    await session.commit()
