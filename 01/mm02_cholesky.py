"https://www.youtube.com/watch?v=qNKyw5ED7eM"

import sys
import numpy as np
from read_matrix import read_matrix

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output.txt'

matrix_A, matrix_B = read_matrix(INPUT_PATH)

matrix_A = np.array(matrix_A)
matrix_B = np.array(matrix_B)

v, _ = np.linalg.eig(matrix_A)
print(v)