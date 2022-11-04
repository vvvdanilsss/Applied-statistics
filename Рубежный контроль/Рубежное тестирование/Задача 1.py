k = 1 / sum([3 * i - 1 for i in range(1, 9)])
print(k)
p = [k * (3 * i - 1) for i in range(1, 9)]
a = p[4] + p[3] + p[2] + p[7]
print(a)