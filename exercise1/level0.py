import math


def plot_function(f, minx, maxx, dx):
    num_steps = int((maxx - minx) / dx)

    for i in range(num_steps + 1):
        x = minx + i * dx
        y = f(x)
        num_symbols = int(y / dx)

        line = ' ' * num_symbols + '*'
        print(line)

#func
def sin_function(x):
    return math.sin(x)

#params
minx = 0
maxx = 2 * math.pi
dx = 0.1

# draw the line
plot_function(sin_function, minx, maxx, dx)