import itertools

guards = set(range(1, 5))
pool = set()
for _ in itertools.product(*[guards] * 4):
    if len(set(_)) == 4:
        pool.add(_)
print((len(pool)))