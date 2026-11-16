from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import os
import sys
import uvicorn
from typing import Optional, List, Dict

# Adiciona o diretório raiz ao sys.path para importação consistente
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.ai_agent import chat_with_agent, MODEL_NAME

app = FastAPI(
    title="Pet Mix API",
    description="Assistente Inteligente para Pequenos Pet Shops com Grounding e Function Calling",
    version="2.0.0"
)

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Mensagem enviada pelo cliente")
    history: List[Dict] = []
    pet_context: Optional[Dict] = None

class ChatResponse(BaseModel):
    response: str
    tools_used: List[str] = []

@app.get("/api/health")
async def health_check():
    """Endpoint de verificação de integridade (Health Check) para deploy na nuvem."""
    return {
        "status": "healthy",
        "service": "Pet Mix API",
        "model": MODEL_NAME,
        "version": "2.0.0"
    }

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Endpoint principal de conversação com o agente de IA."""
    try:
        # Mantém no máximo as últimas 6 mensagens do histórico para otimização de tokens (Groq free tier)
        history_trimmed = request.history[-6:] if len(request.history) > 6 else request.history
        messages = history_trimmed + [{"role": "user", "content": request.message}]
        
        # Processa mensagem com o agente retornando o texto e as ferramentas executadas
        reply, tools = chat_with_agent(messages, request.pet_context, return_tool_calls=True)
        return {"response": reply, "tools_used": tools}
    except Exception as e:
        print(f"[ERRO NO ENDPOINT /api/chat]: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

# Servir arquivos estáticos do frontend
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
