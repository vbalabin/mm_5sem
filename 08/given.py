import numpy as np


# Дано
a = 0
b = 4
f_1 = lambda y1, y2: 1 / (np.power(y1, 2) + np.power(y2, 2))
f_2 = lambda y1, y2 : np.cos(y1 + y2)
y_1 = -1
y_2 = 1
h = 0.1
