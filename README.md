# 📊 Projeto Descomplica: Análise de Dados & Automações

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

Este repositório centraliza meus estudos, experimentações e implementações práticas em **Ciência de Dados** e **Automação de Processos**. O foco principal é a aplicação de bibliotecas do ecossistema Python para transformar dados brutos em insights estratégicos e otimizar a gestão de produtividade.

---

## 🚀 Estrutura do Projeto

O projeto está organizado para separar a fase de experimentação da fase de implementação:

- 📂 `notebooks/`: Contém arquivos `.ipynb` com análises exploratórias, visualizações e documentação passo a passo.
- 📂 `Scripts Python/`: Contém arquivos `.py` com o código refatorado e pronto para execução, simulando um ambiente de produção.
- 📂 `data/`: Repositório de datasets utilizados nas análises.

---

## 📈 Destaques Técnicos

### 1. Análise de Dados (Pandas)
Implementação de fluxos de **Data Cleaning** e **EDA (Exploratory Data Analysis)**:
- **Análise ProUni:** Manipulação de grandes bases de dados para identificar os cursos com maiores mensalidades e a distribuição de bolsas, utilizando `groupby`, `agg`, `fillna` e funções `lambda`.
- **Análise Financeira:** Extração e tratamento de dados de dividendos e séries temporais de ativos financeiros (ex: ITUB4) via `yfinance`.

### 2. Automações de Produtividade
Criação de ferramentas para otimização de tempo e organização:
- **Sincronização Trello $\rightarrow$ Google Agenda:** Implementação de integração via API REST, utilizando OAuth 2.0 e Tokens de acesso para automatizar a criação de eventos no calendário a partir de cards do Trello.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.13
- **Bibliotecas Principais:** 
  - `Pandas` (Manipulação e análise de dados)
  - `NumPy` (Computação numérica)
  - `YFinance` (Dados financeiros)
- **Ferramentas de Desenvolvimento:**
  - `Jupyter Notebook` (Experimentação e documentação)
  - `Git & GitHub` (Controle de versão e colaboração)
  - `API REST` (Integrações externas)

---

## 📖 Como Iniciar

Para reproduzir as análises ou executar os scripts:

1. Clone o repositório:
   ```bash
   git clone https://github.com/NicholasTeixeira/Descomplica--Analise-de-Dados-.git
   ```
2. Instale as dependências:
   ```bash
   pip install pandas numpy yfinance
   ```
3. Para as automações, configure suas chaves de API no arquivo `.env` (conforme instruções em `INICIAR_SESSAO.txt`).

---

## 📝 Notas de Evolução
Este projeto é vivo. Cada nova aula e desafio é refletido aqui através de commits organizados, seguindo as convenções de *Conventional Commits* para manter a rastreabilidade e profissionalismo do histórico.

---
Maintained by [Nicholas Teixeira](https://www.linkedin.com/in/nicholas-d-teixeira/)
