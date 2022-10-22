from numpy.random import uniform

n = 1000000
necessary_points = list(filter(lambda x: x <= 45, list(uniform(40, 70, n))))
print(round(len(necessary_points) / n, 3))