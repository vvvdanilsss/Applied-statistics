import itertools

cube = set(range(1, 13))
k = 5
pool = set(itertools.product(*[cube] * k))
print(len(pool) + len(cube))