import itertools
import numpy as np
from numpy.lib.arraysetops import unique


pool = set()
min_mans = 8
for quorum in itertools.combinations_with_replacement(np.arange(1, 13), min_mans):
    if len(unique(quorum)) == min_mans:
        pool.add(quorum)
print(len(pool))