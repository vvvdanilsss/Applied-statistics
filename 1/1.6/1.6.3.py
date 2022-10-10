from numpy import random

n = 10000000
successes = 0
for _ in range(n):
    balls = [0] * 7 + [1] * 5
    ball1 = balls.pop(random.randint(len(balls)))
    ball2 = balls[random.randint(len(balls))]
    if ball1 != ball2:
        successes += 1
print(round(successes / n, 3))