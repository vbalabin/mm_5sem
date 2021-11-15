import numpy as np
import os
from build_graph import build_graph_lab6

from manage_data import load_input_data, pretty_print, print_to_txt, strip_ext

INPUT_PATH = 'txt\\input.json'
OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
OUTPUT_GRAPH_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.png'
TO_FILE = True


def least_squares(x, y):
   """
   Функция для аппроксимации массива точек прямой, основанная на
   методе наименьших квадратов.

   :param points: Входной массив точек формы [N, 2]
   :return: Numpy массив формы [N, 2] точек на прямой
   """
   # Для метода наименьших квадратов нам нужно, чтобы X был матрицей,
   # в которой первый столбец - единицы, а второй - x координаты точек
   X = np.vstack((np.ones(x.shape[0]), x)).T
   normal_matrix = np.dot(X.T, X)
   moment_matrix = np.dot(X.T, y)
   # beta_hat это вектор [перехват, наклон], рассчитываем его в
   # в соответствии с формулой.
   beta_hat = np.dot(np.linalg.inv(normal_matrix), moment_matrix)
   intercept = beta_hat[0]
   slope = beta_hat[1]
   # Теперь, когда мы знаем параметры прямой, мы можем
   # легко вычислить y координаты точек на прямой.
   y_hat = intercept + slope * x
   # Соберем x и y в единую матрицу, которую мы собираемся вернуть
   # в качестве результата.
   points_hat = np.vstack((x, y_hat)).T

   return points_hat


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    data = load_input_data(INPUT_PATH)
    x_1 = np.array([float(x) for x in data.keys()])
    y_1 = np.array([data[x] for x in data.keys()])
    print("Дано:")
    pretty_print(data)
    print()    

    points = least_squares(x_1, y_1)
    x_2 = points[:, 0]
    y_2 = points[:, 1]
    result = {k: v for k, v in zip(x_2 , y_2)}
    print("Метод наименьших квадратов:")
    pretty_print(result)
    print()    

    build_graph_lab6(x_1, y_1, x_2, y_2, OUTPUT_GRAPH_PATH)


if __name__ == '__main__':
    main()