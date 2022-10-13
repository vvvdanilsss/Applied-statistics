from numpy import random

n = 100000
successes = 0
for _ in range(n):
    mans = list(random.choice(['watch', 'not watch'], 3, p=[0.7, 0.3]))
    if mans.count('watch') == 2:
        successes += 1
print(round(successes/n, 3))