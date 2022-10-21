from numpy.random import uniform

n = 10000000
numbers = list(uniform(0, 11, (2, n)))  # формируем список из двух списков значений для x и y
good_numbers = list(filter(lambda x: x[0] * x[1] <= 7 and x[1] / x[0] <= 121 / 7,
                           zip(numbers[0], numbers[1])))  # zip создает пары значений x и y и подает их функции filter
print(round(len(good_numbers) / n, 3))
