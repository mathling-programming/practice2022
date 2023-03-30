import numpy as np
data = np.genfromtxt('sample.csv', delimiter=',', dtype=float, skip_header=1)
mean = np.mean(data, axis=1, keepdims=True)
std = np.std(data, axis=1, keepdims=True)
index = np.array(range(1, len(data) + 1))
index = index.astype(float)
mean = np.ravel(mean)
std = np.ravel(std)
new_data = np.vstack([index, mean, std]).T
output = new_data[new_data[..., 2] < 250]
np.savetxt('output.txt', output, delimiter='\t', fmt='%.2f')


