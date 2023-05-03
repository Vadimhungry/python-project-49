#!/usr/bin/env python3
import random


def game():
    # формируем прогрессию длиной от 5 до 10 чисел
    step = random.randint(1, 9)
    length = random.randint(5, 10)
    progression = [random.randint(1, 100)]
    for i in range(1, length):
        progression.append(progression[i - 1] + step)

    # выбираем число для ответа
    answer = random.choice(progression)

    # скрываем выбранное число
    x_position = progression.index(answer)
    progression[x_position] = '..'

    # преобразуем элементы в строки
    for i in range(len(progression)):
        progression[i] = str(progression[i])
    sringed_prog = ' '.join(progression)

    # показываем прогрессию без случайного элемента
    print('What number is missing in the progression?')
    print(f'Question: {sringed_prog}')

    return answer
