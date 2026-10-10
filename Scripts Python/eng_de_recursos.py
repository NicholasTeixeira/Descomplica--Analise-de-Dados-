import pandas as pd
import numpy as np

# --- Parte 1: Análise de Dados da Bovespa ---
# Carregamento dos dados
df = pd.read_csv('/content/bovespa_tidy.csv')

# Filtragem para ITUB4
df_itau = df[df['Ticker'] == 'ITUB4'].copy()

# Conversão de data
df_itau['Date'] = pd.to_datetime(df_itau['Date'], format='%Y-%m-%d')

# Criação de Médias Móveis (Engenharia de Recursos)
df_itau['mm5d'] = df_itau['Close'].rolling(5).mean()
df_itau['mm21d'] = df_itau['Close'].rolling(21).mean()
df_itau['mm60d'] = df_itau['Close'].rolling(60).mean()

# Seleção de features (recursos)
features_bovespa = df_itau.drop(['Ticker', 'Date', 'Close'], axis=1)

# --- Parte 2: Análise de Dados do Titanic ---
# Carregamento dos dados do Titanic
df_titanic = pd.read_csv('http://bit.ly/kaggletrain')

# One-Hot Encoding para 'Embarked'
emb = pd.get_dummies(df_titanic['Embarked'])
df_titanic = pd.concat([df_titanic, emb], axis=1)

# One-Hot Encoding para 'Sex' com drop_first para evitar a armadilha da variável dummy
df_titanic_final = pd.get_dummies(df_titanic, columns=['Sex'], drop_first=True)

print("Processamento concluído com sucesso!")
