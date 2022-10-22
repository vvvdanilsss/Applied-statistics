def grade(score):
    if score < 60:
        return 'неудовлетворительно'
    elif score <= 74:
        return 'удовлетворительно'
    elif score <= 90:
        return 'хорошо'
    else:
        return 'отлично'