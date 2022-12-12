pool = [5, 12, 7, 4, 9, 10, 9, 4, 9, 12]
xi = {x: pool.count(x) / len(pool) for x in set(pool)}
print(xi)