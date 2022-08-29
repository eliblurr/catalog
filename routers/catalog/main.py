from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from .crud import catalog
from typing import List
from .schemas import *

router = APIRouter(prefix='/catalogs')

@router.post('/', response_model=Catalog, status_code=201)
async def create(payload:CreateCatalog, db:Session=Depends(get_db)):
    return await catalog.create(payload, db)

@router.get('/', response_model=List[Catalog])
async def read(skip:int=0, limit:int=100, db:Session=Depends(get_db)):
    return await catalog.read(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=Catalog)
async def read_by_id(id:int, db:Session=Depends(get_db)):
    return await catalog.read_by_id(id, db)

@router.patch('/{id}', response_model=Catalog, status_code=202)
async def update_by_id(id:int, payload:UpdateCatalog, db:Session=Depends(get_db)):
    return await catalog.update(id, payload, db)

@router.delete('/{id}', status_code=204)
async def delete_by_id(id:int, db:Session=Depends(get_db)):
    return await catalog.delete(id, db)