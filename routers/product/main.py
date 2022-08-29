from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from .crud import product
from typing import List
from .schemas import *

router = APIRouter(prefix='/products')

@router.post('/', response_model=Product, status_code=201)
async def create(payload:CreateProduct, db:Session=Depends(get_db)):
    return await product.create(payload, db)

@router.get('/', response_model=List[Product])
async def read(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    return await product.read(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=Product)
async def read_by_id(id:int, db:Session=Depends(get_db)):
    return await product.read_by_id(id, db)

@router.patch('/{id}', response_model=Product, status_code=202)
async def update_by_id(id:int, payload:UpdateProduct, db:Session=Depends(get_db)):
    return await product.update(id, payload, db)

@router.delete('/{id}', status_code=204)
async def delete_by_id(id:int, db:Session=Depends(get_db)):
    return await product.delete(id, db)