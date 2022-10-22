from numpy import random

n = 100000
successes = 0

for _ in range(n):
    count = 0

    while True:
        if random.choice([True, False], p=[0.47, 0.53]) and count < 7:
            count += 1
        else:
            break
    if count == 7:
        successes += 1

print(round(successes/n, 3))