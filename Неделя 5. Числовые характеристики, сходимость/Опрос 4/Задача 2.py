from sympy import integrate, Symbol

x = Symbol('x')
mean = str(integrate(2 ** x * 2 * x, (x, 0, 1))).replace('**', '^').replace('log', 'ln').replace(' ', '')
mean2 = str(integrate(2 ** (2 * x) * 2 * x, (x, 0, 1))).replace('**', '^').replace('log', 'ln').replace(' ', '')
print(f'{mean2}-({mean})^2')