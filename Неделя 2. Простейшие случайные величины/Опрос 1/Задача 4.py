from sympy import Symbol
from sympy.solvers import solve

fi = Symbol('fi')
solutions = solve(
    1.25 * fi ** 2 + 0.5 * fi + 0.5 * fi ** 2 + fi + 3 * fi + 0.75 * fi * 2 - 1, fi)
fi1, fi2 = solutions
print(f'fi1 = {round(fi1, 1)}, fi2 = {round(fi2, 1)}')