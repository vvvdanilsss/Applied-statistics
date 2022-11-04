from sympy import *

k = Symbol('k')
k = float(*solve(sum([(k + 1) * i for i in range(1, 7)]) - 1, k))
print(round(k, 3))

p = [(k + 1) * i for i in range(1, 7)]
print(p)
a = p[0] + p[4] + p[5]
print(round(a, 3))