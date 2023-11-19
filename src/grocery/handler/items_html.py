from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional
from sqlalchemy.orm import Session

from grocery.utils.database import get_db
from grocery.actions import crud
from grocery.repository.schemas import ItemSchema

router = APIRouter()
templates = Jinja2Templates(directory="src/grocery/templates")

@router.get("/", response_class=HTMLResponse)
def read_items(request: Request, db: Session = Depends(get_db), delete: Optional[str] = None, edit: Optional[str] = None, add: Optional[str] = None):
    message = ""
    if add:
        message = f"Item added"
    if delete:
        message = f"Item deleted"
    if edit:
        message = f"Item modified"
    items = crud.get_items(db)
    print(edit)

    return templates.TemplateResponse("home.html", {"request": request,"items": items, "message":message})

@router.get("/add", response_class=HTMLResponse)
async def add_item_form(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@router.get("/edit/{sku}", response_class=HTMLResponse)
def edit_item_form(request: Request, sku: str, db: Session = Depends(get_db)):
    item = crud.get_item(db, sku)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return templates.TemplateResponse("edit.html", {"request": request, "item": item})

@router.get("/delete/{sku}", response_class=HTMLResponse)
def delete_item_form(request: Request, sku: str, db: Session = Depends(get_db)):
    item = crud.get_item(db, sku)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return templates.TemplateResponse("delete.html", {"request": request, "item": item})

@router.post("/add", response_class=HTMLResponse)
async def create_item(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    item_data = ItemSchema(
            sku=form_data.get("sku"),
            name=form_data.get("name"),
            description=form_data.get("description"),
            price=float(form_data.get("price"))
        )
    crud.create_item(db=db, item=item_data)
    return RedirectResponse("/?add=True",status_code=303)

@router.post("/edit", response_class=HTMLResponse)
async def update_item(request: Request, db: Session = Depends(get_db)):
    form_data = await request.form()
    item_data = ItemSchema(
            sku=form_data.get("sku"),
            name=form_data.get("name"),
            description=form_data.get("description"),
            price=float(form_data.get("price"))
        )
    crud.update_item(db=db, item=item_data)
    return RedirectResponse("/?edit=True",status_code=303)

@router.post("/delete/{sku}", response_class=HTMLResponse)
async def delete_item(request: Request, sku: str, db: Session = Depends(get_db)):
    crud.delete_item(db, sku)
    return RedirectResponse("/?delete=True",status_code=303)
