import random
QUERY = 'What number is missing in the progression?'


def generate_question_and_answer():
    step = random.randint(1, 9)
    length = random.randint(5, 10) * step
    progression = list(range(1, length, step))
    answer = random.choice(progression)

    x_position = progression.index(answer)
    progression[x_position] = '..'
    prog_list_of_strings = list(map(str, progression))
    prog_for_question = ' '.join(prog_list_of_strings)

    return {'answer': str(answer),
            'question_expression': f'{prog_for_question}'}
