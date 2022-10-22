import itertools
import numpy as np
from numpy.lib.arraysetops import unique

pool = set()

for permutation in itertools.product(*[np.arange(1, 6)] * 5):
    if len(unique(permutation)) == 5:
        index1 = permutation.index(1)
        index2 = permutation.index(2)
        if abs(index1 - index2) == 1:
            pool.add(permutation)

print(len(pool))