from math import factorial, exp

l = 5.5  # Лямбда в законе Пуассона (индекс у "П")
p = sum(((l ** k / factorial(k)) * exp(-l) for k in range(6)))  # Менее 6 значит k in range(6), если не менее, то 1 - p
print(round(p, 3))
