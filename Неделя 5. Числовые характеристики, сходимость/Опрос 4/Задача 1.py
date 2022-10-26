xi = [-1, 0, 1, 2]
p = [1 / 5, 1 / 10, 3 / 10, 2 / 5]
eta = [value_xi ** 2 - 2 for value_xi in xi]
mean_eta = sum([eta[i] * p[i] for i in range(len(xi))])
mean_eta2 = sum([eta[i] ** 2 * p[i] for i in range(len(xi))])
print(round(mean_eta2 - mean_eta ** 2, 3))