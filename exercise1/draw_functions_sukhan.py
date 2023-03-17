import math

def draw_func(function, min_range: float = -10.0, max_range: float = 10.0, delta: float = 1.0):
    full_range = int(max_range - min_range)
    results = []
    # positions = []
    xes = []
    cut = []
    for i in range(int((full_range) / delta) + 1): # собираем списки иксов и греков с интервалом в d
        try:
            results.append(function(min_range + i * delta))
            xes.append(min_range + i * delta)
        except:
            cut.append(min_range + i * delta)

    min_range_y = min(results)
    max_range_y = max(results)
    results_sorted = sorted(results)
    min_shift = abs(results_sorted[1] - results_sorted[0])
    for num, i in enumerate(results_sorted[1:]):
        min_shift = min(min_shift, abs(i - results_sorted[num - 1]))
    epsilon = 0.000005 # для сравнения флоатов, эпсилон +-
    k_range = math.ceil((max_range_y - min_range_y) / delta)
    last_line = ' ' * int(full_range / delta) # так выглядит базовая строчка графика
    # print(f'вот они {k_range}')
    # настраиваем точность округления с учётом d
    round_range = 0 if float(int(delta)) == delta else abs(str(delta).find('.') - len(str(delta))) - 1
    # print(f'окрулгление до {round_range}')
    lines = []
    for k in range(k_range + 1): # составляем строчки графика. итерируем по длине оси ординат
        this_line_objects = []
        for number, n in enumerate(results):
            # итерируем по значениям y. если найдётся совпадение, ок, иначе дублирует предыдущую строчку
            # при формировании строки нужно подстроиться под то, что значения x могут быть
            # любыми, а вот координаты элементов строк всегда неотрицательны. отсюда формулы.
            # predict = k * delta - k_range / 2 * delta
            predict = k * delta - k_range / 2 * delta + (min_range_y + max_range_y) / 2
            # print(predict, n)
            if - 1 * epsilon < round(predict, round_range) - round(n, round_range) < epsilon:
                symbol = '*' #стандартный символ
                try: # проверка на бесконечность или деление на 0
                    r = function(xes[number] - delta)
                    l = function(xes[number] + delta)
                    if abs((function(xes[number] - delta) - n) / delta) < 0.1:
                        symbol = '-' #функция почти одинакова
                    elif function(xes[number] - delta) < n and function(xes[number] + delta) < n:
                        symbol = '^' # локальный максимум
                    elif function(xes[number] - delta) > n and function(xes[number] + delta) > n:
                        symbol = 'v'# локальный минимум
                    elif function(xes[number] - delta) < n and function(xes[number] + delta) > n:
                        if abs((function(xes[number] + delta) - n) / delta) > 10:
                            symbol = '|' # функция сильно возрастает или убывает
                        else:
                            symbol = '/' # функция возрастает
                    elif function(xes[number] - delta) > n and function(xes[number] + delta) < n:
                        if abs((function(xes[number] - delta) - n) / delta) > 10:
                            symbol = '|' # функция сильно возрастает или убывает
                        else:
                            symbol = r'\\' # функция убывает
                except: # так отображаются lim функции
                    symbol = '0'
                this_line_objects.append((int((xes[number] - min_range) / delta), symbol)) # все значения x, при которых соответствующий y

        new_line = ' ' * int(full_range / delta)
        # print(this_line_objects)
        for items in this_line_objects:
            new_line = new_line[:items[0]] + items[1] + new_line[items[0]:]
            last_line = new_line
        if new_line == ' ' * int(full_range / delta):
            new_line = last_line
        lines.append(new_line) # собрали строчку и добавили её в список
    # return results, positions, xes, min_shift
    for line in lines[::-1]: # рисуем график (наоборот, чтобы не получился вниз головой)
        print(line)

    # return


# ПРИМЕРЫ. ЗАКОММЕНТИРОВАТЬ ДЛЯ СКРЫТИЯ
of = lambda x: 2 * x
# print(draw_func(function=of))
print(draw_func(function=lambda x: math.sin(x), min_range= -10, max_range = 10, delta = 0.1))
# print(draw_func(function=of, min_range= -10, max_range = 10, delta = 0.1))
print(draw_func(function=lambda x: math.log10(x), min_range= 0, max_range = 10, delta = 0.1))
print(draw_func(function=lambda x: 1 / (x * x - 1), min_range= -10, max_range = 10, delta = 0.1))

# print('*\n' * 100)
