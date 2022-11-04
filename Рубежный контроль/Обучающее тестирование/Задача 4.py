values_eta = [-1, 1]
values_xi = [1, 2]
table = [0.5, 0.25, 0.25, 0]
marginal_eta = [0.75, 0.25]
marginal_xi = [0.75, 0.25]

mean_eta = sum([values_eta[_] * marginal_eta[_] for _ in range(2)])
mean_xi = sum([values_xi[_] * marginal_xi[_] for _ in range(2)])
print(f'mean_eta = {mean_eta}')
print(f'mean_xi = {mean_xi}')

mean_eta2 = sum([values_eta[_] ** 2 * marginal_eta[_] for _ in range(2)])
dispersion_eta = mean_eta2 - mean_eta ** 2
print(f'dispersion_eta = {dispersion_eta}')

mean_eta_xi = values_eta[0] * values_xi[0] * table[0] + values_eta[0] * \
              values_xi[1] * table[1] + values_eta[1] * values_xi[0] * \
              table[2] + values_eta[1] * values_xi[1] * table[3]
cov_eta_xi = mean_eta_xi - mean_eta * mean_xi
print(f'cov_eta_xi = {cov_eta_xi}')