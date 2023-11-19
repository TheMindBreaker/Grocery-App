import csv
from sqlalchemy.orm import Session
from grocery.repository.models import Item

def load_data_from_csv(db: Session, csv_file: str):
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = Item(
                sku=row['SKU'],
                name=row['Name'],
                description=row['Description'],
                price=float(row['Price'])
            )
            db.add(item)
        db.commit()
