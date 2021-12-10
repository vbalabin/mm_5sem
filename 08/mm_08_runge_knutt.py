import os
import numpy as np
from manage_data import print_to_txt, strip_ext
from given import a, b, f_1, f_2, y_1, y_2, h


OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
TO_FILE = True


@print_to_txt(TO_FILE, OUTPUT_PATH)
def runge_kutt():
    L = round((b-a) / h)
    X_1 = np.zeros(L)
    X_2 = np.zeros(L)
    X_1[0] = y_1
    X_2[0] = y_2
    for i in range(L - 1):
        k0_1 = h * f_1(X_1[i], X_2[i]); # K0 для 1й функции
        k0_2 = h * f_2(X_1[i], X_2[i]); # K0 для 2й функции
        k1_1 = h * f_1(X_1[i] + h / 2, X_2[i] + (h / 2) * k0_1) # K1 для 1й функции
        k1_2 = h * f_2(X_1[i] + h / 2, X_2[i] + (h / 2) * k0_2) # K1 для 2й функции
        k2_1 = h * f_1(X_1[i] + h / 2, X_2[i] + (h / 2) * k1_1) # K2 для 1й функции
        k2_2 = h * f_2(X_1[i] + h / 2, X_2[i] + (h / 2) * k1_2) # K2 для 2й функции
        k3_1 = h * f_1(X_1[i] + h, X_2[i] + h * k2_1) # K3 для 1й функции
        k3_2 = h * f_2(X_1[i] + h, X_2[i] + h * k2_2) #K3 для 2й функции
        X_1[i + 1] = X_1[i] + (k0_1 + 2 * k1_1 + 2 * k2_1 + k3_1) / 6 # метод Рунге — Кутты для 1й функции
        X_2[i + 1] = X_2[i] + (k0_2 + 2 * k1_2 + 2 * k2_2 + k3_2) / 6 # метод Рунге — Кутты для 2й функции

    print('метод Рунге–Кутта:')
    print('1я функция:')
    for e in X_1:
        print(f'{e:.3f}')
    print()

    print('метод Рунге–Кутта:')
    print('2я функция:')
    for e in X_2:
        print(f'{e:.3f}')
    print()


if __name__ == '__main__':
    runge_kutt()
