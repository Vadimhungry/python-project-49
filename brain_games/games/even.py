#!/usr/bin/env python3
import random

def game():

    # формируем случайное число и верный ответ
    num = random.randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'

    # задаем вопрос
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {num}')
    return answer



