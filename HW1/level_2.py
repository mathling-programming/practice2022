import math

def log_graph(func, min_x, max_x, step):
    values = []
    x = min_x
    while x <= max_x:
        try:
            values.append(func(x))
        except:
            x += step
        x += step

    dif = max(values)
    array = []
    while dif >= min(values):
        graph = ['*' if abs((dif-values[i])/step)<1 else ' ' for i in range(len(values))]
        if '*' not in graph:
            graph.insert(array[-1].index('*'),'*')
        array.append(graph)
        dif -= 0.06
    for i in array:
        print(''.join(i))


log_graph(lambda x: math.log(x), 0.0, 1.5, 0.1)