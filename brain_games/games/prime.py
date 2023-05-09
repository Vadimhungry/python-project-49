import random
QUERY = 'Answer "yes" if given number is prime.' \
        ' Otherwise answer "no".'


def is_prime(num):

    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            return False
    else:
        return True


def init_game():
    num = random.randint(1, 100)
    print(f'Question: {num}')

    return 'yes' if is_prime(num) else 'no'
