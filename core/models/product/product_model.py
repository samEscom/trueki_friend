from core.models import Base
from sqlalchemy import Column, Integer, String, DateTime, Float


class ProductModel(Base):
    __tablename__ = "PRODUCT"

    product_id = Column(Integer, primary_key=True)
    category = Column(Integer)
    subcategory = Column(Integer)
    price = Column(Float)
    detail = Column(String(300))
    is_active = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


