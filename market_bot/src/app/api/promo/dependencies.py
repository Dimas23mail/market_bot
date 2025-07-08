from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import db_helper
from .promo_schemas import Promo
from . import promo_crud


async def promo_by_id(
        promo_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Promo:
    promo = await promo_crud.get_promo(session=session, promo_id=promo_id)
    if promo:
        return promo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {promo_id} not found!"
    )
