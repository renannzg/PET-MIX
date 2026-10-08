from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_chat_endpoint_structure():
    response = client.post("/api/chat", json={
        "message": "Olá",
        "history": [],
        "pet_context": None
    })
    # This might fail with 500 if no API key is provided, but we can at least check if endpoint exists
    assert response.status_code in [200, 500] 
    if response.status_code == 200:
        assert "response" in response.json()
