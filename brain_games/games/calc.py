import random
QUERY = 'What is the result of the expression?'


def init_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    sign = random.choice(['+', '-', '*'])

    if sign == '+':
        answer = num1 + num2
    if sign == '-':
        answer = num1 - num2
    if sign == '*':
        answer = num1 * num2
    return {'answer': answer,
            'question_expression': f'{num1} {sign} {num2}'}
