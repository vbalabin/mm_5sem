import sys
from read_and_calc import read_equation_coeffs, calculate_nonlinear
from read_and_calc import print_to_txt, get_currently_executed_file, INPUT_FILE
from read_and_calc import calculate_diff_1, calculate_diff_2
from read_and_calc import ISOLATIONS

eps = 0.001
IS_TO_TXT = True
OUTPUT_FILE = f'txt/output_{get_currently_executed_file(sys.argv[0])}.txt'

def newton_method(a, b, eps, f_, diff1_f, diff2_f):
    if f_(a) * diff2_f(a) > 0:
        x = a
    elif f_(b) * diff2_f(b) > 0:
        x = b
    else:
        raise ValueError("Условие сходимости для метода Ньютона не выполнено, f(x0)*f''(x0) < 0")

    it = 0
    while f_(x) > eps:
        step_numerator = f_(x)
        step_denumerator = diff1_f(x)
        x = x - step_numerator / step_denumerator
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

    # задаем функцию первой производной
    diff1_f = lambda x: calculate_diff_1(coeffs, x)

    # задаем функцию второй производной
    diff2_f = lambda x: calculate_diff_2(coeffs, x)

    print('список коэффициентов: ', end='')
    print(*coeffs, sep=', ')
    print('-'*32)

    for key, e in zip(iso.keys(), iso.values()):
        x, it = newton_method(e.a, e.b, eps, f_, diff1_f, diff2_f)
        print(f'{key} = {x:.5f}, f(x) = {f_(x):.6f}, eps = {eps}, iterations: {it}')
    print()

main()