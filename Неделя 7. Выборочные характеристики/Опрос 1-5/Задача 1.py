import numpy as np

x = [3, 1, 3, 2, 2, 3, 1, 3, 1, 4, 1, 2, 1, 4, 3, 2, 3, 3, 1, 0, 1, 3, 3, 1, 2, 2, 5, 2, 2, 0]
print(x.count(3) / len(x), x.count(4) / len(x))
print(len(list(filter(lambda _: _ > 3, x))) / len(x))
print(x.count(1) / len(x), x.count(3) / len(x))
print(np.mean(x))
print(np.var(x))
print(np.var(x) * len(x) / (len(x) - 1))
print(np.quantile(x, 0.5))
print(np.quantile(x, 0.25))
print(np.quantile(x, 0.75))