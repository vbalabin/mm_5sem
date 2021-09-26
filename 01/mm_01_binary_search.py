import os
from read_and_calc import read_equation_coeffs, calculate_nonlinear
from read_and_calc import print_to_txt, strip_ext, INPUT_FILE
from read_and_calc import ISOLATIONS

eps = 0.001
IS_TO_TXT = True
OUTPUT_FILE = f'txt\\output_{strip_ext(os.path.basename(__file__))}.txt'

def binary_search(a, b, eps, f_):
    if f_(a) * f_(b) > 0:
        raise ValueError('Условие сходимости не выполнено, f(a)*f(b) > 0')

    is_increasing = True if f_(a) < 0 else False

    x = a
    it = 0
    while abs(f_(x)) > eps:
        x = a + (b - a) / 2 

        """
        if is_increasing:
            if f_(x) < 0:
                a = x
            else:
                b = x     
        else:
            if f_(x) < 0:
                b = x
            else:
                a = x            
        """
        if (f_(x) < 0) ^ is_increasing:
            b = x     
        else:
            a = x
        it += 1
    return x, it

@print_to_txt(IS_TO_TXT, OUTPUT_FILE)
def main():
    
    # ISOLATIONS это словарь(hashmap) с промежутками изоляции,
    # найденными графически, импортирован из вспомогательного модуля
    iso = ISOLATIONS

    # задаем функцию нелинейного уравнения
    coeffs = read_equation_coeffs(INPUT_FILE)
    f_ = lambda x: calculate_nonlinear(coeffs, x)

    print('список коэффициентов: ', end='')
    print(*coeffs, sep=', ')
    print('-'*32)

    for key, e in zip(iso.keys(), iso.values()):
        x, it = binary_search(e.a, e.b, eps, f_)
        print(f'{key} = {x:.5f}, f(x) = {f_(x):.6f}, eps = {eps}, iterations: {it}')
    print()

main()