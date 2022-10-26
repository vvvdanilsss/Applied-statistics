from sympy import integrate, Symbol

x = Symbol('x')
mean = str(integrate(2 ** x * 2 * x, (x, 0, 1)))
print(mean.replace('**', '^').replace('log', 'ln').replace(' ', ''))