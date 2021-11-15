import os
import numpy as np
from manage_data import strip_ext, print_to_txt, load_input_data, pretty_print
from build_graph import build_graph_lab6


INPUT_PATH = 'txt\\input.json'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
OUTPUT_GRAPH_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.png'
TO_FILE = True


def lagrange(x_, y_, a):
    """
    рассчитать интерполяцию в точке
    """
    res = 0.0
    for i in range(len(y_)):
        t_ = y_[i]
        for j in range(len(y_)):
            if i != j:
                t_ *= (a - x_[j]) / (x_[i] - x_[j])
        res += t_
    return res


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():

    data = load_input_data(INPUT_PATH)
    x_1 = [float(x) for x in data.keys()]
    y_1 = [data[x] for x in data.keys()]
    print("Дано:")
    pretty_print(data)
    print()

    x_2 = np.arange(0.2, 2.0, 0.01)
    approximiate = lambda x: lagrange(x_1, y_1, x)
    y_2 = np.fromiter((approximiate(x) for x in x_2), dtype=np.float64)

    print("Интерполяционный многочлен Лангранжа:")
    result = {k: approximiate(k) for k in np.arange(0.3, 2.0, 0.2)}
    pretty_print(result)
    print()

    build_graph_lab6(x_1, y_1, x_2, y_2, OUTPUT_GRAPH_PATH)

if __name__ == '__main__':
    main()
