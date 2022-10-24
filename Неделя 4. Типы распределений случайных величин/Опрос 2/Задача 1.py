import sympy as sp

a = sp.Symbol('a')
x = sp.Symbol('x')

a = sp.solvers.solve(sp.integrate(sp.diff(a * sp.sin(x), x), (x, 0, sp.pi / 6)) - 1)
print(*a)

a = 2
p = sp.integrate(sp.diff(a * sp.sin(x), x), (x, 0, sp.pi / 12))
print(p)