from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import db_helper
from .orders_schemas import Order
from . import orders_crud


async def order_by_id(
        order_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Order:
    order = await orders_crud.get_order(session=session, order_id=order_id)
    if order:
        return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {order_id} not found!"
    )
