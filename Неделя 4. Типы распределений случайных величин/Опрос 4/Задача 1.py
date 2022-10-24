from numpy.random import uniform


def fxy(x, y):
    if a_x <= x <= b_x and a_y <= y <= b_y:
        return 1 / ((b_x - a_x) * (b_y - a_y))
    else:
        return 0


def fx(x):
    if a_x <= x <= b_x:
        return 1 / (b_x - a_x)
    else:
        return 0


def fy(y):
    if a_y <= y <= b_y:
        return 1 / (b_y - a_y)
    else:
        return 0


a_x, a_y, b_x, b_y = 1, 2, 3, 4
x1, y1, x2, y2 = 0, 0, 2, 3
print(fxy(x1, y1), fxy(x2, y2))
print(fx(x1), fx(x2))
print(fy(y1), fy(y2))

iterator = 10000000
pool_x = uniform(a_x, b_x, iterator)
pool_y = uniform(a_y, b_y, iterator)
successes = 0

for _ in range(iterator):
    if 2 < pool_x[_] < 3 and 1 <= pool_y[_] <= 3:
        successes += 1

print(round(successes / iterator, 3))