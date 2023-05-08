import random


def find_gcd(a, b):
    # находим наименьший общий делитель
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i
    return gcd


def init_game():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    gcd = find_gcd(a, b)

    print(f'Question: {a} {b}')

    return gcd
