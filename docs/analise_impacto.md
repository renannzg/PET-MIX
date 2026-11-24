# Análise de Impacto na Comunidade e Extensão Universitária

**Projeto:** Pet Mix - Assistente Inteligente para Pequenos Pet Shops  
**Disciplina:** Projeto Integrador IV (DCEM) — FAESA Vitória / 2026  
**Autores:** Matheus Rhamet & Renan Miguel  
**Professor Orientador:** Prof. M.Sc. Howard Cruz Roatti  

---

## 1. Caracterização da Comunidade Impactada

Segundo dados do levantamento do **Sebrae** com base em informações da Receita Federal, as **micro e pequenas empresas representam cerca de 98% de todo o setor pet brasileiro**, totalizando mais de **111.922 microempreendedores individuais (MEIs)** registrados. Estabelecimentos de menor porte (pequenos e médios pet shops de bairro) respondem por quase metade (49%) de todo o faturamento da cadeia.

Apesar de sua relevância socioeconômica, os pequenos pet shops enfrentam gargalos operacionais diários:
* **Sobrecarga no Atendimento Humano:** Funcionários e atendentes precisam responder repetidamente às mesmas dúvidas (preços de banho por porte, horários de sábado, rações disponíveis, políticas de frete).
* **Ausência de Ferramentas Acessíveis:** Sistemas de automação de grandes redes (Petz, Cobasi) são inacessíveis para o orçamento de um pet shop de bairro.
* **Risco de IAs Genéricas:** Chatbots convencionais sem ancoragem (grounding) costumam alucinar produtos, inventar preços e prometer serviços que a loja não possui, gerando frustração nos clientes e passivo comercial.

---

## 2. Beneficiários do Projeto

* **Beneficiários Diretos:**
  * Microempreendedores e proprietários de pet shops de bairro;
  * Funcionários e recepcionistas dos estabelecimentos, liberados de tarefas repetitivas para focar no atendimento presencial e cuidado direto aos animais.
* **Beneficiários Indiretos:**
  * Tutores de cães e gatos, que recebem respostas imediatas, precisas e transparentes 24 horas por dia;
  * Os próprios animais de estimação, que se beneficiam da personalização (banho e ração indicados para seu porte específico) e da exigência sanitária de vacinação.

---

## 3. Indicadores de Impacto: Metas do Projeto vs. Resultados Alcançados

Os indicadores definidos na fase de concepção (C1/C2) foram formalmente avaliados na entrega final C3 por meio do harness de avaliação automatizada (`eval/run_eval.py`):

| Indicador | Forma de Medição | Meta Estipulada | Resultado Alcançado | Impacto Prático na Comunidade |
|:---|:---|:---:|:---:|:---|
| **Taxa de respostas corretas** | Comparação da resposta com o catálogo real | >= 85% | **100.0%** | Elimina erros de precificação e divergência de informações. |
| **Relevância das respostas** | Avaliação semântica da resposta | >= 85% | **100.0%** | Garante respostas diretas, sem prolixidade desnecessária. |
| **Taxa de alucinação** | Respostas contendo itens/preços inexistentes | <= 5% | **0.0%** | Zero risco de prometer serviços não ofertados (ex.: 'banho de ouro'). |
| **Tempo médio de resposta** | Duração entre envio e exibição | <= 5.0s | **~1.8s (Média Local)** | Atendimento instantâneo ao tutor sem filas de espera. |
| **Execução de ferramentas** | Acionamento correto do Function Calling | >= 90% | **100.0%** | Confiabilidade na consulta em tempo real ao SQLite e políticas. |
| **Robustez adversarial** | Resistência a injeção de prompt / jailbreaks | >= 90% | **100.0%** | Protege o estabelecimento contra tentativas de zerar preços. |

---

## 4. Retorno Social e Extensionista

O Pet Mix comprova a viabilidade da Inteligência Artificial Generativa como ferramenta de **democratização tecnológica para pequenos negócios**. Utilizando modelos abertos e APIs gratuitas de alta performance (Groq Cloud), o custo de infraestrutura de IA para o comerciante é **R$ 0,00**, viabilizando sua adoção sem onerar o caixa do negócio local.
