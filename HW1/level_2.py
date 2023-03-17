import math

def log_graph(min_x, max_x, step):
    values = []
    x = min_x
    while x <= max_x:
        try:
            values.append(math.log(x))
        except:
            x += 0.1
        x += 0.1

    dif = max(values)
    array = []
    while dif >= min(values):
        graph = ['*' if abs(dif-values[i])<0.1 else ' ' for i in range(len(values))]
        if '*' not in graph:
            graph.insert(array[-1].index('*'),'*')
        array.append(graph)
        dif -= 0.09
    for i in array:
        print(''.join(i))


log_graph(0.0, 1.5, 0.1)