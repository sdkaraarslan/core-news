from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_keyword():
    response = client.get("/get-keyword/?date=2024-01-01")
    assert response.status_code == 200
    assert "keyword" in response.json()
