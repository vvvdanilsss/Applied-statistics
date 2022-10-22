from numpy.random import uniform

n = 1000000
points_15 = list(uniform(0, 15, n))
points_18 = list(uniform(0, 18, n))
successes = 0

for _ in range(n):
    if points_15[_] <= 10 or points_18[_] <= 10:
        successes += 1

print(round(successes / n, 3))