from sympy import *


def f(s, x=Symbol('x')):  # Функция распределения F(x)
    t = Symbol('t')
    l = 3.1  # Лямбда (индекс у "Exp")
    if s == "x <= 0":
        return integrate(0, (t, -oo, x))
    elif s == "x > 0":
        return integrate(0, (t, -oo, 0)) + integrate(l * exp(-l * t), (t, 0, x))


p = f('x > 0', 5 + 1e-5) - 2 * f('x > 0', 5) + 1
print(f'P(xi > 5): {p}')
print(f'x <= 0: {f("x <= 0")}, x > 0: {f("x > 0")}')