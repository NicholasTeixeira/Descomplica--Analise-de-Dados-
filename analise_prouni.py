#!/usr/bin/env python
# coding: utf-8

# # 🎓 Análise de Dados do ProUni
# Este notebook realiza a análise da base de dados de cursos, mensalidades e bolsas do ProUni.

# In[4]:


import pandas as pd

# In[7]:


df_prouni = pd.read_excel('/content/cursos-prouni.csv.xlsx')
df_prouni

# In[12]:


pd.set_option('display.max_rows', 1000)

# In[13]:


df_prouni['curso_busca'].value_counts()

# In[14]:


df_prouni['mensalidade'].max()

# In[19]:


df_prouni.groupby('uf_busca')['mensalidade'].agg(['sum'])

# In[20]:


df_prouni.groupby(['uf_busca', 'curso_busca'])['mensalidade'].agg(['mean'])

# In[21]:


df_prouni.groupby(['uf_busca', 'curso_busca'])['mensalidade'].agg(['mean']).sort_values(by= ['uf_busca', 'mean'])

# In[24]:


def duplicabolsa(rows):
    nova_bolsa = rows * 2
    return nova_bolsa

# In[26]:


df = df_prouni[['uf_busca', 'curso_busca', 'mensalidade', 'bolsa_integral_ampla']]
df

# In[27]:


df ['nova_bolsa'] = df['bolsa_integral_ampla'].apply(duplicabolsa)
df

# In[30]:


df['nova_bolsa'] = df['nova_bolsa'].fillna(1)
df

# In[32]:


df['nova_bolsa_lambda'] = df['bolsa_integral_ampla'].apply(lambda x: x * 2)
df

# In[34]:


df = df.assign(nova_bolsa_lambda2 = lambda x : (x['bolsa_integral_ampla'] * 2))
df

# In[ ]:



