import os
import numpy as np
from manage_data import print_to_txt, strip_ext
from given import a, b, f_1, f_2, y_1, y_2, h


OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
TO_FILE = True


@print_to_txt(TO_FILE, OUTPUT_PATH)
def adams_bashfort():
    L = round((b-a) / h)
    y1 = np.zeros(L)
    x = np.zeros(L)
    y2 = np.zeros(L)
    F1 = np.zeros(L)
    F2 = np.zeros(L)

    y1[0] = y_1
    y2[0] = y_2
    x[0] = a

    for i in range(L-1):
        F1[i] = f_1(x[i], y1[i], y2[i])
        F2[i] = f_2(x[i], y1[i], y2[i])
        y1[i + 1] = y1[i] + h * F1[i]
        y2[i + 1] = y2[i] + h * F2[i]
        x[i + 1] = x[i] + h

    for i in range(3, L-1):
        # четырехшаговый метод Адамса–Башфорта
        y1[i + 1] = y1[i] + (h / 24) * (55 * F1[i] - 59 * F1[i - 1] + 37 * F1[i - 2] - 9 * F1[i - 3])
        y2[i + 1] = y2[i] + (h / 24) * (55 * F2[i] - 59 * F2[i - 1] + 37 * F2[i - 2] - 9 * F2[i - 3])
        

    print('метод Адамса–Башфорта:')
    for i in range(len(y1)):
        print(f'{i+1:02d})  y1 = {y1[i]:6.3f} | y2 = {y2[i]:6.3f}')
    print()


if __name__ == '__main__':
    adams_bashfort()
