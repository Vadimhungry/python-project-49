import random

QUERY = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    # находим наименьший общий делитель
    temp = b if a > b else a
    i = 1
    while i <= temp:
        if ((a % i == 0) and (b % i == 0)):
            gcd = i

        i += 1
    return gcd


def generate_question_and_answer():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    answer = find_gcd(a, b)

    return {'answer': str(answer),
            'question_expression': f'{a} {b}'}
