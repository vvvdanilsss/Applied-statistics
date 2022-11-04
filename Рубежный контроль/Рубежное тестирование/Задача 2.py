from numpy.random import choice

pool1 = [1] * 10 + [0] * 7
n = 1000000
suc = 0

for _ in range(n):
    pool2 = choice(pool1, 11, replace=False)
    if sum(pool2) == 5:
        suc += 1

print(suc / n)