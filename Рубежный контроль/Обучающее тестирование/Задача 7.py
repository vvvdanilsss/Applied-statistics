from sympy import *

c, x, y = symbols('c, x, y')
c = float(*solve(integrate(integrate(c * (1 + x) * y, (x, y, - y + 2)), (y, 0, 1)) - 1))
print(c)

p = integrate(integrate(c * (1 + x) * y, (y, 0, x)), (x, 0, 1))
print(p)

fi_xi1_x01 = integrate(c * (1 + x) * y, (y, 0, x))
fi_xi1_x12 = integrate(c * (1 + x) * y, (y, 0, - x + 2))
fi_xi2 = integrate(c * (1 + x) * y, (x, y, - y + 2))

print(fi_xi1_x01.subs(x, 0.5))
print(fi_xi1_x12.subs(x, 1.5))
print(fi_xi2.subs(y, 0.5))
