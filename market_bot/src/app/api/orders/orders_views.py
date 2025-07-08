from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper
from .orders_schemas import Order, OrderCreate, OrderUpdate, OrderUpdatePartial
from .dependencies import order_by_id
from . import orders_crud


router = APIRouter(tags=["Orders"])


@router.get("/", response_model=list[Order])
async def get_orders(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await orders_crud.get_orders(session=session)


@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(order_in: OrderCreate,
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await orders_crud.create_oder(session=session, oder_in=order_in)


@router.get("/{order_id}/", response_model=Order)
async def get_order_by_id(order: Order = Depends(order_by_id)):
    return order


@router.put("/{order_id}/")
async def update_order(order_update: OrderUpdate,
                       order: Order = Depends(order_by_id),
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await orders_crud.update_order(session=session, order=order, order_update=order_update)


@router.patch("/{order_id}/")
async def update_order_partial(
        order_update: OrderUpdatePartial,
        order: Order = Depends(order_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await orders_crud.update_order(
        session=session,
        order=order,
        order_update=order_update,
        partial=True
    )


@router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
        order: Order = Depends(order_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

) -> None:
    await orders_crud.delete_order(session=session, order=order)
