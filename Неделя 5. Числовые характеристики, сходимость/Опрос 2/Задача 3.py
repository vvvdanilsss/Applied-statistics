from sympy import integrate, Symbol, solve

x = Symbol('x')
median = float(solve(integrate(2 * x) - 0.5)[-1])
print(round(median, 3))