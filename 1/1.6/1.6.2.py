from numpy import random


n = 10000000
successes = 0
for _ in range(n):
    cards = []
    if ball1 == ball2:
        successes += 1
print(round(successes / n, 3))