from pydantic import BaseModel

class ItemSchema(BaseModel):
    sku: str
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True

class ExchangeSchema(BaseModel):
    sku: str
    name: str
    description: str
    price: float
    currency: str
