from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper

from .product_type_schemas import ProductType, ProductTypeCreate, ProductTypeUpdate, ProductTypeUpdatePartial
from .dependencies import product_by_id
from . import product_type_crud


router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[ProductType])
async def get_product_types(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await product_type_crud.get_product_types(session=session)


@router.post("/", response_model=ProductType, status_code=status.HTTP_201_CREATED)
async def create_product_type(product_type_in: ProductTypeCreate,
                              session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await product_type_crud.create_product_type(session=session, product_type_in=product_type_in)


@router.get("/{product_type_id}/", response_model=ProductType)
async def get_product_type_by_id(product_type: ProductType = Depends(product_by_id)):
    return product_type


@router.put("/{product_type_id}/")
async def update_product_type(product_type_update: ProductTypeUpdate,
                              product_type: ProductType = Depends(product_by_id),
                              session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await product_type_crud.update_product_type(session=session, product_type=product_type,
                                                       product_type_update=product_type_update)


@router.patch("/{product_type_id}/")
async def update_product_type_partial(product_type_update: ProductTypeUpdatePartial,
                                      product_type: ProductType = Depends(product_by_id),
                                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await product_type_crud.update_product_type(
        session=session,
        product_type=product_type,
        product_type_update=product_type_update,
        partial=True
    )


@router.delete("/{product_type_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_type(
        product_type: ProductType = Depends(product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

) -> None:
    await product_type_crud.delete_product_type(session=session, product_type=product_type)
