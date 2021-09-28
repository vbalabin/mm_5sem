import numpy as np

# функция f1(x) = cos(x+0.5) - 2
f_1 = lambda x: np.cos(x+0.5) - 2

# функция f2(x) = arcsin(1-2x)
f_2 = lambda x: np.arcsin(1 - 2*x)

# ограничения масштаба графика
left_x_limiter = -4
right_x_limiter = 4