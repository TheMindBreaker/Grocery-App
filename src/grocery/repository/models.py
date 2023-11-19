from sqlalchemy import Column, Integer, String, Float
from grocery.utils.database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)