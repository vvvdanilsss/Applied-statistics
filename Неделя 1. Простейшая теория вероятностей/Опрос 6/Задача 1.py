from numpy import random

n = 1000000
successes = 0
balls = [0] * 6 + [1] * 5

for _ in range(n):
    ball = balls[random.randint(len(balls))]
    if ball == 0:
        successes += 1

print(round(successes / n, 3))
