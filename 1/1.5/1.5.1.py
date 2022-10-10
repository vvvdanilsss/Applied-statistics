import itertools

letters = set(['A', 'B', 'C'])
numbers = set(range(1, 100))
pool = set(itertools.product(letters, numbers))
print(len(pool))