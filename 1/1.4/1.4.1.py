import itertools

cube = set(range(1, 7))
pool = set(itertools.product(cube, cube))
successful = 0
for _ in pool:
    if sum(_) == 8:
        successful += 1
print(round(successful / len(pool), 3))
