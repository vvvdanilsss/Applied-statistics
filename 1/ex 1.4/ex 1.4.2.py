from numpy import random

n = 100000
successes = 0
lst = [0.1, 0.02, 0.08]
for _ in range(n):
    while True:
        index = random.choice([0, 1, 2], p=[0.06, 0.19, 0.75])
        returned = random.choice([True, False], p=[1 - lst[index], lst[index]])
        if returned:
            break
    if index == 0:
        successes += 1
print(round(successes/n, 3))