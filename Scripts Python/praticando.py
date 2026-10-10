#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# In[ ]:


pip install yfinance pandas

# In[ ]:


import yfinance as yf

# In[ ]:


acao = yf.Ticker('ITUB4.SA')
data = acao.history(period='1y')

# In[ ]:


type(df)

# In[ ]:


df

# In[ ]:


df = data.filter(items=['Open', 'Close'])
df

# In[ ]:


df = data.filter(like='Dividends', axis=1)
df

# In[ ]:


df = data[(data.index > '2026-10-05')]
df

# In[ ]:


df = data[['Open', 'Close', 'High']]
df

# In[ ]:


df = data.index
df

# In[43]:


df = data.drop(['2025-10-07', '2025-10-08'], axis=0)
df

# In[50]:


df = data.drop(['Low', 'High'], axis=1)
df

# In[68]:


df['new_dividends'] = data['Dividends'].map({0:2.00})
df

# In[76]:


df['new_dividends'] = data['Dividends'].map({0:2.00})
df

# In[77]:


df.isnull()

# In[78]:


df.isnull().sum()

# In[80]:


media = df['new_dividends'].mean()
df = df['new_dividends'].fillna(media)
df

# In[82]:


df.isnull()
df.isnull().sum()
df

# In[ ]:



