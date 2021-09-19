import numpy as np
import sympy as sp
from read_matrix import make_wide_matrix, read_matrix, print_matrix, print_to_txt

INPUT_PATH = 'txt\\input.txt'
OUTPUT_PATH = 'txt\\output_newton.txt'
DEBUG = True
TO_FILE = False

@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    x, y = sp.symbols('x,y')
    eq1 = sp.Eq(sp.cos(x + 0.5) - y, 2)
    eq2 = sp.Eq(sp.sin(y) + 2*x, 1)
    result = sp.solve([eq1, eq2], (x, y))
    print(result)


main()
