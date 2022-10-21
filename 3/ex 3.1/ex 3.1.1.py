from numpy.random import uniform

n = 1000000
tank = list(uniform(0, 56, n))  # формируем нашу емкость 56 тонн
tank_gasoline_1 = list(filter(lambda x: x < 48, tank))  # оставляем только меньше 48
print(f'меньше 48: вероятность = {round(len(tank_gasoline_1) / n, 3)}')
tank_gasoline_2 = list(filter(lambda x: 37 <= x <= 42, tank))  # оставляем только не меньше 37 и не больше 42
print(f'не меньше 37 и не больше 42: вероятность = {round(len(tank_gasoline_2) / n, 3)}')
