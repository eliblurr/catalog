from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from .crud import category, add_products, remove_products
from typing import List
from .schemas import *

router = APIRouter(prefix='/categories')

@router.post('/', response_model=Category, status_code=201)
async def create(payload:CreateCategory, db:Session=Depends(get_db)):
    return await category.create(payload, db)

@router.get('/', response_model=List[Category])
async def read(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    return await category.read(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=Category)
async def read_by_id(id:int, db:Session=Depends(get_db)):
    return await category.read_by_id(id, db)

@router.patch('/{id}', response_model=Category, status_code=202)
async def update_by_id(id:int, payload:UpdateCategory, db:Session=Depends(get_db)):
    return await category.update(id, payload, db)

@router.delete('/{id}', status_code=204)
async def delete_by_id(id:int, db:Session=Depends(get_db)):
    return await category.delete(id, db)

@router.put('/{id}/add-products')
async def _add_products(id: int, payload: List[int], db:Session=Depends(get_db)):
    return await add_products(id, payload, db)

@router.put('/{id}/remove-products')
async def _remove_products(id: int, payload: List[int], db:Session=Depends(get_db)):
    return await remove_products(id, payload, db)