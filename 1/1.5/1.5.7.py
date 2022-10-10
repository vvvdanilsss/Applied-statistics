import itertools
import numpy as np
from numpy.lib.arraysetops import unique


pool = set()
for adult, kid in itertools.product(itertools.combinations_with_replacement(
        np.arange(1, 7), 2), itertools.combinations_with_replacement(
            np.arange(1, 12), 3)):
    if len(unique(adult)) == 2 and len(unique(kid)) == 3:
        pool.add((adult, kid))
print(len(pool))