from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper
from .delivery_type_schemas import DeliveryType, DeliveryTypeCreate, DeliveryTypeUpdate, DeliveryTypeUpdatePartial
from .dependencies import delivery_type_by_id
from . import delivery_type_crud


router = APIRouter(tags=["Delivery Types"])


@router.get("/", response_model=list[DeliveryType])
async def get_products(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await delivery_type_crud.get_delivery_types(session=session)


@router.post("/", response_model=DeliveryType, status_code=status.HTTP_201_CREATED)
async def create_product(delivery_type_in: DeliveryTypeCreate,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await delivery_type_crud.create_delivery_type(session=session, delivery_type_in=delivery_type_in)


@router.get("/{delivery_type_by_id}/", response_model=DeliveryType)
async def get_products_by_id(delivery_type: DeliveryType = Depends(delivery_type_by_id)):
    return delivery_type


@router.put("/{delivery_type_id}/")
async def update_delivery_type(
        delivery_type_update: DeliveryTypeUpdate,
        delivery_type: DeliveryType = Depends(delivery_type_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await delivery_type_crud.update_delivery_type(
        session=session,
        delivery_type=delivery_type,
        delivery_type_update=delivery_type_update)
