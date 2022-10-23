from numpy.random import choice
import numpy as np

p = 0.15
n = 100000
successes = np.array([0] * 10)

for _ in range(n):
    m = 0
    attempt = 0
    while attempt < 1 and m < 11:
        m += 1
        attempt = choice([1, 0], p=[p, 1 - p])
    if m < 10:
        successes[m] += 1

successes = np.divide(successes, n)
print(np.round(successes, decimals=3))
print(*(round(sum(successes[:_]), 3) for _ in range(11)))
