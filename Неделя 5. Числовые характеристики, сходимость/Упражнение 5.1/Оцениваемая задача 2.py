from sympy import Symbol

a_xi, b_xi = 2, 6  # Индексы у U для кси
a_eta, b_eta = 2, 8  # Индексы у U для эты
xi = Symbol('xi')

eta = (xi - a_xi) / (b_xi - a_xi)
eta = a_eta + eta * (b_eta - a_eta)  # Зависимость эты от кси
print(f'eta = teta0 * xi + teta1: {eta}')
