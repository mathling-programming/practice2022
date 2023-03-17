import math

def analysis_graph(min_x, max_x, step):
    values = []
    x = min_x
    while x <= max_x:
        try:
            values.append(math.cos(x))
        except:
            x += 0.1
        x += 0.1

    dif = max(values)
    array = []

    while dif >= min(values):
        graph = [' '] * len(values)
        for i in range(len(values)):
            if abs(round(dif-values[i],1))<step and values[i] > values[i-1]:
                graph[i] = '/'
            elif abs(round(dif-values[i],1))<step and values[i] < values[i-1]:
                graph[i] = '\\'
            if abs(round(dif-values[i],1))<step and abs((values[i]-values[i-1])/step)<0.001:
                graph[i] = '-'
            if abs(round(dif-values[i],1))<step and abs((values[i]-values[i-1])/step)>4:
                graph[i] = '|'
            if abs(round(dif-values[i],1))<step and i != len(values)-1:
                if values[i-1] < values[i] > values[i+1]:
                    graph[i] = '^'
                elif values[i - 1] > values[i] < values[i + 1]:
                    graph[i] = 'v'

        symbols = ['/', '\\', '-', '|']
        if graph == [' '] * len(values):
            for i in symbols:
                if i in array[-1]:
                    graph.insert(array[-1].index(i), i)

        array.append(graph)
        dif -= 0.09

    for i in array:
        print(''.join(i))

analysis_graph(-5.0, 5.0, 0.1)