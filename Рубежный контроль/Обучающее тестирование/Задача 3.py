from numpy.random import choice

basket1 = [1] * 3 + [0] * 2
basket2 = [21] * 5 + [0] * 3
n = 100000
successes = 0

for _ in range(n):
    while True:
        basket3 = [choice(basket1), choice(basket2)]
        fruit = choice(basket3)
        if fruit == 1 or fruit == 21:
            break

    if fruit == 21:
        successes += 1

print(round(successes / n, 3))