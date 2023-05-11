import random

QUERY = 'Answer "yes" if the number is even, otherwise answer "no".'


def init_game():

    num = random.randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'

    return {'answer': answer,
            'question_expression': str(num)}
