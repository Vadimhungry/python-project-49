#!/usr/bin/env python3
import random


def game():
    # формирует два случайных числа
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    # проводим на числах случайную операцию
    sign = random.randint(0, 2)
    signs = ['+', '-', '*']
    print('What is the result of the expression?')
    print(f'Question: {num1} {signs[sign]} {num2}')
    if sign == 0:
        return num1 + num2
    elif sign == 1:
        return num1 - num2
    else:
        return num1 * num2
