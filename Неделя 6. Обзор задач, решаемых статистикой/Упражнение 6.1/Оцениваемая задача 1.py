import numpy as np

np.random.seed(95)
p, n = 0.66, 96
sample = np.random.binomial(1, p, n)
print(*sample[:5], sep=', ')
print(*sample[-5:], sep=', ')
print(np.mean(sample))