from sympy import *


def convert(s):
    """
    Преобразует выражения для читаемости в ответах на открытом образовании;
    :param s: Исходное выражение посчитанное sympy;
    :return: Преобразованное выражение
    """
    s = str(s).replace('**', '^')
    s = s.replace('log', 'ln')
    lst = list(map(lambda x: x.split('*'), s.split()))

    for i, line in enumerate(lst):
        for j, value in enumerate(line):
            try:
                lst[i][j] = str(round(float(value), 6))
            except ValueError:
                continue
        lst[i] = '*'.join(lst[i])

    s = ''.join(lst)
    return s


x, y = symbols('x, y')
y = solve(x - 2 ** y, y)
print(convert(simplify(2 / 3 * y[0] * diff(y[0]))))