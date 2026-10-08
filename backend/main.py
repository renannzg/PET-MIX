from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import sys
import uvicorn
from typing import Optional, List, Dict

# Adiciona o diretório raiz ao sys.path para evitar problemas de import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.ai_agent import chat_with_agent

app = FastAPI(title="Pet Mix API")

class ChatRequest(BaseModel):
    message: str
    history: List[Dict] = []
    pet_context: Optional[Dict] = None

class ChatResponse(BaseModel):
    response: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Constrói histórico de mensagens
        messages = request.history + [{"role": "user", "content": request.message}]
        
        # Chama agente de IA
        reply = chat_with_agent(messages, request.pet_context)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Montar os arquivos estáticos do frontend
frontend_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
