import os
import numpy as np
from read_matrix import make_wide_matrix, read_matrix, print_matrix, strip_ext, print_to_txt


INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
DEBUG = True
TO_FILE = True


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    # чтение из файла
    matrix = read_matrix(INPUT_PATH)

    # вывод
    print('Матрица: ')
    print_matrix(matrix, digits=5, space=12)

    # запишем матрицу как M для краткости
    M = np.array(matrix)

    print("вектор столбец y0 первоначального приближения")
    print("для вычисления СЛАУ коэффициентов")
    y = [np.array([[1],
                    [0],
                    [0],
                    [0]])]
    print('y_0 = ', y, sep='\n')

    for i in range(M.shape[1]):
        print()
        print(f'M @ y[{i}], y{i+1} = ')
        y.append(M @ y[-1])
        print(y[-1])

    # Согласно тождеству Гамильтона –  Кели
    # L - Левая часть
    print()
    L = list()
    for vector in y[-2::-1]:
        L.append(vector)

    L = np.array(L)
    L = np.column_stack(L)

    # y4 правая часть
    size = M.shape[0]
    y4 = np.reshape(y[size], (size,))

    # векторное  равенство  (24)  эквивалентно  СЛАУ
    print()
    print("корни СЛАУ p1, p2, p3, p4 - коэффициенты характеристического уравнения")
    print_matrix(make_wide_matrix(L, y4), digits=5, space=12)

    _roots = np.linalg.solve(L, y4)
    Q = [1]
    for i in range(_roots.shape[0]):
        Q.append(float(_roots[i]) * (-1))

    print('коэффициенты характеристического уравнения:')
    print(*[f'{q:.9f}' for q in Q], sep=', ')
    print()
    print('собственные числа:')    
    print(*[f'λ{i} = {n:.9f}' for i, n in enumerate(np.roots(Q))], sep='\n')

main()