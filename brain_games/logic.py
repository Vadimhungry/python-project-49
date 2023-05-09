import prompt

ROUNDS_COUNT = 3


def play(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Give three correct answers in a row to win.')
    print(game.QUERY)
    # print(QUERY)
    for i in range(ROUNDS_COUNT):
        # задаем вопрос и сохраняем ответ
        answer = str(game.init_game())

        # принимаем ответ
        user_answer = prompt.string('Your answer: ')

        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(")
            print(f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
