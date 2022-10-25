from sympy import *


def convert(s):
    """
    Преобразует выражения для читаемости в ответах на открытом образовании;
    :param s: Исходное выражение посчитанное sympy;
    :return: Преобразованное выражение
    """
    s = '^'.join(str(s).split('**'))
    lst = list(map(lambda x: x.split('*'), s.split()))

    for i, line in enumerate(lst):
        for j, value in enumerate(line):
            try:
                lst[i][j] = str(round(float(value), 4))
            except ValueError:
                continue
        lst[i] = '*'.join(lst[i])

    s = ''.join(lst)
    return s


x, y, c, t, k = symbols('x, y, c, t, k')
# Ищу параметр "c" исходя из того, что повторный интеграл от двумерной плотности должен быть равен 1
c = float(*solve(c * integrate(integrate((4 * x + 5) * y, (y, 0, 5 - (5 / 2) * x)), (x, 0, 2)) - 1))
print(f'c = {round(c, 4)}')

fx = c * integrate((4 * x + 5) * y, (y, 0, 5 - (5 / 2) * x))  # Одномерная функция плотности f(x)
fy = c * integrate((4 * x + 5) * y, (x, 0, 2 - (2 / 5) * y))  # Аналогично f(y)
print(f'x не принадлежит (0, 2]: f(x) = {0}, x принадлежит (0, 2]: f(x) = {convert(fx)}')
print(f'y не принадлежит (0, 5]: f(y) = {0}, x принадлежит (0, 5]: f(y) = {convert(fy)}')

fxy = c * integrate(integrate((4 * t + 5) * k, (k, 0, y)), (t, 0, x))
print('x < 0, y < 0: F(x, y) = 0')
print(f'(x, y) принадлежит K: F(x, y) = {convert(fxy)}')
print('x > 2, y > 5: F(x, y) = 1')
