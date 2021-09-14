from read_matrix import read_matrix
import sys

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output.txt'

matrix_A, matrix_B = read_matrix(INPUT_PATH)

#объединяем матрицы в расширенную
wide_matrix = list()
for i, row_a in enumerate(matrix_A):
    line = list()
    for e in row_a:
        print(f'{e:-6}', end='')
        line.append(e)
    line.append(matrix_B[i])
    print(f'  | {matrix_B[i]:-6}', end='')
    wide_matrix.append(line)
    print()
print()

# переименуем для краткости
a = wide_matrix
# количество строк
n = len(a)
# копим решение здесь
x = [0] * n

# Преобразование строк
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('0 на главной диагонали, На ноль делить нельзя!')
        
    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]
        
        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Последовательная подстановка сверху вниз
x[n-1] = a[n-1][n] / a[n-1][n-1]

for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    
    for j in range(i+1, n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i] / a[i][i]

# Вывод решения
print('\nКорни системы: ')

print(*[f'X{i} = {x[i]:.2f}' for i, e in enumerate(x)], sep=' | ')