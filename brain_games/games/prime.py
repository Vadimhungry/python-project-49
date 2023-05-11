import random
QUESTION = 'Answer "yes" if given number is prime.' \
           ' Otherwise answer "no".'

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            return False
    else:
        return True


def generate_question_and_answer():
    num = random.randint(1, 100)

    answer = 'yes' if is_prime(num) else 'no'
    return {'answer': answer,
            'question_expression': f'{num}'}
