from numpy.random import choice

probabilities = [0.29, 0.01, 0.22, 0.06, 0.3, 0.01]  # Вероятности, что в комнате probabilities[index] опустится потолок
iterator = 1000000
successes = 0
n = 6  # Количество комнат

for _ in range(iterator):
    result = [True] * n  # Сначала во всех комнатах потолки нормальные
    for index in range(0, n, 2):
        # Оставляю потолок нетронутым, либо опускаю его в комнате с нечетным индексом с вероятностью probabilities[index]
        result[index] = choice([True, False], p=[1 - probabilities[index], probabilities[index]])
        # Оставляю потолок нетронутым, либо опускаю его в комнате с четным индексом с вероятностью probabilities[index + 1]
        result[index + 1] = choice([True, False], p=[1 - probabilities[index + 1], probabilities[index + 1]])
        # Если в комнатах расположенных "параллельно" потолки опущены, прерываю цикл
        if result[index] == result[index + 1] == False:
            break
    else:  # Если цикл не прервался, значит можно прийти через комнаты. Засчитываю это как успех
        successes += 1

print(round(successes / iterator, 3))  # Делю количество успешных попыток пройти через комнаты, на количество всех попыток
