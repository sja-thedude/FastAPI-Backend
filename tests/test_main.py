from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_address():
    response = client.get("/address")
    assert response.status_code == 200
    data = response.json()
    assert "address" in data
    address = data["address"]
    assert address["street"] == "Main Street"
    assert address["city"] == "FastAPI City"
    assert address["postcode"] == "12345"