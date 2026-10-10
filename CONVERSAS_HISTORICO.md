# 📖 Diário de Bordo Técnico - Projeto Descomplica

Este arquivo serve como registro histórico de todas as interações, decisões técnicas e evoluções do projeto.

## 🗓️ Sessão: 07/10/2026
### Objetivos
- Sincronização de notebook do Google Colab com GitHub.
- Análise técnica de manipulação de dados com Pandas.

### Atividades Realizadas
1. **Sincronização de Arquivos:**
   - Substituição do arquivo `praticando.ipynb` local pela versão atualizada do Colab.
   - Configuração de autenticação via Personal Access Token (PAT) no Git para permitir pushes automáticos.

2. **Análise Técnica do Notebook:**
   - Verificação de aplicação de conceitos de Pandas:
     - [x] Filtros (`filter`, `like`, `items`).
     - [x] Exclusão de dados (`drop` axis 0 e 1).
     - [x] Mapeamento de valores (`map` e `where`).
     - [x] Tratamento de dados faltantes (`isnull().sum()` e `fillna()` com média).
   - Feedback técnico fornecido sobre a estrutura do código e sugestões de EDA (Análise Exploratória de Dados).

3. **Controle de Versão:**
   - Realização de commits profissionais e sucintos:
     - `feat: implement data extraction and manipulation for ITUB4 using yfinance and pandas`
     - `refactor: update date filter for dividend distribution mapping`
     - `refactor: generalize dividend mapping by removing date constraint`

### Conhecimentos Adquiridos/Discutidos
- Diferenças entre `.map()` e `.replace()` no Pandas.
- Gestão de credenciais do GitHub via CLI e Tokens.
- Fluxo de trabalho de Data Cleaning em notebooks.

---

## 🗓️ Atualização Final: 07/10/2026
### Fechamento de Sessão
- Criado o sistema de persistência de histórico via `CONVERSAS_HISTORICO.md`.
- Criado o guia de inicialização `INICIAR_SESSAO.txt`.
- Validada a aplicação de 100% dos conceitos do módulo de manipulação de dados com Pandas.
- Sessão finalizada com sucesso e sincronizada com o GitHub.

---

## 🗓️ Sessão: 07/10/2026 (Continuação)
### Objetivos
- Download e integração da base de dados do ProUni.
- Validação de conceitos de funções do Pandas.
- Criação de notebook de análise para Google Colab.

### Atividades Realizadas
1. **Gestão de Dados:**
   - Importação da base de dados do ProUni (mensalidades, cursos, bolsas) para a pasta `data/`.
   - Verificação da integridade dos dados via terminal.
2. **Desenvolvimento:**
   - Criação do notebook `analise_prouni.ipynb` com fluxos de limpeza, análise de Top 10 cursos mais caros e distribuição de bolsas.
3. **Validação Técnica:**
   - Revisão completa do notebook para confirmar a aplicação de: `fillna()`, `value_counts()`, `groupby()`, `agg()`, `sort_values()`, `apply()` e funções `lambda`.
   - Confirmada a aplicação de 100% dos conceitos teóricos de funções do Pandas.
4. **Sincronização:**
   - Realização de commits e push de todos os arquivos (dados e notebook) para o GitHub.

### Status Final
- Base de dados integrada.
- Notebook de análise criado e sincronizado.
- Módulo de Funções no Pandas totalmente concluído e validado.

---

## 🗓️ Sessão: 08/10/2026
### Objetivos
- Sincronização de ecossistema de produtividade (Trello $\rightarrow$ Google Agenda).
- Organização de prazos de estudo para a semana.

### Atividades Realizadas
1. **Integrações Técnicas:**
   - Implementação de fluxo OAuth 2.0 para Google Calendar API.
   - Integração com Trello API via Personal Access Token.
   - Automatização da leitura de cards do quadro "Rotina de Estudos" e criação de eventos correspondentes no Google Agenda.
2. **Sincronização de Agenda:**
   - Mapeamento e agendamento da "Aula de Análise de Dados - 08/10".
   - Mapeamento e agendamento da "Aula de Análise de Dados - Sexta-feira".
3. **Manutenção de Repositório:**
   - Execução de `git pull origin main` para garantir a versão mais recente do projeto.

### Status Final
- Ecossistema de produtividade totalmente conectado.
- Próximas aulas agendadas e visíveis no calendário.
- Ambiente técnico pronto para a próxima sessão de análise de dados.

### Adicionais de Agenda (Pessoal)
- Agendada Consulta de Avaliação Psicológica para 13/10/2026.
- Agendada Sessão de Terapia para 16/10/2026.

---

## 🗓️ Sessão: 10/10/2026
### Objetivos
- Sincronização do ambiente de trabalho e resgate do estado do projeto.
- Implementação de Engenharia de Recursos.

### Atividades Realizadas
1. **Manutenção e Contexto:**
   - Execução de `git pull origin main` e análise de logs para retomada.
   - Criação do documento `HISTORICO_COMMITS.md` com a tradução de todos os commits do repositório.
2. **Desenvolvimento Técnico:**
   - Criação do notebook `Eng de recursos.ipynb` focado em Feature Engineering.
   - Implementação de médias móveis (5d, 21d, 60d) para dados da Bovespa (ITUB4).
   - Aplicação de One-Hot Encoding para variáveis categóricas da base do Titanic (Sex, Embarked).
3. **Organização de Estrutura:**
   - Exportação da lógica do notebook para o script `eng_de_recursos.py`.
   - Refatoração da estrutura de pastas, movendo scripts para a pasta `Scripts Python`.
4. **Ritual de Versionamento:**
   - Implementação de novo fluxo: Registro no `HISTORICO_COMMITS.md` $\rightarrow$ Commit incluindo o registro.

### Status Final
- Notebook e script de Engenharia de Recursos criados e sincronizados.
- Estrutura de pastas corrigida (`Scripts Python`).
- Histórico de commits traduzido e fluxo de log estabelecido.
- Agendado estudo de **Numpy e Hadoop** para 11/10 às 09:30.
