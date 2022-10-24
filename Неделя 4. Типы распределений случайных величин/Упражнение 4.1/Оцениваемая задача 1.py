from numpy.random import choice
import numpy as np

p = 0.51  # Вероятность выполнить 1 задание правильно
n = 1000000
successes = np.zeros(8)

for _ in range(n):
    tasks = choice([1, 0], 7, p=[p, 1 - p])  # Генератор выполненных и невыполненных заданий
    successes[sum(tasks)] += 1  # Индекс это количество выполненных заданий

successes = np.divide(successes, n)  # Получаю массив вероятностей выполнить количество заданий равное индексам массива
print(np.round(successes, decimals=3))
print(round(sum(successes[3:5]), 3))  # Суммируя вероятности, получаю вероятность решить больше 2, но не больше 4
