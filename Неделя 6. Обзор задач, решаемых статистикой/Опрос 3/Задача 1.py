import numpy as np
from matplotlib import pyplot as plt
from matplotlib import use
use('TkAgg')

pool = [5, 12, 7, 4, 9, 10, 9, 4, 9, 12]
print(np.mean(pool), np.std(pool) ** 2, np.median(pool))

xi = {x: pool.count(x) / len(pool) for x in set(pool)}
plt.plot(xi.keys(), xi.values())
plt.show()