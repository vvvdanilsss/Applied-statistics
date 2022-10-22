from scipy.stats import binom
import sympy

n, p = 4100, 0.63  # Количество яиц, вероятность вылупления

# Формула Бернулли
probability = 0

for k in range(2536, 2630):
    probability += binom.pmf(k, n, p)  # Родится от 2536 до 2629

print(f'формула Бернулли: вероятность = {round(probability, 3)}')

# Теорема Пуассона
probability = 0.644932415424308985  # Посчитал в вольфраме
interval = min(p, n * p ** 2)
left_border = probability - interval
right_border = probability + interval
print(f'теорема Пуассона: вероятность = {round(probability, 3)}')
print(f'левая граница интервала = {round(left_border, 3) if left_border > 0 else 0}, правая граница интервала = {round(right_border, 3) if right_border < 1 else 1}')

# Интегральная теорема Муавра-Лапласа
k1, k2 = 2536, 2629  # от 2536 до 2629
q = 1 - p
np = n * p
npq = n * p * q
a, b = (k1 - np) / sympy.sqrt(npq), (k2 - np) / sympy.sqrt(npq)
x = sympy.Symbol('x')
probability = (1 / sympy.sqrt(2 * sympy.pi)) * float(sympy.Integral(sympy.exp(-x ** 2 / 2), (x, a, b)).doit())
print(f'интегральная теорема Муавра-Лапласа: вероятность = {round(probability, 3)}')
print(f'погрешность = {round(1 / (p * q * sympy.sqrt(n)), 3)}')