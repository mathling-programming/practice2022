import numpy as np


def plot_function(function_name: str = None, min_x: float = None, max_x: float = None, step_size: float = None):
    # Retrieve the function from the numpy library based on the provided function name
    func = np.__dict__[function_name]

    # Calculate the range and center point
    range_size = max_x - min_x
    center_point = int((range_size / 2) / step_size)

    # Generate the points on the graph
    x = min_x
    points = []
    while x <= max_x:
        y = func(x)
        points.append((int(x / step_size), int(round(y / step_size, 1))))
        x += step_size

    # Sort the points based on the y-coordinate in descending order
    sorted_points = sorted(points, key=lambda p: p[1], reverse=True)

    # Remove duplicate points on the same line
    unique_lines = []
    for point in sorted_points:
        line = [p for p in sorted_points if p[1] == point[1]]
        if line not in unique_lines:
            unique_lines.append(line)

    # Print the graph
    for line in unique_lines:
        to_print = []
        for point in line:
            while len(to_print) < (center_point + point[0]):
                to_print.append(' ')
            to_print.append('*')
        print(''.join(to_print))


# Example usage
plot_function(function_name='sin', min_x=0, max_x=10, step_size=0.1)