from sympy import *

a, x, t = symbols('a, x, t', real=True)

a = solve(integrate(exp(3 * x), (x, 0, a)) - 1, a)
print(a)
x1 = integrate(0, (x, -oo, 0))
print(x1)
x2 = integrate(exp(3 * t), (t, 0, x))
print(x2)
x3 = integrate(0, (x, a, oo))
print(x3)
