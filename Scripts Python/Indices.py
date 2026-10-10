#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

# In[1]:


frutas = ['maça', 'banana', 'abacaxi']
frutas

# In[2]:


frutas[0]

# In[4]:


frutas[0:3]

# In[5]:


frutas[1:]

# In[6]:


frutas[0:]

# In[7]:


frutas[-1]

# In[17]:


df_acoes = pd.read_csv('/content/bovespa_tidy.csv', sep=',')
df_acoes

# In[26]:


df_vale = df_acoes[(df_acoes['Ticker'] == 'VALE3') & (df_acoes['Close'] > 52)]
df_vale

# In[28]:


df_acoes['Ticker'].unique()

# In[29]:


df1 = df_vale.loc[:, 'Date']
df1

# In[34]:


df2 = df_vale.loc[475:488, ['Ticker', 'Open', 'Close']]
df2

# In[41]:


df3 = df_vale.iloc[0]

# In[42]:


df3

# In[45]:


df4 = df_vale.iloc[0:4, :]
df4

# In[ ]:



