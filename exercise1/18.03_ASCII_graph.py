# я не уверена, что нужно загружать код, разобранный на паре, но сделаю для отчётности

import math
from math import floor # модуль базовых мат. функций. если только import math, то прописывай math.floor
import sys # взаимодействие с окружением(?)

f = math.__dict__[sys.argv[1]] # атрибут модуля с доступом ко всем объектам внутри него. #argv — список строчек, argv[1] — элемент
minx = float(sys.argv[2]) 
maxx = float(sys.argv[3])
dx = float(sys.argv[4])

print(f'#### {sys.argv[1]} {minx} {maxx} {dx}')

grid = {} # пустой ассоциативный массив для инициации переменной

for i in range (floor(minx / dx), floor(maxx / dx) + 1):
    y = f(i * dx)
    j = math.floor(y / dx)
    if j not in grid:
        grid[j] = {}
    grid[j][i] = '*'

prevj = None
for j in sorted(grid, reverse = True):
    if prevj is not None:
        print('\n' * (j - prevj - 1), end='')
    prevj = j
    previ = math.floor(minx / dx) - 1
    for i in sorted(grid[j]): # вывод
        print(' ' * (i - previ - 1), end='')
        print(grid[j][i], end='')
        previ = i # сохранение значения абсциссы
    print('')

#в конце — run customised. писать с 'sin'. первое число — минимальное значение, второе — максимальное, третье — шаг. числа с десятыми (1.0)
