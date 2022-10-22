from numpy import random

n = 100000
successes = 0
floors = list(range(2, 8))

for _ in range(n):
    lst = random.choice(floors, 4)
    if len(set(lst)) == 4:
        successes += 1

print(round(successes/n, 3))