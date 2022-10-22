import math
import numpy as np


def f_x(x, a):
    if x <= 0:
        return 0
    elif x > math.pi / 4:
        return 1
    else:
        return a * math.sin(x)


mean_a = np.average([0, math.sqrt(2)])
epsilon = 1e-5
p = f_x(math.pi / 4 + epsilon, mean_a) - f_x(math.pi / 4, mean_a)
print(f'вероятность события кси = пи / 4: {round(p, 3)}')

a = math.sqrt(2)
p = f_x(math.pi / 6 , a) - f_x(0, a)
print(f'вероятность события кси в интервале от 0 до пи / 6: {round(p, 3)}')