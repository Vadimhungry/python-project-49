import random
QUERY = 'What number is missing in the progression?'


def init_game():
    step = random.randint(1, 9)
    length = random.randint(5, 10) * step
    progression = list(range(1, length, step))
    answer = random.choice(progression)

    x_position = progression.index(answer)
    progression[x_position] = '..'
    stringed_prog = list(map(str, progression))
    print(f'Question: {stringed_prog}')

    return answer
