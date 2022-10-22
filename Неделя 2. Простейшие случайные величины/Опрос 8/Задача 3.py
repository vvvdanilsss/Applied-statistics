from numpy.random import choice
from scipy.stats import binom
import math

n, p = 100, 0.02  # Количество испытаний, вероятность успеха

# Метод "в лоб"
iterator = 100000
successes = 0

for _ in range(iterator):
    pool = tuple(choice([1, 0], n, p=[1 - p, p]))
    if pool.count(0) <= 3:
        successes += 1

print(f'метод "в лоб": вероятность = {round(successes / iterator, 2)}')

# Формула Бернулли
probability = 0

for k in range(4):
    probability += binom.pmf(k, n, p)

print(f'формула Бернулли: вероятность = {round(probability, 2)}')

# Теорема Пуассона
probability = 0

for k in range(4):
    lamda = p * n
    probability += (lamda ** k / math.factorial(k)) * math.exp(- lamda)

interval = min(p, n * p ** 2)
left_border = probability - interval
right_border = probability + interval
print(f'теорема Пуассона: вероятность = {round(probability, 2)}')
print(f'левая граница интервала = {round(left_border, 2)}, правая граница интервала = {round(right_border, 2)}')

# Локальная теорема Муавра-Лапласа
q = 1 - p
np = n * p
npq = n * p * q
probability = (1 / math.sqrt(npq)) * (
            1 / math.sqrt(2 * math.pi) * sum(math.exp(-((k - np) / math.sqrt(npq)) ** 2 / 2) for k in range(4)))
print(f'локальная теорема Муавра-Лапласа: вероятность = {round(probability, 2)}')
