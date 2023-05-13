import pandas as pd
import matplotlib.pyplot as plt

# Загрузка таблиц
text_df = pd.read_csv('text.csv')
vocab_df = pd.read_csv('vocab.csv')

# Соединение таблиц по столбцу 'WORD'
merged_df = pd.merge(text_df, vocab_df, on='WORD')

# Фильтрация
filtered_df = pd.DataFrame()

for i in range(1, len(merged_df)):
    if merged_df.loc[i, 'POS'] == merged_df.loc[i - 1, 'POS']:
        filtered_df = pd.concat([filtered_df, merged_df.loc[i:i]])

filtered_df = filtered_df.copy()

# Вычисление длины слова
filtered_df['word_length'] = filtered_df['WORD'].apply(len)
# filtered_df['word_length'] = filtered_df['WORD'].str.len()

# Группируем по 'POS'
grouped = filtered_df.groupby('POS')

# Вычисляем скользящее среднее значение длины слова
filtered_df['rolling_mean'] = grouped['word_length'].transform(lambda x: x.rolling(window=100, min_periods=1).mean())

# Строим график
plt.figure(figsize=(10, 6))

for pos in filtered_df['POS'].unique():
    subset = filtered_df[filtered_df['POS'] == pos]
    plt.plot(subset['POS'], subset['rolling_mean'], label=pos)

plt.xlabel('Группы по POS')
plt.ylabel('Скользящее среднее значение длины слова')

plt.grid(True)
plt.title('Скользящее среднее значения длины слова сгруппированного по POS')
plt.savefig('diagram.png')

# Сохранение таблицы в HTML
filtered_df.to_html('table.html')
