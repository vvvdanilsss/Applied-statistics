from numpy import random

n = 100000
successes = 0
lst = [0.01, 0.05, 0.2]
for _ in range(n):
    while True:
        index = random.choice([0, 1, 2], p=[0.1, 0.2, 0.7])
        returned = random.choice([True, False], p=[lst[index], 1 - lst[index]])
        if returned:
            break
    if index == 1:
        successes += 1
print(round(successes/n, 3))