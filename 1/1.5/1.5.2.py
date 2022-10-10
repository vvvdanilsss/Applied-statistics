import itertools

numbers1 = set(range(1, 27))
numbers2 = set(range(10))
pool = set(itertools.product(*[numbers1] * 2, *[numbers2] * 3))
print(len(pool))