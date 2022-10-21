from numpy.random import choice
from scipy.stats import binom
import math
import sympy

n, p = 1100, 0.0024  # количество семян, вероятность прижиться

# метод "в лоб"
iterator = 100000
successes = 0

for _ in range(iterator):
    pool = tuple(choice([1, 0], n, p=[p, 1 - p]))
    if sum(pool) >= 3:
        successes += 1

print(f'метод "в лоб": вероятность = {round(successes / iterator, 3)}')

# формула Бернулли
probability = 0

for k in range(3):
    probability += binom.pmf(k, n, p)  # приживутся менее 3 семян

probability = 1 - probability  # приживутся не менее 3 семян
print(f'формула Бернулли: вероятность = {round(probability, 3)}')

# теорема Пуассона
probability = 0

for k in range(3):
    lamda = p * n
    probability += (lamda ** k / math.factorial(k)) * math.exp(- lamda)  # приживутся менее 3 семян

probability = 1 - probability  # приживутся не менее 3 семян
interval = min(p, n * p ** 2)
left_border = probability - interval
right_border = probability + interval
print(f'теорема Пуассона: вероятность = {round(probability, 3)}')
print(f'левая граница интервала = {round(left_border, 3)}, правая граница интервала = {round(right_border, 3)}')

# интегральная теорема Муавра-Лапласа
k = 3  # минимум прижившихся
q = 1 - p
np = n * p
npq = n * p * q
a, b = (k - np) / sympy.sqrt(npq), (n - np) / sympy.sqrt(npq)
x = sympy.Symbol('x')
probability = (1 / sympy.sqrt(2 * sympy.pi)) * float(sympy.Integral(sympy.exp(-x ** 2 / 2), (x, a, b)).doit())
print(f'интегральная теорема Муавра-Лапласа: вероятность = {round(probability, 3)}')
print(f'погрешность = {round(1 / (p * q * sympy.sqrt(n)), 3)}')
