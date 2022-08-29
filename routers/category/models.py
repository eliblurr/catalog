from sqlalchemy import Column, String, Float, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine
from datetime import datetime

class CategoryProduct(Base):
    __tablename__ = 'category_products'

    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created = Column(DateTime, default=datetime.utcnow)
    products = relationship('Product', secondary=CategoryProduct.__table__)
    