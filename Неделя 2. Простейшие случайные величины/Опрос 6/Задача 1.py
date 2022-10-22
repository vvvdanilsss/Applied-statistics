import numpy as np

probability, attempts, iterator = 0.75, 10, 1000000
marginal = np.zeros(11)

for _ in range(iterator):
    result = sum(np.random.choice([1, 0], attempts, p=[probability, 1 - probability]))
    marginal[result] += 1

marginal /= iterator
pool = np.random.choice(list(range(len(marginal))), iterator, p=marginal)
expected_value = np.mean(pool)
dispersion = np.mean((pool - expected_value) ** 2)
print(f'expected_value = {round(expected_value, 3)}',
      f'dispersion = {round(dispersion, 3)}', sep='\n')