from sqlalchemy import Column, String, Float, Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine
from datetime import datetime

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created = Column(DateTime, default=datetime.utcnow)
    expiry = Column(DateTime, nullable=True)
    man_date = Column(DateTime, nullable=True)
    catalog_id = Column(Integer, ForeignKey("catalogs.id"), nullable=True)
    catalog = relationship("Catalog", back_populates="products")

    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    supplier = relationship("Supplier", back_populates="products")
    