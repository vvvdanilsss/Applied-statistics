import itertools
from numpy.lib.arraysetops import unique

cards = [1, 2, 3, 4, 5]
pool = set()

for _ in itertools.product(cards, cards):
    if len(unique(_)) == 2:
        pool.add(_)

print(len(pool))
