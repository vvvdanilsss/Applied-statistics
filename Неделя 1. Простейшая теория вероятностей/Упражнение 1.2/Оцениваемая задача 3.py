import itertools

letters = set(range(14))
numbers = set(range(10))
pool = set(itertools.product(*[letters] * 2, *[numbers] * 5))
print(len(pool))