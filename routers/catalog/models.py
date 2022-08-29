from sqlalchemy import Column, String, Float, Integer, Enum, DateTime
from sqlalchemy.orm import relationship
from database import Base, engine
from datetime import datetime

class Catalog(Base):
    __tablename__ = 'catalogs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    image = Column(String, nullable=True)
    updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created = Column(DateTime, default=datetime.utcnow)
    products = relationship("Product", back_populates="catalog")
    