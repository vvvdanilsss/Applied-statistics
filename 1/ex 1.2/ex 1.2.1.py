import itertools

blouses = set(range(1, 9))
skirts = set(range(1, 6))
shoes = set(range(1, 4))
pool = set(itertools.product(blouses, skirts, shoes))
print((len(pool)))