import prompt

ROUNDS_COUNT = 3


def play(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Give three correct answers in a row to win.')
    print(game.QUESTION)

    for i in range(ROUNDS_COUNT):
        # задаем вопрос и сохраняем ответ
        game_data = game.generate_question_and_answer()
        question_expression = game_data['question_expression']
        answer = game_data['answer']
        print(f'Question: {question_expression}')
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
