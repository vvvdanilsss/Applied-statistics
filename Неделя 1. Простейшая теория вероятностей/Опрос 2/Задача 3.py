import itertools
import functools

tetra = list(range(1, 5))
pool = set()

for _ in itertools.product(tetra, tetra):
    if functools.reduce(lambda a, b: a * b % 3 == 0, _):
        pool.add(_)

print(len(pool))