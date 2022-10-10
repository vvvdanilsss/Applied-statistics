import itertools

pool = set()
[pool.add(_) for _ in itertools.product(*[['.', '-']] * 5)]
print(len(pool))
