import itertools

pool = list(
    zip(map(sum, list(itertools.product(*[[0, 1]] * 3))), map(sum, list(itertools.product(*[[0, 1]] * 3))[::-1])))
# print(pool.count((0, 3)) / len(pool))
# 0.125
# print(pool.count((1, 2)) / len(pool))
# 0.375
# print(pool.count((2, 1)) / len(pool))
# P
print(pool.count((3, 0)) / len(pool))