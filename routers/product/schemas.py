from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: Optional[float]
    expiry: Optional[datetime]
    man_date: Optional[datetime]
    catalog_id: Optional[int]
    supplier_id: Optional[int]

    class Config:
        orm_mode = True

class CreateProduct(ProductBase):
    pass

class UpdateProduct(ProductBase):
    name: Optional[str]

class Product(ProductBase):
    id: int
    updated: datetime
    created: datetime