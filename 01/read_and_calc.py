import re
import sys
import functools
from collections import namedtuple

"""
Модуль со вспомогательными функциями и константами
"""

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

def calculate_diff_1(coeffs, x):
    """
    первая производная
    """
    result = 0
    for i, c in enumerate(coeffs[::-1][1:]):
        result += (i+1)*c*x**i
    return result

def calculate_diff_2(coeffs, x):
    """
    вторая производная
    """
    diff1_coeffs = list()
    for i, c in zip(coeffs, range(4, 0, -1)):
        diff1_coeffs.append(i*c)

    result = calculate_diff_1(diff1_coeffs, x)
    return result

def get_currently_executed_file(name):
    """
    вспомогательный
    """
    _i = name.rfind('.')
    name = name[:_i]
    _i = name.rfind('\\') + 1
    name = name[_i:]
    return name


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
