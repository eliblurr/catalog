from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from .crud import supplier
from typing import List
from .schemas import *

router = APIRouter(prefix='/suppliers')

@router.post('/', response_model=Supplier, status_code=201)
async def create(payload:CreateSupplier, db:Session=Depends(get_db)):
    return await supplier.create(payload, db)

@router.get('/', response_model=List[Supplier])
async def read(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    return await supplier.read(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=Supplier)
async def read_by_id(id:int, db:Session=Depends(get_db)):
    return await supplier.read_by_id(id, db)

@router.patch('/{id}', response_model=Supplier, status_code=202)
async def update_by_id(id:int, payload:UpdateSupplier, db:Session=Depends(get_db)):
    return await supplier.update(id, payload, db)

@router.delete('/{id}', status_code=204)
async def delete_by_id(id:int, db:Session=Depends(get_db)):
    return await supplier.delete(id, db)