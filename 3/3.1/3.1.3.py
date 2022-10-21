from numpy.random import uniform

n = 10000000
points = list(uniform(0, 5, (2, n)))
points_sorted = list(map(sorted, zip(points[0], points[1])))
points_sorted_filter = list(filter(lambda x: 5 < 2 * x[1] < 5 + 2 * x[0] and 5 > 2 * x[0], points_sorted))
print(round(len(points_sorted_filter) / len(points_sorted), 3))