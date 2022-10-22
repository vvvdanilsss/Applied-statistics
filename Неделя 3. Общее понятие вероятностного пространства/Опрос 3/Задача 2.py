from numpy.random import choice
from numpy import unique

n, p, k = 3, 0.9, 5
iterator = 1000000
successes = 0

for _ in range(iterator):
    hit_or_not = list(choice([1, 0], n, p=[p, 1 - p]))
    compartments = list(choice(list(range(1, k + 1)), n))
    result = [hit_or_not[_] * compartments[_] for _ in range(n)]
    if result.count(0) == 1 and len(unique(result)) == n or result.count(0) == 0 and len(unique(result)) >= n - 1:
        successes += 1

print(round(successes / iterator, 3))