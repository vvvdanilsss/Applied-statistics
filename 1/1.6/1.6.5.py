import itertools
from numpy.lib.arraysetops import unique

word = 'банан'
word_list = list(word)
letters, counts = unique(word_list, return_counts=True)
lib = dict(zip(letters, counts))
count, successes = 0, 0
for _ in itertools.product(*[unique(word_list)] * len(word_list)):
    letters_, counts_ = unique(_, return_counts=True)
    lib_ = dict(zip(letters_, counts_))
    word_ = ''.join(_)
    if lib_ == lib:
        count += 1
        if word_ == word:
            successes += 1
print(round(successes/count, 3))