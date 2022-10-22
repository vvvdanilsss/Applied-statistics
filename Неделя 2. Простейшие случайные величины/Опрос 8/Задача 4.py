import sympy

k, n, p = 2650, 20000, 0.13
# Интегральная теорема Муавра-Лапласа
q = 1 - p
np = n * p
npq = n * p * q
a, b = -np / sympy.sqrt(npq), (k - np) / sympy.sqrt(npq)
x = sympy.Symbol('x')
probability = (1 / sympy.sqrt(2 * sympy.pi)) * float(sympy.Integral(sympy.exp(-x ** 2 / 2), (x, a, b)).doit())
print(f'интегральная теорема Муавра-Лапласа: вероятность = {round(probability, 2)}')
print(f'погрешность = {round(1 / (p * q * sympy.sqrt(n)), 2)}')