#!/usr/bin/env python3
import random


def game():
    num = random.randint(1, 100)
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    print(f'Question: {num}')

    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return 'yes'
    else:
        return 'no'
