from random import randint
from django.conf import settings


def random_matrix(lines: int, columns: int):
    r_min = settings.MATRIX_RAND_MIN
    r_max = settings.MATRIX_RAND_MAX

    m = list()

    for i in range(lines):
        row = list()
        for j in range(columns):
            row.append(randint(r_min, r_max))
        m.append(row)
    return m


def matrix_add(a, b):
    result = list()

    for i in range(len(a)):
        row = list()
        for j in range(len(a[i])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def exec_operation(op: str, lines: int, columns: int):
    if op == 'add':
        result = matrix_add(lines, columns)
