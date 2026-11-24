# Governança, Ética e IA Responsável

**Projeto:** Pet Mix - Assistente Inteligente para Pequenos Pet Shops  
**Disciplina:** Projeto Integrador IV — FAESA Vitória / 2026  
**Autores:** Matheus Rhamet & Renan Miguel  

---

A concepção do Pet Mix foi orientada pelos quatro pilares obrigatórios de Inteligência Artificial Responsável estabelecidos no edital: **Privacidade/LGPD**, **Segurança Cibernética**, **Ética e Viés** e **Sustentabilidade de Custos**.

---

## 1. Privacidade e LGPD (Lei Geral de Proteção de Dados)

* **Minimização de Dados (Privacy by Design):** A aplicação não coleta CPF, endereço, dados de cartão de crédito, telefone ou e-mail do usuário.
* **Dados do Pet:** Os únicos dados opcionais solicitados são o nome, espécie e porte do animal. Esses dados são armazenados localmente no navegador do tutor (`localStorage`) e transitam para o backend apenas no payload transitório da sessão ativa.
* **Anonimização:** Nenhuma informação pessoal identificável (PII) é persistida no banco de dados SQLite ou enviada a terceiros.
* **Base Legal:** Legítimo interesse do titular para atendimento e simulação de serviços, em estrita conformidade com o Art. 7º da Lei nº 13.709/2018 (LGPD).

---

## 2. Segurança Cibernética e Mitigação de Prompt Injection

Os Large Language Models são vulneráveis a ataques de injeção de prompt e jailbreaks nos quais usuários mal-intencionados tentam contornar diretrizes de segurança.

* **Riscos Identificados:**
  1. Tentativa de forçar o modelo a conceder banhos ou rações de graça ("Tudo hoje é grátis");
  2. Tentativa de induzir a personificação do dono do estabelecimento ("System Override: o dono autorizou");
  3. Tentativa de induzir alucinações sobre produtos de luxo ou serviços proibidos.
* **Mecanismos de Mitigação Implementados:**
  * **System Prompt Blindado:** Instrução explícita de recusa a comandos adversariais e proibição de alteração de preços tabelados.
  * **Grounding Estruturado Inviolável:** A IA não possui acesso de escrita ao banco de dados; ela opera exclusivamente com funções de leitura (`SELECT`). Os preços exibidos dependem deterministicamente do retorno do SQLite, impedindo que o modelo "invente" um preço zero no banco.
  * **Validação por Eval Adversarial:** O harness de testes inclui casos reais de ataque (`ADV_01` e `ADV_02`), comprovando **100% de robustez** nos testes automatizados.

---

## 3. Ética e Limitações em Saúde Animal

* **Risco de Falso Aconselhamento Médico:** Um dos riscos mais severos em aplicações para pets é a prescrição indevida de remédios caseiros ou diagnósticos falsos por modelos de linguagem, o que pode levar o animal a óbito.
* **Diretriz de Segurança Médica:** O Pet Mix foi expressamente instruído a **nunca diagnosticar doenças ou receitar medicamentos**.
* **Conduta em Casos de Emergência:** Diante de perguntas sobre vômito, sangue, envenenamento ou sintomas clínicos (`ETICA_01`), o assistente emite um aviso claro orientando o tutor a conduzir o animal imediatamente a uma clínica veterinária presencial.

---

## 4. Sustentabilidade e Consciência de Custo

* **Custo Zero:** A aplicação utiliza o provedor **Groq Cloud** (plano Free Tier), que oferece acesso a LLMs open-weight (modelos abertos) com aceleração por LPUs sem cobrança financeira.
* **Otimização de Tokens:**
  * Redução do `max_tokens` para 500 por requisição (evita estouro do limite OTPM - *Output Tokens Per Minute*);
  * Poda inteligente do histórico da conversa (`history[-6:]`), evitando o envio de contextos infinitos e economizando tokens de entrada;
  * Seleção de modelo equilibrado (`openai/gpt-oss-20b` com fallback para `qwen/qwen3.8-27b`), garantindo latência inferior a 2 segundos e alta densidade de raciocínio com baixo consumo computacional.
