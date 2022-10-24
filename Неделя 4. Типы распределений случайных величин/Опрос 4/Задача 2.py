from sympy import *

x, y, c, t, k = symbols('x, y, c, t, k')
c = float(*solve(c * integrate(integrate(x * y, (y, 0, 3 - 1.5 * x)), (x, 0, 2)) - 1))
print(c)

fx = c * integrate(x * y, (y, 0, 3 - 1.5 * x))
fy = c * integrate(x * y, (x, 0, 2 - (2 / 3) * y))
print(fx, fy)

fxy = (c * integrate(integrate(t * k, (k, 0, y)), (t, 0, x)))
print(fxy)
fxy = integrate(fx, (x, 0, x))
print(fxy)
fxy = integrate(fy, (y, 0, y))
print(fxy)
fxy = (c * integrate(integrate(x * y, (y, 0, 3 - 1.5 * x)), (x, 0, 2)))
print(fxy)