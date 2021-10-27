import os
import numpy as np
from read_matrix import read_matrix, print_matrix, strip_ext, print_to_txt

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
DEBUG = True
TO_FILE = True

# функция для возведения матрицы в степень
def matrix_power(m, pow):
    if pow < 1:
        raise ValueError('power has to be 1+')
    
    result = np.copy(m)
    for _ in range(1, pow):
        result = result @ m

    return result


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    # чтение из файла
    matrix = read_matrix(INPUT_PATH)

    # вывод
    print('Матрица: ')
    print_matrix(matrix, digits=5, space=12)

    # запишем матрицу как M для краткости
    M = np.matrix(matrix)

    # массив-полуфабрикат для поиска коэффициентов 
    # характеристического уравнения
    A = list()

    # применение алгоритма рекуррентной формклы по методу леверье к A
    for n in range(M.shape[0] + 1):
        if n == 0:
            A.append(1)

        elif n == 1:
            A.append(float(M.trace()))

        else:
            sum = 0
            for k, a in zip(range(1, len(A) + 1), A[::-1]):
                S = float((matrix_power(M, k)).trace())
                sum += (-1)**(k+1) * a * S
            A.append(sum / n )

        if DEBUG:
            print(f'итерация: {n+1}')        
            print(f'A = {A[-1]:.9f}, * {(-1)**(n+2)}')
            print('-'*32)


    # коэффициенты характеристического полинома
    Q = [a * (-1)**(i+2) for i, a in enumerate(A)]
    
    print('коэффициенты характеристического уравнения:')
    print(*[f'{q:.9f}' for q in Q], sep=', ')
    print()
    print('собственные числа:')
    print(*[f'λ{i} = {n:.9f}' for i, n in enumerate(np.roots(Q))], sep='\n')


main()