from sympy import *

k, x = symbols('k, x')
k = float(*solve(integrate(k * (3 * x + 1) ** 2, (x, 3, 4)) - 1))
print(k)
p = integrate(k * (3 * x + 1) ** 2, (x, 3, 3.5))
print(p)
e = integrate(x * k * (3 * x + 1) ** 2, (x, 3, 4))
print(e)
d = integrate(x ** 2 * k * (3 * x + 1) ** 2, (x, 3, 4)) - e ** 2
print(d)