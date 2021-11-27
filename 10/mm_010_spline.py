import os
import numpy as np
from math import sqrt
from build_graph import build_graph_lab6

from manage_data import load_input_data, pretty_print, print_to_txt, strip_ext

INPUT_PATH = 'txt\\input.json'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
OUTPUT_GRAPH_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.png'
TO_FILE = True
 
def cubic_interp1d(x0, x, y):
    x = np.asfarray(x)
    y = np.asfarray(y)
 
    # проверка на отсортированность
    if np.any(np.diff(x) < 0):
        indexes = np.argsort(x)
        x = x[indexes]
        y = y[indexes]
 
    size = len(x)
 
    xdiff = np.diff(x)
    ydiff = np.diff(y)
 
    # создадим буферные матрицы
    Li = np.empty(size)
    Li_1 = np.empty(size-1)
    z = np.empty(size)
 
    # заполним диагоналт Li и Li-1 , решим [L][y] = [B]
    Li[0] = sqrt(2*xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0 # ограничение
    z[0] = B0 / Li[0]
 
    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]
 
    i = size - 1
    Li_1[i-1] = xdiff[-1] / Li[i-1]
    Li[i] = sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
    Bi = 0.0 # ограничение
    z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]
 
    # решаем [L.T][x] = [y]
    i = size-1
    z[i] = z[i] / Li[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]
 
    # найдем индекс
    index = x.searchsorted(x0)
    np.clip(index, 1, size-1, index)
 
    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0
 
    # подсчитаем cubic
    f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
         zi1/(6*hi1)*(x0-xi0)**3 + \
         (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
         (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
    return f0

def solve_diff(x_1, y_1):
    # x_3 = np.arange(x_1[0], x_1[-1], 0.05)
    # result = {k: v for k, v in zip(x_3 , cubic_interp1d(x_3, x_1, y_1))}
    y_diff = list()
    for i in range(0, len(x_1)):
        if i == 0:
            i = 1
        delta_x = x_1[i] - x_1[i-1]
        delta_y = y_1[i] - y_1[i-1]
        y_diff.append(delta_y / delta_x)
    return y_diff


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():

    data = load_input_data(INPUT_PATH)
    x_1 = [float(x) for x in data.keys()]
    y_1 = [data[x] for x in data.keys()]
    print("Дано:")
    pretty_print(data)
    print()

    y_diff = solve_diff(x_1, y_1)
    x_graph = np.arange(x_1[0], x_1[-1], 0.01)
    y_graph = cubic_interp1d(x_graph, x_1, y_diff)

    print("Производная табличной функции сплайном:")

    x_result = np.arange(x_1[0], x_1[-1], 0.05)
    result = {k: v for k, v in zip(x_result , cubic_interp1d(x_result, x_1, y_diff))}
    pretty_print(result)
    print()

    build_graph_lab6(x_1, y_1, x_graph, y_graph, OUTPUT_GRAPH_PATH)


if __name__ == '__main__':
    main()
    