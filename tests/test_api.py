import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.grocery.utils.database import Base, engine, SessionLocal

client = TestClient(app)

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_read_items():
    response = client.get("/item/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_item():
    test_sku = "F345"
    response = client.get(f"/item/{test_sku}")
    assert response.status_code == 200

def test_create_item():
    item_data = {"sku": "test", "name": "Test Item", "description": "Test Description", "price": 10.0}
    response = client.post("/item/", json=item_data)
    print(response)
    assert response.status_code == 201

def test_delete_item():
    test_sku = "F345"
    response = client.delete(f"/item/{test_sku}")
    assert response.status_code == 200

def test_get_item_converted():
    test_sku = "O456"
    currency = "EUR"
    response = client.get(f"/item/{test_sku}/convert?currency={currency}")
    assert response.status_code == 200
