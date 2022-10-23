from numpy.random import choice
import numpy as np

p = 0.71
n = 1000000
successes = np.array([0] * 6)

for _ in range(n):
    hits = choice([1, 0], 5, p=[p, 1 - p])
    successes[sum(hits)] += 1

successes = np.divide(successes, n)
print(np.round(successes, decimals=3))
print(*(round(sum(successes[:_]), 3) for _ in range(7)))
