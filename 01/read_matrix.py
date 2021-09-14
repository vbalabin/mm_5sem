import re

def has_digit(string: str):
    for c in string:
        if c.isdigit():
            return True

def split_by_whitespace(string: str):
    result = list()
    for e in re.split('\s', string):
        if has_digit(e):
            e = e.replace(',', '.').replace('–', '-')
            num = float(e)
            result.append(num)
    return result

def read_matrix(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    matrix_A, matrix_B = list(), list()
    for line in text.split('\n'):
        if has_digit(line):
            a, b = line.split('|')
            matrix_A.append(split_by_whitespace(a))
            matrix_B.append(float(f"{b.strip().replace(',', '.').replace('–', '-')}"))

    return matrix_A, matrix_B
