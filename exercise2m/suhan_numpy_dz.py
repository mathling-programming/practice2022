import numpy as np

arr = np.genfromtxt('sample.csv', delimiter=',', dtype=float)
print(arr)
means = []
stds = []
result = []
for n, i in enumerate(arr):
    m = np.mean(i)
    s = np.std(i)
    stds.append(s)
    result.append([n + 1, m, s])
means_array = np.array(means)
# print(means_array)
# print(np.mean(arr[0]))

result = np.array(result)
# print(result)
# print(len(arr))
# print(len(result))
res_fil = np.delete(result, np.where(
    (result[:, 2] >= 250)), axis=0)
print(res_fil)
np.savetxt('output.txt', res_fil, fmt='%.2f', delimiter='\t')


