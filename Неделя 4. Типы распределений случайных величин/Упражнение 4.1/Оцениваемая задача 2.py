from numpy.random import choice
import numpy as np

p = 0.6  # Вероятность удержаться у каждого участника
n = 100000
successes = np.zeros(5)

for _ in range(n):
    m = 0  # Количество попыток участников
    attempt = 0
    while attempt < 1 and m < 5:  # До первого победителя. Менее 5 попыток
        m += 1
        attempt = choice([1, 0], p=[p, 1 - p])  # Генератор результата 1 попытки
    if m < 5:
        successes[m] += 1  # Индекс это количество попыток до первого победителя

successes = np.divide(successes, n)  # Получаю массив вероятностей удержаться на конкретной попытке
print(np.round(successes, decimals=3))
print(round(sum(successes), 3))  # Кто-то победит это сумма вероятностей удержаться менее чем за 5 попыток
