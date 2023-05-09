import random
QUERY = 'What number is missing in the progression?'


def init_game():
    step = random.randint(1, 9)
    length = random.randint(5, 10) * step
    progression = list(range(1, length, step))
    answer = random.choice(progression)

    x_position = progression.index(answer)
    progression[x_position] = '..'

    for i in range(len(progression)):
        progression[i] = str(progression[i])
    sringed_prog = ' '.join(progression)

    print(f'Question: {sringed_prog}')

    return answer
