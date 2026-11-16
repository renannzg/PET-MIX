# Matriz de Divisão de Responsabilidades e Contribuição dos Integrantes

**Projeto:** Pet Mix - Assistente Inteligente para Pequenos Pet Shops  
**Disciplina:** Projeto Integrador IV — FAESA Vitória / 2026  
**Integrantes:**
* **Matheus Rhamet** (Matrícula / Perfil GitHub)
* **Renan Miguel** (Matrícula / Perfil GitHub)

---

## 1. Distribuição de Tarefas no Projeto (C1, C2 e C3)

Para garantir uma colaboração equilibrada, a arquitetura e a entrega final do Pet Mix foram divididas em dois eixos complementares de engenharia:

| Módulo / Atividade | Responsável Principal | Co-Responsável / Revisão | Entregáveis Produzidos |
|:---|:---:|:---:|:---|
| **Arquitetura do Backend & API** | **Matheus Rhamet** | Renan Miguel | Criação dos endpoints FastAPI (`main.py`), validações com Pydantic e Health Check. |
| **Integração com LLM & Function Calling** | **Matheus Rhamet** | Renan Miguel | Agente de IA com Groq Cloud (`ai_agent.py`), loop de ferramentas e prompt anti-alucinação. |
| **Harness de Avaliação da IA (Eval)** | **Matheus Rhamet** | Renan Miguel | Criação do motor de avaliação (`eval_engine.py`), dataset de testes e script `run_eval.py`. |
| **Modelagem e Banco de Dados SQLite** | **Renan Miguel** | Matheus Rhamet | Schema relacional (`init_db.py`), catálogo de produtos, serviços, horários e base de políticas. |
| **Interface Frontend & Usabilidade (UI/UX)** | **Renan Miguel** | Matheus Rhamet | Desenvolvimento do layout moderno (`index.html`, `style.css`), Markdown dinâmico e chips rápidos. |
| **Testes Automatizados de Software** | **Renan Miguel** | Matheus Rhamet | Suíte de testes unitários e de integração com Pytest (`test_api.py` e `test_eval.py`). |
| **Infraestrutura de Deploy & Docker** | **Renan Miguel** | Matheus Rhamet | Criação do `Procfile`, `render.yaml`, `Dockerfile` e publicação em nuvem no Render. |
| **Documentação & Governança (LGPD/Ética)** | **Matheus Rhamet** | Renan Miguel | Elaboração dos relatórios técnicos, análise de impacto na comunidade e registro de prompts. |

---

## 2. Instruções para Versionamento Balanceado no Git (GitHub)

Para que o histórico de commits do repositório demonstre formalmente a participação de ambos os integrantes, utilize os seguintes passos no terminal antes de realizar os commits:

### Para commits realizados por Matheus Rhamet:
```bash
git config user.name "Matheus Rhamet"
git config user.email "gamessa1000@gmail.com"
git add backend/ eval/ docs/
git commit -m "feat(ia-eval): implementa harness de avaliacao quantitativa e grounding"
```

### Para commits realizados por Renan Miguel:
```bash
git config user.name "Renan Miguel"
git config user.email "miguelrenan618@gmail.com" 
git add frontend/ database/ tests/ Procfile render.yaml Dockerfile
git commit -m "feat(frontend-deploy): moderniza interface web e configura deploy no Render"
```

### Para commits conjuntos (Co-authored-by):
Caso um integrante finalize o trabalho em conjunto, pode-se usar a tag oficial do GitHub no rodapé da mensagem de commit:
```bash
git commit -m "feat: entrega C3 - MVP consolidado com testes e documentacao

Co-authored-by: Renan Miguel <renan.miguel@exemplo.com>
Co-authored-by: Matheus Rhamet <matheus.rhamet@exemplo.com>"
```
Assim, a aba *Insights / Contributors* do GitHub computará as contribuições para ambos os estudantes!
