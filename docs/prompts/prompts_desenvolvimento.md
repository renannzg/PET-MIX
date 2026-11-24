# Registro de Prompts Utilizados no Desenvolvimento (Integridade Acadêmica)

Em estrita conformidade com a **Seção 11 do Edital de Trabalhos — Projeto Integrador IV (2026/2)**, este documento registra os prompts principais utilizados pelo grupo em assistentes de IA generativa para tarefas de engenharia de software, modelagem de dados e testes.

---

## 1. Concepção e Modelagem da Arquitetura (Fase C1 e C2)

* **Prompt 1.1 (Arquitetura e Escopo):**
  > *"Atue como arquiteto de software. Tenho um trabalho de faculdade sobre aplicação de IA para pequenos pet shops (Pet Mix). Preciso definir uma arquitetura com backend em Python (FastAPI), banco SQLite, frontend web simples e integração com LLM via API Groq usando Function Calling para buscar produtos, serviços, preços e horários, evitando respostas inventadas (grounding). Como estruturar as pastas e o fluxo do agente?"*
* **Resultado Obtido:** Estrutura inicial do repositório em camadas (`backend/`, `database/`, `frontend/`, `tests/`, `eval/`, `docs/`) e fluxo do loop de Function Calling.

* **Prompt 1.2 (Modelagem Relacional SQLite):**
  > *"Crie um script em Python usando sqlite3 para inicializar um banco de dados local com tabelas para produtos (nome, preco, estoque, categoria), servicos (nome, preco, descricao) e horarios (dia_semana, abertura, fechamento). Popule com dados fictícios de um pet shop de bairro."*
* **Resultado Obtido:** Criação do script `database/init_db.py`.

---

## 2. Implementação do Agente e Resolução de Erros de Dependência (Fase C2)

* **Prompt 2.1 (Ajuste de Conectividade com a Groq):**
  > *"O modelo `llama3-70b-8192` foi descontinuado na Groq gerando erro 400. Liste os modelos ativos e adapte o código do agente para usar um modelo open-weight gratuito que suporte chamadas de ferramentas (Function Calling) com limite seguro de tokens para não estourar a cota OTPM da Groq."*
* **Resultado Obtido:** Migração para `openai/gpt-oss-20b` com fallback para `qwen/qwen3.8-27b`, fixando o limite `max_tokens=500`.

* **Prompt 2.2 (Roteiro de Demonstração C2):**
  > *"Gere um roteiro narrado de 3 a 4 minutos para apresentar o protótipo C2 no YouTube, cobrindo o problema, a interface do chat, a consulta com function calling ao SQLite e os testes automatizados com pytest."*
* **Resultado Obtido:** Roteiro estruturado utilizado no vídeo da entrega C2.

---

## 3. Resolução do Feedback do Professor e Finalização do MVP (Fase C3)

* **Prompt 3.1 (Harness de Avaliação Real da IA):**
  > *"O professor deu o seguinte feedback na C2: 'os testes de eval da IA (injeção e alucinação) são apenas esqueletos (pass/comentados) e não avaliam de fato o LLM; o README descreve RAG com embeddings, mas é function-calling sobre SQLite'. Preciso que você construa um harness de eval real com dataset curado de 15 casos (factuais, anti-alucinação de produtos inexistentes, injeção adversarial de prompt, personalização de pet e políticas da loja), medindo taxa de acerto, alucinação, robustez e latência com asserts reais em pytest."*
* **Resultado Obtido:** Implementação de `eval/dataset.py`, `eval/eval_engine.py`, `eval/run_eval.py` e `eval/test_eval.py` com 100% de sucesso.

* **Prompt 3.2 (Correção Técnica do README e RAG):**
  > *"Explique com precisão acadêmica no README que o grounding do Pet Mix utiliza Function Calling determinístico sobre banco relacional SQLite para preços e estoques em vez de busca vetorial aproximada por embeddings densos, e adicione uma base de conhecimento de políticas institucionais (vacinas, formas de pagamento, entregas) consultada via RAG textual."*
* **Resultado Obtido:** Atualização do `README.md` eliminando divergências conceituais e fundamentando a escolha de engenharia.

* **Prompt 3.3 (Deploy em Nuvem Gratuita):**
  > *"Gere os arquivos necessários para deploy público no Render (free tier) com FastAPI: Procfile, render.yaml, Dockerfile e documente o passo a passo para colocar no ar."*
* **Resultado Obtido:** Arquivos de infraestrutura e guia de deploy.
