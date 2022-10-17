from itertools import product
from numpy.random import choice
from math import isclose

list_probabilities = [0.02, 0.02, 0.06, 0.1,
                      0.03, 0.03, 0.09, 0.15,
                      0.02, 0.02, 0.06, 0.1,
                      0.03, 0.03, 0.09, 0.15]
l = 4
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
for i in range(l):
    for j in range(l):
        if not isclose(list_probabilities[list_table_indexes.index((i, j))], \
                       marginal_distribution_eta[i] * marginal_distribution_xi[j]):
            break
    else:
        continue
    break
else:
    print('Независимы')