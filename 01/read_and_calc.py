import re
import sys
import functools
from collections import namedtuple

INPUT_FILE = 'txt/input.txt'
RootIsolation = namedtuple('RootIsolation', ['a', 'b'])
# промежутки изоляции корней, найденные графически
ISOLATIONS = { "x1": RootIsolation(-1, 0), "x2": RootIsolation(3, 4)}


def has_digit(string: str):
    """
    вспомогательная для read_equation_coeffs
    """
    for c in string:
        if c.isdigit():
            return True


def split_by_whitespace(string: str):
    """
    вспомогательная для read_equation_coeffs
    """
    result = list()
    for e in re.split('\s', string):
        if has_digit(e):
            e = e.replace(',', '.').replace('–', '-')
            num = float(e)
            result.append(num)
    return result


def read_equation_coeffs(filename):
    """
    читает коэффициенты из файла "filename"
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()

    coeffs = split_by_whitespace(line)
    return coeffs


def calculate_nonlinear(coeffs, x):
    """
    вычисляет значение заданной коэффициентами f(x) при заданном x
    """
    result = 0
    for i, c in enumerate(coeffs[::-1]):
        result += c * x ** i
    return result


def print_to_txt(is_set, path):
    def decorator_print(func):
        @functools.wraps(func)
        def wrapper_print(*args, **kwargs):
            if is_set:
                with open(path, 'w', encoding='utf-8') as fileout:
                    stdout = sys.stdout
                    sys.stdout = fileout
                    value = func(*args, **kwargs)

                with open(path, 'r', encoding='utf-8') as f:
                    sys.stdout = stdout
                    print(f.read())
            else:
                value = func(*args, **kwargs)
            return value
        return wrapper_print
    return decorator_print    