from pydantic import BaseModel
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    phone: Optional[str]
    location: Optional[str]
    gender: Optional[str]

    class Config:
        orm_mode = True

class CreateSupplier(SupplierBase):
    pass

class UpdateSupplier(SupplierBase):
    name: Optional[str]

class Supplier(SupplierBase):
    id: int