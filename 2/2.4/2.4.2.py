from itertools import product
from numpy.random import choice
from numpy import mean

eta_values = [2, 3, 5, 10]
xi_values = [-4, -2, 0, 3]
probabilities_list = [0.02, 0.02, 0.06, 0.1,
                      0.03, 0.03, 0.09, 0.15,
                      0.02, 0.02, 0.06, 0.1,
                      0.03, 0.03, 0.09, 0.15]
l = 4
table_indexes_list = list(product(*[range(l)], *[range(l)]))
product_list = []
n = 1000000
for _ in range(n):
    index = choice(list(range(l ** 2)), p=probabilities_list)
    product_list.append(eta_values[table_indexes_list[index][0]]
                        * xi_values[table_indexes_list[index][1]])
print(f'expected value = {round(mean(product_list), 3)}')