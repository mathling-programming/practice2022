import numpy as np

data = np.genfromtxt("sample.csv", delimiter=",")

mean_values = np.mean(data, axis=1)
std_values = np.std(data, axis=1)

renamed_rows = np.arange(2, len(data) + 2)
renamed_rows_df = np.column_stack((renamed_rows, mean_values, std_values))

filtered_data = renamed_rows_df[renamed_rows_df[:, 2] < 250]

np.savetxt('output.txt', filtered_data, delimiter='\t', fmt='%.2f')