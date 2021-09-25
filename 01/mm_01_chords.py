import sys
from read_and_calc import read_equation_coeffs, calculate_nonlinear
from read_and_calc import print_to_txt, get_currently_executed_file, INPUT_FILE
from read_and_calc import ISOLATIONS

eps = 0.001
IS_TO_TXT = True
OUTPUT_FILE = f'txt/output_{get_currently_executed_file(sys.argv[0])}.txt'

def chords_method(a, b, eps, f_):
    if f_(a) * f_(b) > 0:
        raise ValueError('Условие сходимости не выполнено, f(a)*f(b) > 0')

    it = 0
    while abs(f_(b)) > eps:
        step_numerator = (a - b) * f_(b)
        step_denumerator = f_(a) - f_(b)
        b = b - step_numerator / step_denumerator
        it += 1
    return b, it

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
        x, it = chords_method(e.a, e.b, eps, f_)
        print(f'{key} = {x:.5f}, f(x) = {f_(x):.6f}, eps = {eps}, iterations: {it}')
    print()

main()