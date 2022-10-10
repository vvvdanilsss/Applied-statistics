import itertools
import numpy as np

pool = set()
for attempt in itertools.product(np.arange(1, 7), np.arange(1, 5)):
    if attempt.count(1) == 1 or attempt.count(1) == 0:
        pool.add(attempt)
print(len(pool))