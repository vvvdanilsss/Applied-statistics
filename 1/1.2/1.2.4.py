import itertools
import functools

tetra = list(range(1, 5))
pool = set(itertools.product(tetra, tetra))
pool1 = set()
for _ in pool:
    if sum(_) == 7:
        pool1.add(_)
print(pool1)
pool2 = set()
for _ in pool:
    if functools.reduce(lambda a, b: a * b % 3 == 0, _):
        pool2.add(_)
print(pool2)