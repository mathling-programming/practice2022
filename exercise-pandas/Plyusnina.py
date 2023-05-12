#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd

df = pd.read_csv('text.csv')


# In[42]:


df


# In[43]:


df2 = pd.read_csv('vocab.csv')


# In[44]:


df2


# In[45]:


a = df.merge(df2, left_on='WORD', right_on='WORD', how='inner')


# In[46]:


a


# In[47]:


#a = a.dropna(axis=0)
#a


# In[48]:


a = a.sort_values(by='WORDNO', ascending= True)
a.reset_index(drop = True, inplace = True)
a


# In[49]:


new = []
res = []
ind = []
for i,item in enumerate(a['POS'], start=0):
    new.append(item)
    value = i-1
    if new[value] == new[i]:
        res.append(item)
        ind.append(i)


# In[50]:


new = a.loc[ind]
new


# In[51]:


lent = []
for i,item in enumerate(new['WORD'], start=0):
    lent.append(len(item))


# In[52]:


new['LEN'] = lent


# In[53]:


new


# In[54]:


new = new.groupby('POS').mean()[['LEN']]
new


# In[55]:


new.to_html('Results.html')


# In[56]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


plt.plot(new)


# In[59]:


plt.savefig('my_plot.png')


# In[ ]:




