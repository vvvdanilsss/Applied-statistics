from numpy.random import choice
from numpy import median

values_xi = [-4, -2, 0, 3, 4, 6, 7, 9]
probabilities_xi = [0.1, 0.15, 0.05, 0.15, 0.1, 0.05, 0.25, 0.15]
pool = choice(values_xi, 10000000, p=probabilities_xi)
print(f'expected value = {round(pool.mean(), 3)},'
      f' median = {median(pool)}')