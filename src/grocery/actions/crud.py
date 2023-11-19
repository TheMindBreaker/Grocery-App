from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from grocery.repository.models import Item
from grocery.repository.schemas import ItemSchema

def get_items(db: Session):
    return db.query(Item).all()

def get_item(db: Session, sku: str):
    db_item = db.query(Item).filter(Item.sku == sku).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return db_item

def delete_item(db: Session, sku: str):
    db_item = db.query(Item).filter(Item.sku == sku).first()
    if db_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}

def create_item(db: Session, item: ItemSchema):
    print(item)
    existing_item = db.query(Item).filter(Item.sku == item.sku).first()
    if existing_item:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="SKU already in use")

    db_item = Item(sku=item.sku, name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: ItemSchema):
    print(item)
    item_db = db.query(Item).filter(Item.sku == item.sku).first()
    if not item:
        return None
    
    item_db.name = item.name
    item_db.description = item.description
    item_db.price = item.price
    db.commit()
    return item_db