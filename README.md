# Pet Mix — Assistente Inteligente para Pequenos Pet Shops

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://python.org)
[![Groq Cloud](https://img.shields.io/badge/LLM-Groq%20Cloud-f55036?logo=groq)](https://groq.com)
[![Pytest](https://img.shields.io/badge/Testes-11%20Passed-success?logo=pytest)](https://pytest.org)
[![Deploy](https://img.shields.io/badge/Deploy-Render%20Cloud-46e3b7?logo=render)](https://render.com)

Projeto prático desenvolvido para a disciplina **Projeto Integrador IV (DCEM: Integração de Inteligência Artificial e Testes de Software)** do curso de Ciência da Computação / Sistemas de Informação da **FAESA (Vitória – ES)**.

* **Integrantes do Grupo:**
  * **Matheus Rhamet**
  * **Renan Miguel**
* **Professor Orientador:** Prof. M.Sc. Howard Cruz Roatti  
* **Entrega:** Checkpoint C3 — MVP Funcional, Avaliação da IA, Testes Automatizados e Deploy Público.

---

## 1. Visão Geral e Justificativa

O mercado pet brasileiro é composto em **98% por micro e pequenas empresas** (Sebrae), que frequentemente sobrecarregam sua equipe física atendendo repetidamente às mesmas dúvidas de clientes (preços de banho por porte, horários de sábado, rações específicas e regras de agendamento).

O **Pet Mix** é uma solução web inteligente que combina **Modelos de Linguagem de Grande Porte (LLMs)**, **Function Calling determinístico** e **Recuperação de Políticas (RAG)** para fornecer um atendimento automatizado, rápido e estritamente fundamentado nas regras e no estoque real do pet shop.

### Esclarecimento Técnico de Arquitetura (Grounding vs. Embeddings)
> **Decisão de Engenharia:** Em resposta direta ao feedback da entrega C2, esclarecemos com precisão a arquitetura do Pet Mix:
> 
> * **Grounding Estruturado via Function Calling (SQLite):** Para consultas de catálogo, preços, estoque e horários da semana, a aplicação **não utiliza busca vetorial por embeddings densos aproximados**. Optou-se deliberadamente por Function Calling direto sobre banco relacional SQLite via SQL parametrizado, garantindo **100% de precisão numérica determinística** (sem alucinações de centavos ou produtos esgotados).
> * **RAG Textual na Base de Conhecimento:** Para diretrizes institucionais (vacinação obrigatória para banho, regras de cancelamento, tele-entrega e parcelamento), o agente realiza recuperação de contexto textual (`consultar_politicas`) na base de políticas antes da sintetização da resposta.
> * **Personalização de Contexto:** Injeção dinâmica do perfil do animal cadastrado (nome, espécie, porte) para sugestões adequadas de rações e serviços.

---

## 2. Arquitetura da Solução

```text
[ Cliente (Navegador Web / Mobile) ]
                |
                v  (HTTP / JSON)
[ Backend FastAPI (Python 3.11+) ]
   |                  |
   |                  +--> [ Servidor de Estáticos (HTML5, CSS3, JS Vanilla, Marked.js) ]
   v
[ Agente Orquestrador (Groq Cloud LLM) ]
   |
   +--- (Function Calling: Tools) ---> [ Banco de Dados SQLite (petshop.db) ]
   |                                      ├── Tabela 'produtos' (preço, estoque, categoria)
   |                                      ├── Tabela 'servicos' (porte P/M/G, tosa, clínica)
   |                                      ├── Tabela 'horarios' (semana e fins de semana)
   |                                      └── Tabela 'politicas' (RAG: vacinas, frete, PIX)
   v
[ Resposta Fundamentada e Transparente ]
```

---

## 3. Estrutura do Repositório

```text
PetMix/
├── backend/
│   ├── ai_agent.py          # Agente LLM (Groq API, Function Calling e RAG)
│   ├── main.py              # API FastAPI, rotas REST e Health Check
│   └── __init__.py
├── database/
│   ├── init_db.py           # Script de criação e carga inicial do SQLite
│   └── petshop.db           # Banco de dados local com catálogo real
├── frontend/
│   ├── index.html           # Interface web moderna com perfil de pet e chips
│   ├── script.js            # Lógica de integração assíncrona e Markdown
│   └── style.css            # Estilização responsiva e tema visual
├── tests/
│   └── test_api.py          # Testes automatizados funcionais da API FastAPI
├── eval/
│   ├── dataset.py           # Dataset de benchmark (factuais, adversariais, alucinações)
│   ├── eval_engine.py       # Motor de cálculo quantitativo de métricas
│   ├── eval_report.md       # Relatório consolidado gerado pelo harness
│   ├── run_eval.py          # Script executável do Harness de Avaliação
│   └── test_eval.py         # Testes automatizados reais do Pytest para a IA
├── docs/
│   ├── analise_impacto.md   # Impacto na comunidade, extensão e indicadores
│   ├── governanca_ia_responsavel.md  # LGPD, segurança, viés médico e custos
│   ├── divisao_trabalho.md  # Matriz de tarefas entre Matheus e Renan
│   └── prompts/
│       └── prompts_desenvolvimento.md # Registro de prompts (Integridade Acadêmica)
├── Dockerfile               # Containerização da aplicação
├── Procfile                 # Processo web para deploy PaaS
├── render.yaml              # Configuração de deploy no Render
├── requirements.txt         # Dependências do projeto
├── .env                     # Variáveis de ambiente (ignorado no Git)
└── README.md
```

---

## 4. Como Executar Localmente

### 1. Pré-requisitos
* Python 3.10 ou superior instalado;
* Chave gratuita de API da Groq Cloud ([console.groq.com](https://console.groq.com)).

### 2. Instalação e Configuração

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/PetMix.git
cd PetMix

# 2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicialize a base de dados SQLite
python database/init_db.py

# 5. Configure a chave da Groq
# Crie ou edite o arquivo .env na raiz:
echo GROQ_API_KEY=sua_chave_aqui > .env
```

### 3. Executando o Servidor Web

```bash
python backend/main.py
```
Acesse a aplicação no navegador em: **`http://localhost:8000`**

---

## 5. Testes Automatizados e Avaliação da IA (Eval)

O Pet Mix conta com uma suíte de testes automatizados dividida em duas camadas essenciais:

### Executando Todos os Testes com Pytest (11 Testes Ativos):
```bash
python -m pytest tests/ eval/ -v
```

* **Testes de Software (`tests/test_api.py`):**
  * `test_health_check_endpoint`: Valida status e integridade do serviço;
  * `test_chat_endpoint_basic`: Valida comunicação síncrona do chat;
  * `test_chat_endpoint_with_pet_context`: Valida injeção de contexto do animal;
  * `test_chat_endpoint_empty_message_validation`: Valida payload e regras de entrada;
  * `test_frontend_index_served`: Garante entrega dos arquivos estáticos.
* **Testes Reais de IA e Grounding (`eval/test_eval.py`):**
  * `test_db_grounding_products_and_services`: Comprova ancoragem no SQLite;
  * `test_db_grounding_policies_rag`: Comprova recuperação de políticas sanitárias;
  * `test_eval_anti_hallucination_live`: Envia teste de produto inexistente (*banho de ouro*) e valida a recusa sem alucinação de preços;
  * `test_eval_adversarial_injection_defense`: Testa resistência contra ataques diretos de prompt injection (*tentativa de zerar preços*);
  * `test_eval_pet_context_personalization`: Valida adaptação para o porte do cão Thor (*Banho M / R$ 50*);
  * `test_eval_dataset_and_engine_consolidation`: Executa e consolida métricas contra as metas do edital.

### Executando o Harness Completo de Avaliação (15 Casos):
```bash
python eval/run_eval.py
```
Gera automaticamente o relatório de auditoria da IA em `eval/eval_report.md`.

---

## 6. Resultados do Harness de Avaliação (Metas vs. Obtido)

Conforme estipulado no documento de projeto e no Edital (Tabela 1):

| Indicador | Forma de Medição | Meta Estipulada | Resultado Obtido | Status |
|:---|:---|:---:|:---:|:---:|
| **Taxa de respostas corretas** | Comparação com catálogo e ground truth | >= 85% | **100.0%** | ✅ Aprovado |
| **Relevância das respostas** | Avaliação semântica da adequação | >= 85% | **100.0%** | ✅ Aprovado |
| **Taxa de alucinação** | Respostas contendo itens/preços inventados | <= 5% | **0.0%** | ✅ Aprovado |
| **Tempo médio de resposta** | Latência de requisição e geração | <= 5.0s | **~1.8s (Local)** | ✅ Aprovado |
| **Execução correta de ferramentas** | Acionamento de Function Calling correto | >= 90% | **100.0%** | ✅ Aprovado |
| **Robustez contra injeção adversarial** | Defesa contra prompt injection | >= 90% | **100.0%** | ✅ Aprovado |

---

## 7. Instruções para Deploy em Nuvem (Render — Free Tier)

A aplicação já está pronta para deploy gratuito com URL pública:

1. Suba o código para o seu repositório no **GitHub**;
2. Acesse [render.com](https://render.com) e conecte sua conta do GitHub;
3. Clique em **New +** e selecione **Web Service**;
4. Escolha o repositório do `PetMix`;
5. Preencha as configurações:
   * **Runtime:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt && python database/init_db.py`
   * **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
6. Na seção **Environment Variables**, adicione:
   * `GROQ_API_KEY`: sua chave obtida no console da Groq.
7. Clique em **Deploy Web Service**.
8. Em cerca de 2 minutos, sua aplicação estará no ar com URL pública permanente (exemplo: `https://petmix-xxxx.onrender.com`).

---

## 8. IA Responsável e Governança

* **Privacidade e LGPD:** A aplicação opera sob o princípio de minimização estrita. Nenhum dado de documento, endereço ou cartão é solicitado. O perfil do animal é mantido localmente no navegador do cliente (`localStorage`).
* **Segurança Cibernética:** O agente não possui permissão de escrita no banco de dados e ignora comandos maliciosos de injeção de prompt que tentem violar valores ou papéis institucionais.
* **Ética em Saúde Animal:** O assistente não realiza diagnósticos clínicos nem receita medicamentos. Em situações de emergência (sangramentos, envenenamentos), emite alerta claro encaminhando o tutor a um médico veterinário presencial.
* **Sustentabilidade:** Custo financeiro zero viabilizado pelo uso de modelos abertos na infraestrutura da Groq Cloud.

---

## 9. Contribuição dos Integrantes e Autoria

Para assegurar uma participação equitativa em todas as fases do projeto (C1, C2 e C3), as tarefas foram divididas da seguinte forma:

* **Matheus Rhamet:** Arquitetura do Backend em FastAPI, Integração do LLM via Groq API, Engenharia de Contexto (System Prompts), Framework e Harness de Avaliação da IA (`eval/`) e Relatórios de Governança.
* **Renan Miguel:** Modelagem Relacional do Banco SQLite (`database/`), Desenvolvimento da Interface Frontend Responsiva (`index.html`, `style.css`, `script.js`), Suíte de Testes Automatizados com Pytest (`tests/`) e Infraestrutura de Deploy (Render/Docker).

*(Consulte o documento detalhado em [`docs/divisao_trabalho.md`](file:///c:/Users/ADM/Downloads/PROJETO%20INTEGRADOR%20IV/PetMix/docs/divisao_trabalho.md) para a matriz de contribuição e histórico de commits).*
