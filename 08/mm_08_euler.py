import os
import numpy as np
from manage_data import print_to_txt, strip_ext
from given import a, b, f_1, f_2, y_1, y_2, h


OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
TO_FILE = True


@print_to_txt(TO_FILE, OUTPUT_PATH)
def euler():
    L = round((b-a) / h)
    X_1 = np.zeros(L)
    X_2 = np.zeros(L)
    X_1[0] = y_1
    X_2[0] = y_2    
    for i in range(1, L):
        X_1[i] = X_1[i-1] + h * f_1(X_1[i-1], X_2[i-1])
        X_2[i] = X_2[i-2] + h * f_2(X_1[i-1], X_2[i-1])

    print('метод Эйлера:')
    print('1я функция:')
    for e in X_1:
        print(f'{e:.3f}')
    print()

    print('метод Эйлера:')
    print('2я функция:')
    for e in X_2:
        print(f'{e:.3f}')
    print()


if __name__ == '__main__':
    euler()
