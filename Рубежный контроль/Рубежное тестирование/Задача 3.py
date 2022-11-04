from numpy.random import choice

cont1 = [1] * 8 + [0] * 5
cont2 = [1] * 9 + [0] * 5
n = 1000000
suc = 0

for _ in range(n):
    cont3 = [choice(cont1), choice(cont2)]
    if choice(cont3) == 1:
        suc += 1

print(suc / n)

cont1 = [11] * 8 + [0] * 5
cont2 = [21] * 9 + [0] * 5
n = 1000000
suc = 0

for _ in range(n):
    while True:
        cont3 = [choice(cont1), choice(cont2)]
        shar = choice(cont3)
        if shar == 11 or shar == 21:
            break
    if shar == 21:
        suc += 1

print(suc / n)