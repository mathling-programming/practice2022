import math


def sin_graph(min_x, max_x, step):
    values = []
    x = min_x

    while x <= max_x:
        values.append(math.sin(x))
        x += step

    for i in range(len(values)):
        k = values[i] - min(values)
        print(' '*int(abs(round(k,1))*10)+'*')

sin_graph(0.0, 7.3, 0.1)