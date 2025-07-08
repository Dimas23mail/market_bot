from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper
from .delivery_status_schemas import (DeliveryStatus, DeliveryStatusCreate, DeliveryStatusUpdate,
                                      DeliveryStatusUpdatePartial)
from .dependencies import delivery_status_by_id
from . import delivery_status_crud


router = APIRouter(tags=["Delivery Status"])


@router.get("/", response_model=list[DeliveryStatus])
async def get_products(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await delivery_status_crud.get_all_delivery_status(session=session)


@router.post("/", response_model=DeliveryStatus, status_code=status.HTTP_201_CREATED)
async def create_product(delivery_status_in: DeliveryStatusCreate,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await delivery_status_crud.create_delivery_status(session=session, delivery_status_in=delivery_status_in)


@router.get("/{delivery_status_by_id}/", response_model=DeliveryStatus)
async def get_products_by_id(delivery_status: DeliveryStatus = Depends(delivery_status_by_id)):
    return delivery_status


@router.put("/{delivery_status_id}/")
async def update_delivery_type(
        delivery_status_update: DeliveryStatusUpdate,
        delivery_status: DeliveryStatus = Depends(delivery_status_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await delivery_status_crud.update_delivery_status(
        session=session,
        delivery_status=delivery_status,
        delivery_status_update=delivery_status_update)
