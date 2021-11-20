import os
import numpy as np
from read_matrix import read_matrix, print_matrix, strip_ext, print_to_txt


INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
DEBUG = True
TO_FILE = True


def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = make_householder(A[i:, i])
        Q = np.dot(Q, H)
        A = np.dot(H, A)
    return Q, A

def make_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    # чтение из файла
    matrix = np.array(read_matrix(INPUT_PATH))

    # вывод
    print('Матрица: ')
    print_matrix(matrix, digits=5, space=12)

    # запишем матрицу как A для краткости
    A = np.array(matrix)

   
    Q, R = qr(A)
    print('Q:')
    print_matrix(Q, digits=8, space=12)
    print('R:')
    print_matrix(R, digits=8, space=12)
    
    
    print('собственные числа:')
    print(*[f'λ{i} = {n:.9f}' for i, n in enumerate(np.diagonal(R))], sep='\n')

if __name__ == "__main__":
    main()