from numpy import random

n = 1000000
successes = 0
places = list(range(1, 11))

for _ in range(n):
    man1, man2 = random.choice(places, 2, replace=False)
    if abs(man1 - man2) == 1 or abs(man1 - man2) == 9:
        successes += 1

print(round(successes/n, 3))