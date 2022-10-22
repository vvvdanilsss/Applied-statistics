from numpy.random import choice

dice = list(range(1, 7))  # Игральная кость
iterator = 1000000
successes = 0

for _ in range(iterator):
    attempt = []
    # Бросаю кости пока не встретим хотя бы одну 1 по условию "выпала как минимум одна 1"
    while attempt.count(1) < 1:
        attempt = list(choice(dice, 8))
    # Проверяю по условию задачи "как минимум две 1 после 8 бросков"
    if attempt.count(1) > 1:
        successes += 1  # Если условие выполняется, зачитываю как успешную попытку

print(round(successes / iterator, 3))