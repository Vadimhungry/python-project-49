#!/usr/bin/env python3
import prompt

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Give three correct answers in a row to win.')
    return name

def play(game):
    # приветствуем юзера и сохраняем имя
    name = welcome_user()

    for i in range(3):
        # задаем вопрос и сохраняем ответ
        answer = str(game())

        # принимаем ответ
        user_answer = prompt.string('Your answer: ')


        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(")
            print(f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            break
    else:
        print('Correct!')
        print(f"Congratulations, {name}!")


