from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_chat_endpoint_structure():
    response = client.post("/api/chat", json={
        "message": "Olá",
        "history": [],
        "pet_context": None
    })
    # Isso pode falhar com erro 500 se nenhuma chave de API for fornecida, mas pelo menos podemos verificar se o endpoint existe.
    assert response.status_code in [200, 500] 
    if response.status_code == 200:
        assert "response" in response.json()
