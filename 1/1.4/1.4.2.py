import itertools
import functools

cube = set(range(1, 7))
pool = set(itertools.product(cube, cube))
successful = 0
for _ in pool:
    if functools.reduce(lambda a, b: a * b == 8, _):
        successful += 1
print(round(successful / len(pool), 3))