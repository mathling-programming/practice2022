#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from numpy import genfromtxt
import pandas as pd


# In[40]:


file = genfromtxt('sample.csv', delimiter=',', dtype= None ) #открываю файл чтобы читался
otkl = np.std(file, axis=1, keepdims=True) #считаю отклонение
otkl = np.around(otkl, decimals = 2) #округляю его до сотых 
#print(otkl)
srednee = np.mean(file, axis=1, keepdims=True) #считаю среднее
srednee = np.around(srednee, decimals = 2) #округляю до сотых
#print(srednee)

df = pd.DataFrame(srednee, columns=['mean']) #Создаю датафрейм тк по мне так удобнее и нагляднее
df_2 = pd.DataFrame(otkl, columns=['deflection']) 
df['deflection'] = df_2 #добавляю столбец
df = df.loc[df['deflection'] < 250] #убираю значения отклонения меньше 250
#print(df)


# In[39]:


with open('output.txt', 'w') as f: #записываю все в файл
    dfAsString = df.to_string(header=False, index=True)
    f.write(dfAsString)

