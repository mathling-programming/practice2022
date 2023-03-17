import math

def cos_graph(min_x, max_x, step):
    values = []
    x = min_x
    while x <= max_x:
        values.append(math.cos(x))
        x += 0.1

    dif = max(values)
    while dif >= min(values):
        graph = ['*' if abs(round(dif-values[i],1))<0.1 else ' ' for i in range(len(values))]
        print(''.join(graph))
        dif -= 0.09


cos_graph(0.0, 10.0, 0.1)