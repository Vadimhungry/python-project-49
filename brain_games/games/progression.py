import random
QUERY = 'What number is missing in the progression?'


def init_game():
    step = random.randint(1, 9)
    length = random.randint(5, 10)
    progression = [random.randint(1, 100)]
    for i in range(1, length):
        progression.append(progression[i - 1] + step)

    answer = random.choice(progression)

    x_position = progression.index(answer)
    progression[x_position] = '..'

    for i in range(len(progression)):
        progression[i] = str(progression[i])
    sringed_prog = ' '.join(progression)

    print(f'Question: {sringed_prog}')

    return answer
