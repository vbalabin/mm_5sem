from mm01_gauss import TO_FILE
import sys
import numpy as np
from read_matrix import make_wide_matrix, read_matrix, print_matrix, print_to_txt

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output_cholesky.txt'
DEBUG = True
TO_FILE = True

@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    # чтение из файла
    matrix_A, matrix_B = read_matrix(INPUT_PATH)

    print_matrix(make_wide_matrix(matrix_A, matrix_B))
    matrix_A = np.array(matrix_A)
    matrix_B = np.array(matrix_B)

    # AT * Ax = AT * B
    matrix_A_T = matrix_A.transpose()

    prod_matrix_A = matrix_A_T @ matrix_A
    prod_matrix_B = matrix_A_T @ matrix_B
    print('-'*32)
    print_matrix(make_wide_matrix(prod_matrix_A, prod_matrix_B))

    def cholesky_decomposition(a):
        """
        Декомпозиция Холецкого
        Возвращает нижнетреугольную матрицу
        """

        L = np.zeros_like(a)
        n, _ = np.shape(L)

        # декомпозиция
        # i строка, j столбец, k для сбора суммы
        for i in range(n):
            for j in range(i+1):
                tmp_sum = sum(L[i][k] * L[j][k] for k in range(j))
                
                if (i == j): # Диагональные элементы
                    L[i][j] = np.sqrt(a[i][i] - tmp_sum)
                else:
                    L[i][j] = (1.0 / L[j][j] * (a[i][j] - tmp_sum))
        return L
    
    def solveLU(L, U, b):
        n, _ = np.shape(L)
        x = np.zeros(n)
        y = np.zeros(n)

        #прямая
        for i in range(n):
            y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]
        
        #обратная
        for i in range(n-1, -1, -1):
            x[i] = (y[i] - np.sum(U[i, i+1:n] * x[i+1:n])) / U[i,i]
        
        return x

    L = cholesky_decomposition(prod_matrix_A)
    if DEBUG:
        print('-'*32)
        print_matrix(L)
        # print_matrix(np.linalg.cholesky(prod_matrix_A))

    x = solveLU(L, L.transpose(), prod_matrix_B)
    if DEBUG:
        print('проверка: ')
        _s = r"np.linalg.solve(prod_matrix_A, prod_matrix_B) ="
        print(_s, np.linalg.solve(prod_matrix_A, prod_matrix_B))

    print('\nКорни системы: ')
    print(*[f'X{i} = {x[i]:.2f}' for i, e in enumerate(x)], sep=' | ')


main()
