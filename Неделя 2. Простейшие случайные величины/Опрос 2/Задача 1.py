import itertools

pool = list(
    zip(map(sum, list(itertools.product(*[[0, 1]] * 3))), map(sum, list(itertools.product(*[[0, 1]] * 3))[::-1])))
# print(pool.count((Неделя 0. Введение в Python, Неделя 3. Общее понятие вероятностного пространства)) / len(pool))
# Неделя 0. Введение в Python.125
# print(pool.count((Неделя 1. Простейшая теория вероятностей, Неделя 2. Простейшие случайные величины)) / len(pool))
# Неделя 0. Введение в Python.375
# print(pool.count((Неделя 2. Простейшие случайные величины, Неделя 1. Простейшая теория вероятностей)) / len(pool))
# P
print(pool.count((3, 0)) / len(pool))
