from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CatalogBase(BaseModel):
    name: str
    description: Optional[str]
    image: Optional[str]

    class Config:
        orm_mode = True

class CreateCatalog(CatalogBase):
    pass

class UpdateCatalog(CatalogBase):
    name: Optional[str]

class Catalog(CatalogBase):
    id: int
    updated: datetime
    created: datetime