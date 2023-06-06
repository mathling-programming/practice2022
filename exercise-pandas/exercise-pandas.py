import pandas as pd
import matplotlib.pyplot as plt

text = pd.read_csv('text.csv', na_filter=False)
vocab = pd.read_csv('vocab.csv', na_filter=False)

merged = text.merge(vocab, on=['WORD'], how='left')

filtered = merged[merged['POS'] != merged['POS'].shift()]

grouped = filtered.groupby('POS')

means = {}
names = grouped.groups.keys()
for name, group in grouped:
    group['LENGTH'] = group['WORD'].apply(lambda x: len(x))
    if len(group) > 10:
        window = 10
    else:
        window = 1
    group['MEAN'] = group['LENGTH'].rolling(window).mean()
    for i in names:
        if i in name:
            means[i] = group['MEAN'].values[-1]
    group.to_html(open('result.html', 'a', encoding='utf-8'))
    
    

plot_keys = list(means.keys())
plot_values = list(means.values())

plt.figure(figsize=(25, 5))
plt.bar(range(len(means)), plot_values, width=0.5, align='edge', tick_label = plot_keys)
plt.savefig('bars.png')

