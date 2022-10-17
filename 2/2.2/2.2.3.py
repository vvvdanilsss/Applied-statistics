from itertools import product
from numpy.random import choice

list_probabilities = [0.2, 0.2, 0,
                      0.1, 0.05, 0.05,
                      0.05, 0.1, 0.25]
l = 3
list_table_indexes = list(product(*[range(l)], *[range(l)]))
marginal_distribution_eta = [0] * l
marginal_distribution_xi = [0] * l
n = 100000
for _ in range(n):
    index = choice(list(range(len(list_table_indexes))), p=list_probabilities)
    marginal_distribution_eta[list_table_indexes[index][0]] += 1
    marginal_distribution_xi[list_table_indexes[index][1]] += 1
for _ in range(l):
    marginal_distribution_eta[_] = round(float(marginal_distribution_eta[_]) / n, 2)
    marginal_distribution_xi[_] = round(float(marginal_distribution_xi[_]) / n, 2)
values_eta = [3, 5, 7]
values_xi = [-1, -2, 5]
print(f'eta: {dict(zip(values_eta, marginal_distribution_eta))}',
      f'xi: {dict(zip(values_xi, marginal_distribution_xi))}', sep='\n')