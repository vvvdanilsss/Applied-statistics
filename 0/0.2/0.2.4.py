from math import factorial as fact

x = 1.57
y = x - x ** 3 / fact(3) + x ** 5 / fact(5) - x ** 7 / fact(7)
print(round(y, 3))