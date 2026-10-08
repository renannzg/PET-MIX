# Pet Mix - Assistente Inteligente para Pequenos Pet Shops

Este repositório contém o protótipo (Entrega C2) do projeto "Pet Mix", desenvolvido para a disciplina **Projeto Integrador IV**. 
A aplicação utiliza Inteligência Artificial (LLM via Groq API), RAG (recuperação do banco de dados SQLite) e Function Calling para fornecer respostas precisas aos clientes, baseadas nos dados reais do estabelecimento.

## Estrutura do Projeto

- `backend/`: Código da API FastAPI e lógica do Agente de IA.
- `database/`: Script de inicialização e arquivo SQLite do banco de dados local.
- `frontend/`: Interface HTML/CSS/JS (Chatbot) que consome a API do backend.
- `tests/`: Testes automatizados funcionais.
- `eval/`: Scripts de avaliação da Inteligência Artificial.

## Como Executar o Protótipo

### 1. Pré-requisitos
- Python 3.10+
- Chave de API do **Groq** (para usar o modelo LLM). Você pode obter uma gratuitamente em [console.groq.com](https://console.groq.com).

### 2. Configuração

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Inicialize o Banco de Dados (cria as tabelas e dados fictícios):
   ```bash
   python database/init_db.py
   ```

3. Configure a Chave de API:
   - Abra o arquivo `.env` na raiz do projeto e substitua o valor pela sua chave real:
     ```
     GROQ_API_KEY=sua_chave_groq_aqui
     ```

### 3. Rodando o Servidor

Inicie a aplicação com o FastAPI / Uvicorn:
```bash
python backend/main.py
```
Acesse o sistema pelo navegador em: **http://localhost:8000**

## Testes e Avaliação (Eval)

Para rodar os testes da aplicação e do banco de dados (garantindo grounding):
```bash
pytest tests/
pytest eval/
```

## Viabilidade Técnica (Checklist C2)
- [x] Backend e Frontend operacionais.
- [x] Banco de dados estruturado com os serviços e produtos.
- [x] Agente de IA integrado com LLM (via Groq API).
- [x] Function Calling implementado (busca no BD em tempo real).
- [x] Interface com suporte à personalização do contexto do Pet.
- [x] Estrutura de testes (`tests/` e `eval/`) pronta.
