from math import factorial, exp

l = 4.3
p = 1 - sum(((l ** k / factorial(k)) * exp(-l) for k in range(8)))
print(round(p, 3))