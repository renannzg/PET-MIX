# PET MIX

## Assistente Inteligente para Pequenos Pet Shops

Projeto desenvolvido para a disciplina **Projeto Integrador IV**, do curso de **Ciência da Computação – FAESA**.

O **Pet Mix** é uma aplicação web que utiliza **Inteligência Artificial** para auxiliar pequenos pet shops no atendimento aos seus clientes, permitindo que dúvidas sobre produtos, serviços e informações do estabelecimento sejam respondidas de forma mais rápida e acessível.

---

## 📌 Sobre o Projeto

Pequenos pet shops podem enfrentar dificuldades para manter um atendimento rápido e consistente, principalmente quando há grande quantidade de dúvidas repetitivas sobre produtos, serviços, horários e informações do estabelecimento.

O Pet Mix propõe uma solução baseada em **Inteligência Artificial**, utilizando uma base de conhecimento cadastrada pelo próprio estabelecimento para fornecer respostas relacionadas ao seu contexto.

A aplicação será desenvolvida com foco em pequenos pet shops, buscando facilitar o atendimento aos clientes sem substituir a interação humana quando ela for necessária.

---

## 🎯 Objetivo

Desenvolver uma aplicação web com um assistente baseado em Inteligência Artificial capaz de auxiliar clientes de pequenos pet shops, respondendo perguntas relacionadas aos produtos, serviços e informações disponibilizadas pelo estabelecimento.

### Objetivos específicos

* Desenvolver uma interface web simples e acessível;
* Permitir o cadastro e gerenciamento de informações do pet shop;
* Permitir que clientes realizem perguntas utilizando linguagem natural;
* Utilizar um modelo de linguagem (LLM) para geração das respostas;
* Utilizar uma base de conhecimento específica do estabelecimento;
* Reduzir respostas incorretas ou informações inventadas pela IA;
* Implementar testes automatizados;
* Avaliar a qualidade, relevância e robustez das respostas da IA;
* Analisar indicadores relacionados ao impacto da solução.

---

## 🤖 Inteligência Artificial

O projeto utilizará um **Large Language Model (LLM)** acessado por meio de API, com possibilidade de utilização da plataforma **Groq**.

Também será avaliada a utilização de **RAG (Retrieval-Augmented Generation)** para permitir que o modelo utilize informações recuperadas da base de conhecimento do pet shop antes de gerar uma resposta.

Fluxo previsto:

```text
Cliente
   ↓
Interface Web
   ↓
Backend
   ↓
Busca na Base de Conhecimento
   ↓
Contexto Recuperado
   ↓
LLM
   ↓
Resposta
   ↓
Cliente
```

A aplicação deverá evitar a criação de informações que não estejam disponíveis na base de conhecimento. Quando não houver informações suficientes para responder a uma pergunta, o sistema deverá indicar essa limitação.

---

## 👥 Comunidade Impactada

### Beneficiários diretos

* Pequenos pet shops;
* Proprietários de pequenos pet shops;
* Funcionários responsáveis pelo atendimento.

### Beneficiários indiretos

* Clientes dos pet shops;
* Tutores de animais de estimação.

A solução busca facilitar o acesso às informações e auxiliar no atendimento de dúvidas relacionadas ao estabelecimento.

---

## 📊 Indicadores de Impacto

Durante o desenvolvimento e avaliação do projeto, poderão ser analisados indicadores como:

* Quantidade de perguntas realizadas;
* Taxa de respostas consideradas corretas;
* Relevância das respostas;
* Avaliação de utilidade pelos usuários;
* Tempo de resposta;
* Taxa de respostas inadequadas ou alucinações;
* Satisfação dos usuários.

---

## 🧪 Testes e Avaliação da IA

O projeto contará com testes automatizados para partes críticas da aplicação e uma estratégia específica para avaliação das respostas geradas pela Inteligência Artificial.

Serão considerados cenários como:

* Perguntas sobre produtos existentes;
* Perguntas sobre produtos inexistentes;
* Perguntas sobre serviços;
* Perguntas sobre informações do estabelecimento;
* Perguntas para as quais não existem informações na base;
* Perguntas formuladas de maneiras diferentes;
* Tentativas de induzir a IA a ignorar suas instruções.

A avaliação deverá considerar aspectos como **qualidade, relevância, robustez e ocorrência de respostas incorretas ou alucinações**.

---

## 🔐 IA Responsável

O desenvolvimento do Pet Mix considerará aspectos de Inteligência Artificial responsável, incluindo:

* Privacidade e proteção de dados;
* Conformidade com a LGPD;
* Segurança da aplicação;
* Prevenção contra tentativas de prompt injection;
* Possíveis vieses nas respostas;
* Controle de custos relacionados ao uso da API;
* Uso consciente de recursos computacionais.

Esses aspectos fazem parte dos requisitos previstos para o projeto.

---

## 🛠️ Tecnologias Previstas

| Tecnologia                     | Utilização                 |
| ------------------------------ | -------------------------- |
| HTML, CSS e JavaScript / React | Frontend                   |
| Python                         | Backend                    |
| FastAPI ou Flask               | API do sistema             |
| SQLite / PostgreSQL            | Banco de dados             |
| Groq / LLM                     | Inteligência Artificial    |
| RAG                            | Recuperação de informações |
| Pytest                         | Testes automatizados       |
| Git e GitHub                   | Versionamento              |
| Render / Railway               | Deploy                     |

As tecnologias poderão ser ajustadas durante o desenvolvimento de acordo com as necessidades do projeto.

---

## 📁 Estrutura Inicial

```text
PetMix/
│
├── README.md
├── .gitignore
│
├── docs/
│   └── relatorio-C1.pdf
│
├── backend/
│
├── frontend/
│
└── tests/
```

---

## 📅 Cronograma

| Etapa | Objetivo                                                                          | Data       |
| ----- | --------------------------------------------------------------------------------- | ---------- |
| C1    | Definição do problema, metodologia, comunidade, indicadores e organização inicial | 18/09/2026 |
| C2    | Protótipo funcional, IA funcionando e primeiros testes/avaliação                  | 30/10/2026 |
| C3    | MVP completo, documentação, testes, avaliação, deploy e análise de impacto        | 04/12/2026 |

As datas seguem o cronograma definido no edital do Projeto Integrador IV.

---

## 👨‍💻 Equipe

**Curso:** Ciência da Computação – FAESA
**Disciplina:** Projeto Integrador IV
**Professor:** Prof. M.Sc. Howard Cruz Roatti

### Integrantes

* Matheus Rhamet
* Renan Miguel

---

## 📄 Documentação

O relatório referente à **C1** está disponível na pasta:

```text
docs/relatorio-C1.pdf
```

---

## ⚠️ Observação

O projeto encontra-se em fase inicial de desenvolvimento. As funcionalidades, tecnologias e arquitetura apresentadas neste repositório poderão ser aprimoradas durante as próximas etapas do Projeto Integrador IV.

O uso de Inteligência Artificial durante o desenvolvimento será documentado no repositório, incluindo os prompts utilizados quando aplicável, conforme orientação do edital.
