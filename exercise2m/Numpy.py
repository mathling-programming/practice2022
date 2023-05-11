#1-ый вариант

# импортируем библиотеку
import numpy as np

# разделитель - ','; пропуск заголовка
data = np.genfromtxt('sample.csv', delimiter=',', skip_header=1) # импортируем данные из .csv

k = 0
result_1 = np.empty((0,3), int) # создаем пустой массив

for i in data[:,]: # пробегаемся по строчкам в массиве
  k += 1 # номер строчки в массиве
  mean = np.mean(i)
  std = np.std(i)
  
  if std <= 250:
    result_1 = np.append(result_1, np.array([[k, mean, std]]), axis=0)

print(result_1)
np.savetxt('output_1.txt', result_1, fmt='%.2f', delimiter='\t')

#2-ый вариант

rows = data.shape[0] # количество строчек

indexes = np.arange(1, rows + 1)
indexes = np.reshape(indexes, (-1,1))

new_data = np.hstack([indexes, data])

data_std = np.std(data, axis = 1)
std_array = data_std[data_std <= 250].reshape((-1,1))
temp = new_data[data_std <= 250]

id_array = temp[:,0].reshape((-1,1))

data_mean = np.mean(data, axis = 1)
mean_array = data_mean[data_std <= 250].reshape((-1,1))

result_2 = np.hstack([id_array, mean_array, std_array])

np.savetxt('output_2.txt', result_2, fmt='%.2f', delimiter='\t')
