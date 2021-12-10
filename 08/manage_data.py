import re
import sys
import functools


def strip_ext(name):
    """
    вспомогательный
    """
    _i = name.rfind('.')
    name = name[:_i]
    return name


def has_digit(string: str):
    """
    вспомогательная для read matrix
    """
    for c in string:
        if c.isdigit():
            return True


def split_by_whitespace(string: str):
    """
    вспомогательная для read matrix
    """
    result = list()
    for e in re.split('\s', string):
        if has_digit(e):
            e = e.replace(',', '.').replace('–', '-').replace('З', '3').strip()
            num = float(e)
            result.append(num)
    return result


def load_input_data(input_path):
    import json
    with open(input_path) as json_file:
        data = json.load(json_file)
        return data


def pretty_print(values):
    for x in values:
        print(f'при x = {float(x):.2f} , y = {values[x]:.3f}')


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
