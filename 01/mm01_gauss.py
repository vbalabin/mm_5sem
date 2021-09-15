from read_matrix import make_wide_matrix, read_matrix, print_matrix
import sys

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output.txt'
DEBUG = True

# чтение из файла
matrix_A, matrix_B = read_matrix(INPUT_PATH)


#объединяем матрицы в расширенную
wide_matrix = make_wide_matrix(matrix_A, matrix_B)
print_matrix(wide_matrix)

# переименуем для краткости
a = wide_matrix
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