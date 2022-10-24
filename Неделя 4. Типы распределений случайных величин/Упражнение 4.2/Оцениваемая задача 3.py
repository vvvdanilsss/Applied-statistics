from sympy import *


def f(x):
    t = Symbol('t')
    a, sigma = 4.2, sqrt(2.89)  # Параметры нормального распределения (sqrt(sigma) тк дано sigma**2)
    return 1 / (sigma * sqrt(2 * pi)) * integrate(exp(-(t - a) ** 2 / (2 * sigma ** 2)), (t, -oo, x))


p = f(7.09) - f(1.31)  # Значение функции распределения от правой границы минус - от левой
print(f'P(|xi - 4.2| <= 2.89) = {p}')