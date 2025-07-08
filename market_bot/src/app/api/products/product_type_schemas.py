from pydantic import BaseModel, ConfigDict


class ProductTypeBase(BaseModel):
    title: str
    word: str
    imageURL: str


class ProductTypeCreate(ProductTypeBase):
    pass


class ProductType(ProductTypeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductTypeUpdate(ProductTypeCreate):
    pass


class ProductTypeUpdatePartial(ProductTypeCreate):
    title: str | None = None
    word: str | None = None
    imageURL: str | None = None
