from sympy import Symbol

a_xi, b_xi = 2, 3
a_eta, b_eta = -1, 4
xi = Symbol('xi')

eta = (xi - a_xi) / (b_xi - a_xi)
eta = a_eta + eta * (b_eta - a_eta)
print(eta)