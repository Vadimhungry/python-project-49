import random
QUESTION = 'What number is missing in the progression?'


def generate_question_and_answer():
    step = random.randint(1, 9)
    length = random.randint(5, 10) * step
    progression = list(range(1, length, step))

    answer_index = random.randint(0, len(progression) - 1)
    answer = progression[answer_index]

    progression[answer_index] = '..'
    prog_list_of_strings = list(map(str, progression))
    prog_for_question = ' '.join(prog_list_of_strings)

    return str(answer), f'{prog_for_question}'
