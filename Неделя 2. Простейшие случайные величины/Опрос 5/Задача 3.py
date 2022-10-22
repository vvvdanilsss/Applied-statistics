from itertools import product
from numpy.random import choice
from numpy import mean

eta_values = [-1, 1, 4]
xi_values = [2, 3, 5]
probabilities_eta_and_xi = [0.1, 0.3, 0.2,
                            0.1, 0.05, 0,
                            0, 0.15, 0.1]
l = 3
table_indexes = list(product(*[range(l)], *[range(l)]))
marginal_distribution_eta = [0] * l
marginal_distribution_xi = [0] * l
product_list = []
n = 1000000

for _ in range(n):
    index = choice(list(range(len(table_indexes))), p=probabilities_eta_and_xi)
    product_list.append(eta_values[table_indexes[index][0]]
                        * xi_values[table_indexes[index][1]])
    marginal_distribution_eta[table_indexes[index][0]] += 1
    marginal_distribution_xi[table_indexes[index][1]] += 1

for _ in range(l):
    marginal_distribution_eta[_] = round(float(marginal_distribution_eta[_]) / n, 3)
    marginal_distribution_xi[_] = round(float(marginal_distribution_xi[_]) / n, 3)

expected_value = mean(product_list)
expected_value_eta = mean(choice(eta_values, n, p=marginal_distribution_eta))
expected_value_xi = mean(choice(xi_values, n, p=marginal_distribution_xi))

pool_eta = choice(eta_values, n, p=marginal_distribution_eta)
pool_xi = choice(xi_values, n, p=marginal_distribution_xi)

sigma_eta = mean((pool_eta - mean(pool_eta)) ** 2) ** 0.5
sigma_xi = mean((pool_xi - mean(pool_xi)) ** 2) ** 0.5

print(f'cov(eta, xi) = {round(expected_value - expected_value_eta * expected_value_xi, 3)}')
print(f'p(eta, xi) = {round((expected_value - expected_value_eta * expected_value_xi) / (sigma_eta * sigma_xi), 3)}')