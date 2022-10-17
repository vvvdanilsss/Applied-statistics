import sympy

p3 = sympy.Symbol('p3')
p3 = round(*sympy.solvers.solve(
    1 / 4 + 1 / 6 + p3 + 1 / 12 - 1, p3), 1)
print(p3)