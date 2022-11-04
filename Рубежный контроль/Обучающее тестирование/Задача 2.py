from numpy.random import choice

basket = [1] * 5 + [0] * 10
n = 1000000
successes = 0

for _ in range(n):
    pool = choice(basket, 7, replace=False)
    if sum(pool) == 3:
        successes += 1

print(round(successes / n, 3))