from itertools import product
from numpy.random import choice
from numpy import mean

values_eta = [4, 6]  # Индексы таблицы по горизонтали
values_xi = [168, 170, 172, 174]  # Индексы таблицы по вертикали
probabilities_eta_and_xi = [0.02, 0.13, 0.11, 0.04,
                            0.04, 0.29, 0.11, 0.26]  # Сама таблица
i = 2  # Количество горизонтальных индексов
j = 4  # Количество вертикальных индексов
table_indexes = list(product(*[range(i)], *[range(j)]))  # Список кортежей из всех индексов ij таблицы
marginal_distribution_eta = [0] * i
marginal_distribution_xi = [0] * j
product_list = []
n = 200000000  # Будет долго выполнятся, зато хорошая точность

for _ in range(n):
    index = choice(list(range(len(table_indexes))),
                   p=probabilities_eta_and_xi)  # Рандомно выбираем пару индексов ij с определенной вероятностью
    product_list.append(values_eta[table_indexes[index][0]]
                        * values_xi[
                            table_indexes[index][1]])  # Собираем список большого количества произведений эты на кси
    marginal_distribution_eta[table_indexes[index][0]] += 1  # Собираем список вероятностей отдельно для эты
    marginal_distribution_xi[table_indexes[index][1]] += 1  # Аналогично для кси

for _ in range(i):
    marginal_distribution_eta[_] = round(float(marginal_distribution_eta[_]) / n,
                                         3)  # Округляем чтобы в дальнейшем сумма вероятностей была Неделя 1. Простейшая теория вероятностей
for _ in range(j):
    marginal_distribution_xi[_] = round(float(marginal_distribution_xi[_]) / n, 3)  # Аналогично для кси

print(f'marginal_distribution_eta: {dict(zip(values_eta, marginal_distribution_eta))}')
print(f'marginal_distribution_xi: {dict(zip(values_xi, marginal_distribution_xi))}')

expected_value = mean(product_list)  # Математическое ожидание произведения эты на кси
print(f'expected_value = {round(expected_value, 3)}')

expected_value_eta = mean(choice(values_eta, n, p=marginal_distribution_eta))  # Математическое ожидание значения эты
print(f'expected_value_eta = {round(expected_value_eta, 3)}')
expected_value_xi = mean(choice(values_xi, n, p=marginal_distribution_xi))  # Аналогично для кси
print(f'expected_value_xi = {round(expected_value_xi, 3)}')

pool_eta = choice(values_eta, n,
                  p=marginal_distribution_eta)  # Пул значений эты, полученный рандомно с определенными, вычисленными ранее, вероятностями
pool_xi = choice(values_xi, n, p=marginal_distribution_xi)  # Аналогично для кси

dispersion_eta = mean((pool_eta - mean(pool_eta)) ** 2)
print(f'dispersion_eta = {round(dispersion_eta, 3)}')
dispersion_xi = mean((pool_xi - mean(pool_xi)) ** 2)
print(f'dispersion_xi = {round(dispersion_xi, 3)}')

print(f'cov(eta, xi) = {round(expected_value - expected_value_eta * expected_value_xi, 3)}')
sigma_eta = mean((pool_eta - mean(pool_eta)) ** 2) ** 0.5
sigma_xi = mean((pool_xi - mean(pool_xi)) ** 2) ** 0.5
print(f'p(eta, xi) = {round((expected_value - expected_value_eta * expected_value_xi) / (sigma_eta * sigma_xi), 3)}')