import os
import math
from manage_data import print_to_txt, strip_ext

## Дано:
a = 0
b = 1
n = 100
def f_(x):
    return math.exp(math.cos(x))

OUTPUT_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'
OUTPUT_GRAPH_PATH = f'txt\\output_{strip_ext(os.path.basename(__file__))}.png'
TO_FILE = True
 
def rectangular(a, b, n, f_):
    h = (b-a)/n
    h2 = h/2.0
    s = 0.0
    for j in range(n):
        x = a + j * h - h2
        s = s + f_(x)
    return s * h

def trapezoidal(a, b, n, f_):
    h = (b - a) / n
    s = (f_(a) + f_(b)) * 0.5
    for j in range(0, n - 1):
        x = a + j * h
        s = s + f_(x)
    return s * h

def simpson(a, b, n, f_):
    n2 = n * 2 
    n1 = n2 - 1 
    h = (b - a) / n2
    s = f_(a) + f_(b)
    for j in range(0, n1):
        z = 3.0 - math.pow((-1),j)
        x = a + j * h 
        s = s + z * f_(x)
    return s * h / 3


@print_to_txt(TO_FILE, OUTPUT_PATH)
def main():
    print(f"метод прямоугольников: a = {a}, b = {b}, n = {n}")
    print(rectangular(a, b, n, f_))
    print()

    print(f"метод трапеций: a = {a}, b = {b}, n = {n}")
    print(trapezoidal(a, b, n, f_))
    print()

    print(f"метод Симпсона: a = {a}, b = {b}, n = {n}")
    print(simpson(a, b, n, f_))
    print()


if __name__ == '__main__':
    main()
