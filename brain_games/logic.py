#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt


def logic(game):
    # приветствуем юзера и сохраняем имя
    name = welcome_user()

    for i in range(3):
        # задаем вопрос и сохраняем ответ
        answer = str(game())

        # принимаем ответ
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
        else:
            break

    if i == 2:
        print(f"Congratulations, {name}!")
    else:
        print(f"'{user_answer}' is wrong answer ;(")
        print(f"Correct answer was '{answer}'")
        print(f"Let's try again, {name}!")
