import numpy as np
from read_matrix import make_wide_matrix, read_matrix, print_matrix, print_to_txt

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output_yakobi.txt'
DEBUG = True
TO_FILE = True


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    # чтение из файла
    matrix_A, matrix_B = read_matrix(INPUT_PATH)

    print_matrix(make_wide_matrix(matrix_A, matrix_B), digits=4, space=10)
    a = np.array(matrix_A)
    b = np.array(matrix_B)
    n, _ = a.shape


    def max_difference(x, x_last):
        result = 0
        for i in range(len(x)):
            current_value = abs(x[i] - x_last[i])
            if current_value > result:
                result = current_value
        return result

    def solve(a, b, n, eps):
        x = np.zeros(n)
        x_last = np.zeros(n)

        for i in range(n):
            x[i] = b[i] / a[i, i]

        k = 1
        while True:
            for i in range(n):
                s = 0
                for j in range(0, i-1):
                    s += a[i, j] * x[j]

                for j in range(i+1, n):
                    s += a[i, j] * x[j]
                x_last[i] = (b[i] - s) / a[i, i]

            norma = max_difference(x, x_last)
            if norma < eps or k > 25:
                break
            x = np.copy(x_last)
            k += 1

        return x, k

    eps = 0.01
    x, k = solve(a, b, n, eps)

    print('-' * ord(' ') + '\n')
    print('Корни системы: ')
    print(*[f'X{i} = {e}' for i, e in enumerate(x)], sep=' | ', end='\n')
    print(f'итераций произведено: {k}, eps = {eps}', end='\n\n')

    if DEBUG:
        print('проверка: ')
        _s = r"np.linalg.solve(a, b) ="
        print(_s, np.linalg.solve(a, b))


main()