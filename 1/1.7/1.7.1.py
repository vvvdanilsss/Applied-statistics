from numpy import random

n = 100000
lst_x = [0] * 8 + [1] * 2
lst_y = [0] * 9 + [1]
successes = 0
for _ in range(n):
    x = random.choice(lst_x)
    y = random.choice(lst_y)
    if x != y:
        successes += 1
print(round(successes/n, 3))