variance_xi1, variance_xi2 = 5.5, 11.3  # Дисперсии кси1 и кси2
coefficient_xi1, coefficient_xi2 = 8, 12.5  # Коэффициенты перед уси1 и кси2
variance_xi1_plus_xi2 = coefficient_xi1 ** 2 * variance_xi1 + coefficient_xi2 ** 2 * variance_xi2
print(variance_xi1_plus_xi2)