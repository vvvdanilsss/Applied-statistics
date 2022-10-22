from numpy.random import choice
from numpy import mean

xi_values = [-4, -2, 0, 3]
probability_values = [0.1, 0.1, 0.3, 0.5]
pool = choice(xi_values, 10000000, p=probability_values)
dispersion = round(mean((pool - mean(pool)) ** 2), 3)
sigma = round(dispersion ** 0.5, 3)
print(f'dispersion = {dispersion}, sigma = {sigma}')