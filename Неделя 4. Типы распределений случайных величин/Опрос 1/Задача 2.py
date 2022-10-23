from numpy.random import choice
import numpy as np

p1, p2, p3 = 0.6, 0.7, 0.8
n = 1000000

hits1 = choice([1, 0], n, p=[p1, 1 - p1])
hits2 = choice([1, 0], n, p=[p2, 1 - p2])
hits3 = choice([1, 0], n, p=[p3, 1 - p3])

attempts = tuple(zip(hits1, hits2, hits3))
successes = np.array([0] * 4)

for _ in range(n):
    successes[sum(attempts[_])] += 1

successes = np.divide(successes, n)
print(np.round(successes, decimals=3))
print(*(round(sum(successes[:_]), 3) for _ in range(5)))
