#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

# In[ ]:


df = pd.read_excel('/content/planilha_vendas.xlsx')
df

# In[ ]:


pd.crosstab(df.pais, df.produto)

# In[ ]:


pd.crosstab(df.pais, df.produto, margins=True)

# In[ ]:


pd.crosstab(df.pais, [df.produto, df['garantia extendida']], margins=True)

# In[ ]:


pd.crosstab([df.produto], [df.pais], values=df.quantidade, aggfunc=np.sum, margins=True)

# In[ ]:


pd.crosstab([df.produto], [df.pais], values=df.quantidade, aggfunc=np.sum, margins=True)

# In[ ]:


df['valor_total'] = df.valorunitario * df.quantidade

df2 = df.copy()
df2

# In[ ]:


pd.crosstab(df2.pais, df2.produto, normalize='index')

# In[ ]:


pd.crosstab(df2.pais, df2.produto, normalize='index').round(4)*100

# In[54]:


df_tipo_cell = df.groupby('produto')
df_tipo_cell

# In[55]:


df_tipo_cell.ngroups

# In[56]:


df.groupby('pais').ngroups


# In[57]:


df.groupby('pais').groups


# In[59]:


df.groupby('pais').size()


# In[65]:


df.groupby('pais').get_group('Brasil')


# In[73]:


df.groupby('pais').mean(numeric_only=True)

# In[77]:


df.groupby(['pais', 'produto',])['valor_total'].sum()

# In[ ]:



