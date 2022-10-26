import numpy as np

xi = np.array((-1, 0, 1, 2))
p_xi = [1 / 5, 1 / 10, 3 / 10, 2 / 5]
eta = list(xi ** 2 - 2)
eta_answer = list(set(eta))
p_eta_answer = []

for i, x in enumerate(eta_answer):
    if eta.count(x) > 1:
        p = p_xi[eta.index(x)]
        for j, y in enumerate(eta[i:]):
            if y == x:
                p += p_xi[i + j]
        p_eta_answer.append(p)
    else:
        p_eta_answer.append(p_xi[eta.index(x)])

print(dict(sorted(zip(eta_answer, p_eta_answer))))