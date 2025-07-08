from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.db_helper import db_helper
from .promo_schemas import Promo, PromoCreate, PromoUpdate, PromoUpdatePartial
from .dependencies import promo_by_id
from . import promo_crud


router = APIRouter(tags=["Promo Actions"])


@router.get("/", response_model=list[Promo])
async def get_promos(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await promo_crud.get_promo(session=session)


@router.post("/", response_model=Promo, status_code=status.HTTP_201_CREATED)
async def create_promo(
        promo_in: PromoCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await promo_crud.create_promo(session=session, promo_in=promo_in)


@router.get("/{promo_id}/", response_model=Promo)
async def get_promo_by_id(promo: Promo = Depends(promo_by_id)):
    return promo


@router.put("/{promo_id}/")
async def update_promo(
        promo_update: PromoUpdate,
        promo: Promo = Depends(promo_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await promo_crud.update_promo(session=session, promo=promo, promo_update=promo_update)


@router.patch("/{promo_id}/")
async def update_promo_partial(
        promo_update: PromoUpdatePartial,
        promo: Promo = Depends(promo_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await promo_crud.update_promo(
        session=session,
        promo=promo,
        promo_update=promo_update,
        partial=True
    )


@router.delete("/{promo_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_promo(
        promo: Promo = Depends(promo_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),

) -> None:
    await promo_crud.delete_promo(session=session, promo=promo)
