import itertools

tetra = list(range(1, 5))
pool = set()

for _ in itertools.product(tetra, tetra):
    if sum(_) == 7:
        pool.add(_)

print(len(pool))