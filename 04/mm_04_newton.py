import os
import numpy as np
from data_input import jacobi, system_newton, root, eps
from output_help import strip_ext, make_wide_matrix, print_matrix, print_to_txt

OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
TO_FILE = True

# алгоритм итерации
def iterative_newton(fun, x0, jacobian, eps):
    max_iter = 20

    x_last = x0
    for k in range(max_iter):
        print('Итерация :', k + 1)
        # Решаем J(xn)*( xn+1 - xn ) = -F(xn):
        J = np.array(jacobian(x_last))
        F = np.array(fun(x_last))
        matr = make_wide_matrix(J, F)
        print_matrix(matr, digits=4)

        diff = np.linalg.solve( J, -F )
        x_last = x_last + diff

        # Условие выхода из цикла:
        if np.linalg.norm(diff) < eps:
            break

    print('количество итераций:', k + 1)

    return {'x': x_last[0], 'y': x_last[1]}


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():

    x0 = np.array([e for e in root.values()])
    result = iterative_newton(system_newton, x0, jacobi, eps)
    print(f"Ответ: x = {result['x']:.5f}, y = {result['y']:.5f}, eps = {eps}")

    # # проверка через fsvole модуля Scipy
    # from scipy.optimize import fsolve

    # sol = fsolve(system_newton, x0, fprime=jacobi, full_output=0)
    # print('solution fsolve:', sol)


main()
