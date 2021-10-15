import os
import numpy as np
from data_input import system_iter, root, eps
from output_help import strip_ext, print_to_txt

OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
TO_FILE = True

# вычисление нормы
def get_matrix_norm(matrix, x, y):
    res = 0
    for row in matrix:
        for func in row:
            res += func(x, y) ** 2
    return np.sqrt(res)


def iterate_roots(root, system, key):
    return system[key](root)


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():

    print("-"*32)
    print(f"приблизительные значения корня")
    print(f"x = {root['x']}, y = {root['y']}")

    i = 1
    while True:
        root['previous x'] = root['x']
        root['y'] = iterate_roots(root['x'], system_iter, 'x')
        root['x'] = iterate_roots(root['y'], system_iter, 'y')
        print("-"*32)
        print(f"итерация №{i}")
        print(f"x = {root['x']:.5f}, y = {root['y']:.5f}")
        if abs(root['x'] - root['previous x']) < eps:
            print("-"*32)
            break
        i += 1

    print(f"Ответ: x = {root['x']:.5f}, y = {root['y']:.5f}, eps = {eps}")

main()