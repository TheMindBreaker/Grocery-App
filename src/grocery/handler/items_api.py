from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session



from grocery.actions import crud
from grocery.repository.schemas import ItemSchema, ExchangeSchema
from grocery.repository.exchange import convert_currency
from grocery.utils.database import get_db

router = APIRouter()

@router.get("/item/", response_model=list[ItemSchema])
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@router.get("/item/{sku}", response_model=ItemSchema)
def read_item(sku: str,db: Session = Depends(get_db)):
    return crud.get_item(db, sku)

@router.post("/item/", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.put("/item/", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item=item)


@router.delete("/item/{sku}")
def delete_item(sku: str, db: Session = Depends(get_db)):
    return crud.delete_item(db, sku)

@router.get("/item/{sku}/convert", response_model=ExchangeSchema)
def get_item_converted(sku: str, currency: str = Query("MXN"), db: Session = Depends(get_db)):
    item = crud.get_item(db, sku)
    converted_price = convert_currency(item.price, "USD", currency)
    item.price = converted_price
    item.currency = currency 
    return item