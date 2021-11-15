import os
import numpy as np
from manage_data import strip_ext, print_to_txt, load_input_data, pretty_print
from build_graph import build_graph_lab6


INPUT_PATH = 'txt\\input.json'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
OUTPUT_GRAPH_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.png'
TO_FILE = True


def newton_interpolation(X, Y, x):
    """
    Рассчитать интерполяцию х точек
    """
    sum = Y[0]
    temp = np.zeros((len(X), len(X)))
    # Назначьте первую строку
    for i in range(0,len(X)):
        temp[i, 0] = Y[i]
    temp_sum = 1.0
    for i in range(1, len(X)):
        # х многочлен
        temp_sum = temp_sum * (x - X[i-1])
        # Рассчитать среднюю разницу
        for j in range(i, len(X)):
            temp[j, i] = (temp[j, i-1] - temp[j-1, i-1]) / (X[j] - X[j - i])
        sum += temp_sum * temp[i, i] 
    return sum    


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():

    data = load_input_data(INPUT_PATH)
    x_1 = [float(x) for x in data.keys()]
    y_1 = [data[x] for x in data.keys()]
    print("Дано:")
    pretty_print(data)
    print()

    approximiate = lambda x: newton_interpolation(x_1, y_1, x)
    x_2 = np.arange(0.2, 2.0, 0.01)
    y_2 = np.fromiter((approximiate(x) for x in x_2), dtype=np.float64)

    print("Интерполяционные полиномы Ньютона:")
    result = {k: approximiate(k) for k in np.arange(0.3, 2.0, 0.2)}
    pretty_print(result)
    print()

    build_graph_lab6(x_1, y_1, x_2, y_2, OUTPUT_GRAPH_PATH)


if __name__ == '__main__':
    main()
