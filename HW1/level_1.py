import math

def graph(func, min_x, max_x, step):
    values = []
    x = min_x
    while x <= max_x:
        values.append(func(x))
        x += step

    dif = max(values)
    while dif >= min(values):
        graph = ['*' if abs((dif-values[i])/step)<0.5 else ' ' for i in range(len(values))]
        print(''.join(graph))
        dif -= 0.09


graph(lambda x: math.sin(x), 0.0, 10.0, 0.1)

graph(lambda x: math.cos(x), 0.0, 10.0, 0.1)