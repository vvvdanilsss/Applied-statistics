from math import factorial as fact

x = 1
a = sum(x ** i / fact(i) for i in range(6))
print(round(a, 3))