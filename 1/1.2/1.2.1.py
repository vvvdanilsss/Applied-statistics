import itertools

tetra = list(range(1, 5))
pool = set(itertools.product(tetra, tetra))
print(len(pool))