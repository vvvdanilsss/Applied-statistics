from numpy.random import uniform


def f(x):  # Функция плотности
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


iterator = 10000000
pool = uniform(4, 6, iterator)  # Генератор 10000000 точек на отрезке от 4 до 6
successes = 0

for x in pool:
    if x < 5:
        successes += 1  # Считаю количество точек меньше 5

print(f'p(xi < 5) = {round(successes / iterator, 3)}')
a, b = 4, 6  # Интервал значений случайной величины
print(f'x < a или x > b: f(x) = {f(1)}, a <= x <= b: f(x) = {f(5)}')