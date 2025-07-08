"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import DeliveryStatus

from .delivery_status_schemas import (DeliveryStatusUpdate, DeliveryStatusUpdatePartial,
                                      DeliveryStatusCreate)


async def get_all_delivery_status(session: AsyncSession) -> list[DeliveryStatus]:
    stmt = select(DeliveryStatus).order_by(DeliveryStatus.id)
    result: Result = await session.execute(stmt)
    delivery_status = result.scalars().all()
    return list(delivery_status)


async def get_one_delivery_status(session: AsyncSession, delivery_status_id: int) -> DeliveryStatus | None:
    return await session.get(DeliveryStatus, delivery_status_id)


async def create_delivery_status(session: AsyncSession, delivery_status_in: DeliveryStatusCreate) -> DeliveryStatus:
    delivery_status = DeliveryStatus(**delivery_status_in.model_dump())
    session.add(delivery_status)
    await session.commit()
    await session.refresh(delivery_status)
    return delivery_status


async def update_delivery_status(
        session: AsyncSession,
        delivery_status: DeliveryStatus,
        delivery_status_update: DeliveryStatusUpdate | DeliveryStatusUpdatePartial,
        partial: bool = False
) -> DeliveryStatus:
    for key, value in delivery_status_update.model_dump(exclude_unset=partial).items():
        setattr(delivery_status, key, value)
    await session.commit()
    return delivery_status


async def delete_delivery_status(
        session: AsyncSession,
        delivery_status: DeliveryStatus) -> None:
    await session.delete(delivery_status)
    await session.commit()
