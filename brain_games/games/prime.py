import random
QUERY = 'Answer "yes" if given number is prime.' \
        ' Otherwise answer "no".'


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False


def init_game():
    num = random.randint(1, 100)
    print(f'Question: {num}')

    return 'yes' if is_prime(num) else 'no'
