import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def compute_rolling_word_lengths(group):
    word_lengths    = group['WORD'].apply(len)
    rolling_word_lengths = word_lengths.rolling(window=10).mean().tail(20)
    return rolling_word_lengths.values.tolist()

def plot_rolling_word_lengths(rolling_word_df):
    figure(figsize=(20, 10))
    for column in rolling_word_df.columns:
        plt.bar(column, rolling_word_df[column])
    plt.savefig('chart.jpg')
    plt.show()

def save_grouped_word_lengths(rolling_word_df):
    rolling_word_df.to_html('output.html')

def main():
    text_df = pd.read_csv('text.csv')
    vocab_df = pd.read_csv('vocab.csv')

    merged_df = text_df.merge(vocab_df, on='WORD')

    consecutive_same_pos = merged_df[merged_df['POS'] == merged_df.shift(-1)['POS']]
    groups = merged_df.groupby('POS')

    rolling_word_lengths = [compute_rolling_word_lengths(group_data) for _, group_data in groups]
    rolling_word_df = pd.DataFrame(rolling_word_lengths, index=[group_name for group_name, _ in groups])

    plot_rolling_word_lengths(rolling_word_df)
    save_grouped_word_lengths(rolling_word_df)

if __name__ == '__main__':
    main()