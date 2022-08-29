from sqlalchemy import Column, String, Float, Integer, Enum
from sqlalchemy.orm import relationship
from database import Base, engine

class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    location = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    products = relationship("Product", back_populates="supplier")
    