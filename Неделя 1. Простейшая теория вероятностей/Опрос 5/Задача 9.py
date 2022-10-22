import itertools
from numpy.lib.arraysetops import unique

pool = set()
word = list('колокол')
letters, counts = unique(word, return_counts=True)
lib = dict(zip(letters, counts))

for _ in itertools.product(*[unique(word)] * 7):
    letters_, counts_ = unique(_, return_counts=True)
    lib_ = dict(zip(letters_, counts_))
    if lib_ == lib:
        pool.add(_)

print(len(pool))