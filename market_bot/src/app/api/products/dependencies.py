from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import db_helper
from .products_schemas import Product
from . import products_crud
from .product_type_schemas import ProductType
from . import product_type_crud


async def product_by_id(
        product_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Product:
    product = await products_crud.get_product(session=session, product_id=product_id)
    if product:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!"
    )


async def product_type_by_id(
        product_type_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ProductType:
    product_type = await product_type_crud.get_product_type(session=session, product_type_id=product_type_id)
    if product_type:
        return product_type
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_type_id} not found!"
    )
