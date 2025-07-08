"""
create
read
update
delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.models import ProductType

from .product_type_schemas import ProductTypeCreate, ProductTypeUpdate, ProductTypeUpdatePartial


async def get_product_types(session: AsyncSession) -> list[ProductType]:
    stmt = select(ProductType).order_by(ProductType.id)
    result: Result = await session.execute(stmt)
    product_types = result.scalars().all()
    return list(product_types)


async def get_product_type(session: AsyncSession, product_type_id: int) -> ProductType | None:
    return await session.get(ProductType, product_type_id)


async def create_product_type(session: AsyncSession, product_type_in: ProductTypeCreate) -> ProductType:
    product_type = ProductType(**product_type_in.model_dump())
    session.add(product_type)
    await session.commit()
    await session.refresh(product_type)
    return product_type


async def update_product_type(
        session: AsyncSession,
        product_type: ProductType,
        product_type_update: ProductTypeUpdate | ProductTypeUpdatePartial,
        partial: bool = False
) -> ProductType:
    for key, value in product_type_update.model_dump(exclude_unset=partial).items():
        setattr(product_type, key, value)
    await session.commit()
    return product_type


async def delete_product_type(
        session: AsyncSession,
        product_type: ProductType) -> None:
    await session.delete(product_type)
    await session.commit()
