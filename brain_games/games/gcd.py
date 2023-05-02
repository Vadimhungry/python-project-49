#!/usr/bin/env python3
import random


def game():
    # формируем два случайных числа
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    # находим наименьший общий делитель
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i

    # задаем вопрос
    print('Find the greatest common divisor of given numbers.')
    print(f'Question: {a} {b}')


    return gcd

