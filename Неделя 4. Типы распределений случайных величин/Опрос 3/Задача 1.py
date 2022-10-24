from numpy.random import uniform
from numpy import zeros, round

iterator = 10000000
pool = uniform(0, 5, iterator)
successes = zeros(3)

for x in pool:
    if x < 2:
        successes[0] += 1
    elif x > 4:
        successes[1] += 1
    else:
        successes[2] += 1

print(round(successes / iterator, 3))