from sympy import *

c, x, y = symbols('c, x, y')
c = float(*solve(integrate(integrate(c * (1 + 3 * x) * y, (y, x - 1, - x + 7)), (x, 1, 4)) - 1))
print(c)
p = integrate(integrate(c * (1 + 3 * x) * y, (y, x - 1, 3)), (x, 1, 4))
print(p)
fxi1_14 = integrate(c * (1 + 3 * x) * y, (y, x - 1, - x + 7))
fxi2_03 = integrate(c * (1 + 3 * x) * y, (x, 1, y + 1))
fxi2_36 = integrate(c * (1 + 3 * x) * y, (x, 1, - y + 7))
print(fxi1_14.subs(x, 1.5))
print(fxi2_03.subs(y, 2.5))
print(fxi2_36.subs(y, 3.5))