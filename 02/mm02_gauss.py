import sys
from read_matrix import make_wide_matrix, read_matrix, print_matrix, print_to_txt
import numpy as np

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output_gauss.txt'
DEBUG = True
TO_FILE = True

@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    # чтение из файла
    matrix_A, matrix_B = read_matrix(INPUT_PATH)
    b = [0] * 3
    A = [[0] * 4, [0] * 4, [0] * 4]
    A = np.zeros((3, 4), float)
    b[0] = 1.48
    b[1] = 1.92
    b[2] = 2.16

    A[0, 0] = 2.36
    A[0, 1] = 2.37
    A[0, 2] = 2.13
    A[0, 3] = b[0]

    A[1, 0] = 2.51
    A[1, 1] = 2.40
    A[1, 2] = 2.10
    A[1, 3] = b[1]

    A[2, 0] = 2.59
    A[2, 1] = 2.41
    A[2, 2] = 2.06
    A[2, 3] = b[2]


    #объединяем матрицы в расширенную
    wide_matrix = make_wide_matrix(matrix_A, matrix_B)
    print_matrix(wide_matrix)

    # переименуем для краткости
    a = wide_matrix
    a = A
    # количество строк
    n = len(a)
    # копим решение здесь
    x = [0] * n

    # Преобразование строк к верхнетреугольному
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('0 на главной диагонали, На 0 делить нельзя!')
            
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            
            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]
        
        if DEBUG:
            print('-'*32)
            print(f'i = {i}, ratio = {ratio:.3f}')
            print_matrix(a)

    # Последовательная подстановка снизу вверх
    x[n-1] = a[n-1][n] / a[n-1][n-1]

    for i in range(n-2, -1, -1):
        x[i] = a[i][n]
        
        for j in range(i+1, n):
            x[i] = x[i] - a[i][j]*x[j]
        
        x[i] = x[i] / a[i][i]

    # Вывод решения
    print('\nКорни системы: ')
    print(*[f'X{i} = {x[i]:.2f}' for i, e in enumerate(x)], sep=' | ')

main()
