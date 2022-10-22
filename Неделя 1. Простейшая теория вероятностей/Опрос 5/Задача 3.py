import itertools
import numpy as np
from numpy.lib.arraysetops import unique


pool = set()
lessons = 6

for day in itertools.product(*[np.arange(1, 11)] * lessons):
    if len(unique(day)) == lessons:
        pool.add(day)

print(len(pool))