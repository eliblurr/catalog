from .models import Category, CategoryProduct
from sqlalchemy.orm import Session
from utils import CRUD
from typing import List

category = CRUD(Category)

async def add_products(id:int, payload:List[int], db:Session):
    try:
        data = [
            CategoryProduct(
                **{
                    'category_id':id,
                    'product_id':product_id
                }
            ) 
        for product_id in payload]

        db.add_all(data)
        db.commit()

        return 'successfully added'
    except Exception as e:
        print(e)

async def remove_products(id:int, payload:List[int], db:Session):
    try:
        records =  db.query(CategoryProduct).filter(
            CategoryProduct.category_id==id,
            CategoryProduct.product_id.in_(payload)
        ).delete()
        db.commit()
        return 'success', f'{records} row(s) deleted'
    except Exception as e:
        print(e)