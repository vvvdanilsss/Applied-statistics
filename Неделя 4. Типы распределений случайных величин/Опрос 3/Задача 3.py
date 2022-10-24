from sympy import *


def f(x, a, sigma):
    t = Symbol('t')
    return 1 / (sigma * sqrt(2 * pi)) * integrate(exp(-(t - a) ** 2 / (2 * sigma ** 2)), (t, -oo, x))


p = f(3, 2.5, 2) - f(-3, 2.5, 2)
print(p)