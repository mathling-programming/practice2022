import numpy as np
from numpy import genfromtxt

# импортируем csv
sample = genfromtxt('sample.csv', delimiter=',', dtype= None )

# в массиве указана не экспоненциальная система (десятичная точка на 2 знака вправо)
data = np.array(sample)

# среднее для каждой строки
data_mean = np.mean(data[:], axis=1) # axis - ось массива (1 - строки)
print(data_mean)

# среднеквадратичное отклонение для каждой строки
data_std = np.std(data[:], axis=1) 
print(data_std)

# объединение столбцов массивов
data_full = np.column_stack([data_mean, data_std])
print(data_full)

output = []

for i, value in enumerate(data_full, 1):
    #print(f'{i} {value}') # нумерация строк
    for std in value:
        if std < 250: # выбираем std < 250
            index = np.array([i])
            general_array = np.column_stack([[index], [value]])
            output.append(general_array[0])
            
output_array = np.asarray(output)
print(output_array)

np.savetxt('output.txt', output_array, fmt='%.2f', delimiter='\t')
