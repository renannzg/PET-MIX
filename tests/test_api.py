"""
Testes automatizados da API Web (FastAPI) do Pet Mix.
Valida endpoints, tratamento de requisições, validação de payload e integração com o agente.
"""

import pytest
from fastapi.testclient import TestClient
import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.main import app

client = TestClient(app)

def test_health_check_endpoint():
    """Valida o endpoint de health check para monitoramento e deploy."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "Pet Mix API"
    assert "version" in data

def test_chat_endpoint_basic():
    """Valida envio e resposta de mensagem simples no chat."""
    response = client.post("/api/chat", json={
        "message": "Olá, tudo bem?",
        "history": [],
        "pet_context": None
    })
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert len(data["response"]) > 0
    assert "tools_used" in data

def test_chat_endpoint_with_pet_context():
    """Valida requisição ao chat contendo perfil de pet salvo."""
    response = client.post("/api/chat", json={
        "message": "Quais são os serviços de banho?",
        "history": [],
        "pet_context": {
            "nome": "Thor",
            "especie": "Cachorro",
            "porte": "Médio"
        }
    })
    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert len(data["response"]) > 0

def test_chat_endpoint_empty_message_validation():
    """Valida que mensagens vazias disparam erro 422 de validação."""
    response = client.post("/api/chat", json={
        "message": "",
        "history": [],
        "pet_context": None
    })
    assert response.status_code == 422

def test_frontend_index_served():
    """Valida se a rota raiz entrega a interface HTML do frontend."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    assert "Pet Mix" in response.text
