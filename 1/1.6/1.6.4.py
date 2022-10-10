from numpy import random
from numpy.lib.arraysetops import unique

n = 100000
successes = 0
for _ in range(n):
    cards = []
    while len(unique(cards)) != 4:
        cards.append(random.randint(52))
        count = 0
    for card in unique(cards):
        if card < 26:
            count += 1
    if count == 1 or count == 3:
        successes += 1
print(round(successes / n, 3))