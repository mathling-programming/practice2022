import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#считать таблицы в датафреймы
text_df = pd.read_csv("text.csv")
vocab_df = pd.read_csv('vocab.csv')

#соединить датафреймы о столбцу WORD
annot_df = pd.merge(text_df, vocab_df, how='left', on='WORD')
filtered_df = annot_df[:]

#отфильтровать строки, следующие за строкой с таким же значением POS
for i in range(1, len(annot_df)-1):
    if filtered_df.loc[i, 'POS'] != filtered_df.loc[i-1, 'POS'] and \
    filtered_df.loc[i, 'POS'] == filtered_df.loc[i+1, 'POS']:
        filtered_df.loc[i, 'WORDNO'] = 0
filtered_df = filtered_df[filtered_df.WORDNO != 0]

#группировка числовых значений
for x in range(len(annot_df)):
    if str(annot_df.loc[x,'POS']).isnumeric():
        annot_df.loc[x, 'POS'] = 'NUM'

#группировка по полю POS
annot_df.loc[:, 'WORDLEN'] = [len(x) for x in annot_df.loc[:, 'WORD']]
grouped = annot_df.groupby('POS')
group_values = [group[0] for group in grouped]
mean_values = pd.DataFrame()

#вычисление скользящего среднего значения длины слова для каждой группы
for value in group_values:
    group_df = grouped.get_group(value)
    window = 3 if len(group_df) >= 3 else len(group_df)
    roll_mean = pd.DataFrame()
    roll_mean[f'{value}'] = group_df['WORDLEN'].rolling(window=window).mean()
    roll_mean = roll_mean.dropna()
    mean_values = pd.concat([mean_values, roll_mean], ignore_index=True)

#построение диаграммы
mean_values.plot()
plt.show()

#запись таблицы со средним скользящим значением длины слова
mean_values.to_html('mean_values_table.html')