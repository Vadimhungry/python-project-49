#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.brain_games_start import main

# приветствуем юзера и сохраняем имя
name = main()
print('Give three correct answers in a row to win.')

for i in range(3):
    # формируем случайное число и верный ответ
    random_num = random.randint(1, 100)
    correct_answer = 'yes' if random_num % 2 == 0 else 'no'

    # задаем вопрос
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f'Question: {random_num}')

    # принимаем и проверяем ответ
    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
    else:
        break


if i == 2:
    print(f"Congratulations, {name}!")
else:
    print(f"'{user_answer}' is wrong answer ;(")
    print(f"Correct answer was '{correct_answer}'")
    print(f"Let's try again, {name}!")
