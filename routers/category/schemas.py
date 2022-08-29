from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True

class CreateCategory(CategoryBase):
    pass

class UpdateCategory(CategoryBase):
    name: Optional[str]

class Category(CategoryBase):
    id: int
    updated: datetime
    created: datetime

