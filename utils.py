from sqlalchemy.orm import Session

class CRUD:
    def __init__(self, model):
        self.model = model

    async def create(self, payload, db:Session):
        try:
            obj = self.model(**payload.dict())
            db.add(obj)
            db.commit()
            db.refresh(obj)
        except Exception as e:
            print(e)

        return obj

    async def read(self, db:Session, skip:int=0, limit:int=100):
        return db.query(self.model).offset(skip).limit(limit).all()

    async def read_by_id(self, id:int, db:Session):
        return db.query(self.model).filter(self.model.id==id).first()
    
    async def update(self, id:int, payload, db:Session):
        try:
            db.query(self.model).filter(self.model.id==id).update(payload.dict(exclude_unset=True))
            db.commit()
            return await self.read_by_id(id, db)
        except Exception as e:
            print(e)

    async def delete(self, id:int, db:Session):
        try:
            records = db.query(self.model).filter(self.model.id==id).delete()
            db.commit()
            return 'success', f'{records} row(s) deleted'
        except Exception as e:
            print(e)

