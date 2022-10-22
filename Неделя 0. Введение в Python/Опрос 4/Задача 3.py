def get_sum_odd(a, b):
    if a % 2 == 0:
        return sum(range(a + 1, b + 1, 2))
    else:
        return sum(range(a, b + 1, 2))