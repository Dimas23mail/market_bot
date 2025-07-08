from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import db_helper
from .delivery_type_schemas import DeliveryType
from . import delivery_type_crud
from .delivery_status_schemas import DeliveryStatus
from . import delivery_status_crud


async def delivery_type_by_id(
        delivery_type_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> DeliveryType:
    delivery_type = await delivery_type_crud.get_delivery_type(session=session, delivery_type_id=delivery_type_id)
    if delivery_type:
        return delivery_type
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Delivery_type {delivery_type_id} not found!"
    )


async def delivery_status_by_id(
        delivery_status_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> DeliveryStatus:
    delivery_status = await delivery_status_crud.get_one_delivery_status(
        session=session,
        delivery_status_id=delivery_status_id
    )
    if delivery_status:
        return delivery_status
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Delivery_type {delivery_status_id} not found!"
    )
