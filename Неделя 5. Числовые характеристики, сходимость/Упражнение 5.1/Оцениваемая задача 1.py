from decimal import Decimal

xi = [-10, 2, 6, 10]  # Значения кси
p_xi = [0.1, 0.05, 0.2, 0.65]  # Вероятности кси
# Генерирую список значений эты. Decimal нужен поскольку числа в 12 степени не помещаются в int
eta = [Decimal(5 * (xi_value ** 12) + 4) for xi_value in xi]
eta_answer = list(set(eta))  # Список уникальных значений эты
p_eta_answer = []

for i, x in enumerate(eta_answer):
    if eta.count(x) > 1:  # Есть ли повторения значений эты
        p = 0
        for j, y in enumerate(eta[i:]):  # Прохожусь по всем повторениям
            if y == x:
                p += p_xi[i + j]  # Суммирую их вероятности
        p_eta_answer.append(p)
    else:
        p_eta_answer.append(p_xi[eta.index(x)])

eta_table = dict(sorted(zip(eta_answer, p_eta_answer)))
eta_answer = [str(value) for value in eta_table.keys()]
p_eta_answer = [str(value) for value in eta_table.values()]
print(f'5 * xi ** 12 + 4: {" | ".join(eta_answer)}')
print(f'P: {" | ".join(p_eta_answer)}')
