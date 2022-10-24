from sympy import *


def f(s, x=Symbol('x')):
    t = Symbol('t')
    if s == 'x <= 0':
        return integrate(0, (t, -oo, x))
    elif s == 'x > 0':
        return integrate(0, (t, -oo, 0)) + integrate(3 * exp(-3 * t), (t, 0, x))


t = Symbol('t')
print(f('x <= 0'))
print(f('x > 0'))

p = f('x <= 0', -4) + 1 - f('x > 0', 2)
print(p)