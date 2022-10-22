import itertools
import numpy as np
from numpy.lib.arraysetops import unique


pool = set()

for chairman, quorum in itertools.product(
        np.arange(1, 13), itertools.combinations_with_replacement(
            np.arange(1, 12), 7)):
    if len(unique(quorum)) == 7:
        pool.add((chairman, quorum))

print(len(pool))