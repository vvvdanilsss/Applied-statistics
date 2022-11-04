from sympy import *

c, x = symbols('c, x')
c = float(*solve(integrate(c * x ** 2, (x, 0, 1)) - 1))
print(c)

p = integrate(c * x ** 2, (x, 0, 0.5))
print(round(p, 3))

mean = integrate(x * c * x ** 2, (x, 0, 1))
print(round(mean, 3))

dispersion1 = integrate((x - mean) ** 2 * c * x ** 2, (x, 0, 1))
dispersion2 = integrate(x ** 2 * c * x ** 2, (x, 0, 1)) - mean ** 2
print(round(dispersion1, 3))
print(round(dispersion2, 3))