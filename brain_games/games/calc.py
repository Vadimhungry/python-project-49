import random
QUERY = 'What is the result of the expression?'


def init_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    sign = random.choice(['+', '-', '*'])
    print(f'Question: {num1} {sign} {num2}')
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    else:
        return num1 * num2
