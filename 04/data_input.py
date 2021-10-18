import numpy as np

# -------------------------------
# эти переменные используются в модуле build_graph.py
# для построения гшрафика

# функция f1(x) для графика
f_1 = lambda x: 1 - np.cos(x-1)

# функция f2(x) для графика
f_2 = lambda x: np.arcsin(1.6 - 2*x)

# ограничения масштаба графика
left_x_limiter = -4
right_x_limiter = 4

"--------------в обоих модулях---------------"
# приблизительные корни
root = {
    'x': 0.85,
    'y': 0.1,
}
"--------------mm_04_iterations.py---------------"
eps = 1e-4
# система уравнений
system_iter = {
    'x': lambda x: 1 - np.cos(x - 1),
    'y': lambda y: 0.8 - 0.5 * np.sin(y),
}

"--------------mm_04_newton.py---------------"

# вычисление нормы
def get_matrix_norm(matrix):
    res = 0
    for row in matrix:
        for elem in row:
            res += elem ** 2
    return np.sqrt(res)

def jacobi(roots):
    x, y = roots
    return [[-np.sin(x-1), 1],
            [2, np.cos(y)]]


def system_newton(roots):
    x, y = roots
    return [np.cos(x-1) + y - 1, 2*x + np.sin(y) - 1.6]
