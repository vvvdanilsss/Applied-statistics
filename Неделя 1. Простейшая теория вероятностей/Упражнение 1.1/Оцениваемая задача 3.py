cube = set(range(1,
                 9))  # Здесь кубик 8-гранный, если сделать range(Неделя 1. Простейшая теория вероятностей, 8) - будет 7-гранный
k = 1 / sum(cube)  # Это число k
print(round(k, 3))
P3 = sum([k * i for i in range(1,
                               3)])  # Это вероятность события: "выпало меньше Неделя 3. Общее понятие вероятностного пространства", усли сделать range(Неделя 1. Простейшая теория вероятностей, 4) - будет вероятность события: "выпало меньше 4"
print(round(P3, 3))
