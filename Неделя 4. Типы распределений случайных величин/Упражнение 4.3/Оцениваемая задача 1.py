from numpy.random import uniform


def fxy(x, y):  # Функция плотности f(x, y)
    if a_x <= x <= b_x and a_y <= y <= b_y:
        return 1 / ((b_x - a_x) * (b_y - a_y))
    else:
        return 0


def fx(x):  # Одномерная функция плотности f(x)
    if a_x <= x <= b_x:
        return 1 / (b_x - a_x)
    else:
        return 0


def fy(y):  # Аналогично f(y)
    if a_y <= y <= b_y:
        return 1 / (b_y - a_y)
    else:
        return 0


a_x, a_y, b_x, b_y = 8, 2, 10, 8  # Края области K
x1, y1, x2, y2 = 0, 0, 9, 6  # Одна точка из области K, другая - нет
print(f'(x, y) не принадлежит K: f(x, y) = {fxy(x1, y1)},(x, y) принадлежит K: f(x, y) = {round(fxy(x2, y2), 4)}')
print(f'x не принадлежит [8, 10]: f(x) = {fx(x1)}, x принадлежит [8, 10]: f(x) = {round(fx(x2), 4)}')
print(f'y не принадлежит [2, 8]: f(y) = {fy(y1)}, y принадлежит [2, 8]: f(y) = {round(fy(y2), 4)}')

iterator = 10000000
pool_x = uniform(a_x, b_x, iterator)  # Равномерно заполняю 10000000 точек отрезок a_xb_x
pool_y = uniform(a_y, b_y, iterator)  # Аналогично a_yb_y
successes = 0

for _ in range(iterator):
    if 9.4 <= pool_x[_] <= 13 and 2.7 <= pool_y[_] <= 8:  # Проверяю попадание точки в данную в условии область
        successes += 1

print(f'P(x принадлежит [9.4, 13], y принадлежит [2.7, 8]) = {round(successes / iterator, 4)}')
