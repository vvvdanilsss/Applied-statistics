cube = set(range(1, 9)) #здесь кубик 8-гранный, если сделать range(1, 8) - будет 7-гранный
k = 1/sum(cube) #это число k
print(round(k, 3))
P3 = sum([k * i for i in range(1, 3)])#это вероятность события: "выпало меньше 3", усли сделать range(1, 4) - будет вероятность события: "выпало меньше 4"
print(round(P3, 3))