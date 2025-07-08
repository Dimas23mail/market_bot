"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import PromoAction

from .promo_schemas import PromoCreate, PromoUpdate, PromoUpdatePartial


async def get_promos(session: AsyncSession) -> list[PromoAction]:
    stmt = select(PromoAction).order_by(PromoAction.id)
    result: Result = await session.execute(stmt)
    promos = result.scalars().all()
    return list(promos)


async def get_promo(session: AsyncSession, promo_id: int) -> PromoAction | None:
    return await session.get(PromoAction, promo_id)


async def create_promo(session: AsyncSession, promo_in: PromoCreate) -> PromoAction:
    promo = PromoAction(**promo_in.model_dump())
    session.add(promo)
    await session.commit()
    await session.refresh(promo)
    return promo


async def update_promo(
        session: AsyncSession,
        promo: PromoAction,
        promo_update: PromoUpdate | PromoUpdatePartial,
        partial: bool = False
) -> PromoAction:
    for key, value in promo_update.model_dump(exclude_unset=partial).items():
        setattr(promo, key, value)
    await session.commit()
    return promo


async def delete_promo(
        session: AsyncSession,
        promo: PromoAction) -> None:
    await session.delete(promo)
    await session.commit()
