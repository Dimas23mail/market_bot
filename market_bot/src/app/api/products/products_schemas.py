from typing import List
from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    title: str
    price: int
    imageURL: str
    description: str
    availability: int
    allImagesURL: List[str]
    color: str
    room_id: int
    product_type_id: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    title: str | None = None
    price: int | None = None
    imageURL: str | None = None
    description: str | None = None
    availability: int | None = None
    allImagesURL: List[str] | None = None
    color: str | None = None
    room_id: int | None = None
    product_type_id: int | None = None
