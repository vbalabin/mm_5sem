import sys
import functools


def strip_ext(name):
    """
    вспомогательный
    """
    _i = name.rfind('.')
    name = name[:_i]
    return name

def make_wide_matrix(a , b):
    """
    """
    wide_matrix = list()
    for i, row_a in enumerate(a):
        line = list()
        for e in row_a:
            line.append(e)
        line.append(b[i])
        wide_matrix.append(line)
    return wide_matrix


def strip_ext(name):
    """
    вспомогательный
    """
    _i = name.rfind('.')
    name = name[:_i]
    return name


def print_matrix(m, digits=2, space=8):
    """
    """
    if len(m) < len(m[0]):
        for row in m:
            for e in row[:-1]:
                print(f'{e:-{space}.{digits}f}', end='') 
            print(f'  | {row[-1]:-{space}.{digits}f}', end='')
            print()
        print()
    
    elif len(m) == len(m[0]):
        for row in m:
            for e in row:
                print(f'{e:-{space}.{digits}f}', end='') 
            print()
        print()  


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
