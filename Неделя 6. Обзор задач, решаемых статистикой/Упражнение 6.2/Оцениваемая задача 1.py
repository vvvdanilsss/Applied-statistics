import numpy as np
from matplotlib import pyplot as plt
from matplotlib import use
use('TkAgg')

pool = [5, 6, 2, 5, 5, 4, 1, 1, 3, 5, 2, 4]
xi = {x: round(pool.count(x) / len(pool), 6) for x in set(pool)}
print(xi)
print(round(np.mean(pool), 3), round(np.var(pool), 3), round(np.std(pool), 3), round(np.median(pool), 3))
plt.plot(xi.keys(), xi.values())
plt.show()