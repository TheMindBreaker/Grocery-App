import uvicorn
from fastapi import FastAPI

from grocery.utils.database import engine, SessionLocal
from config import PORT
from grocery.repository.models import Base, Item
from grocery.handler import items_api, items_html
from grocery.utils.load_data import load_data_from_csv


Base.metadata.create_all(bind=engine)

def initialize_database():
    db = SessionLocal()
    try:
        if db.query(Item).count() == 0:
            load_data_from_csv(db, 'src/grocery/utils/sample_grocery.csv')
    finally:
        db.close()

initialize_database()


app = FastAPI()

app.include_router(items_api.router)
app.include_router(items_html.router)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=PORT, reload=True)
