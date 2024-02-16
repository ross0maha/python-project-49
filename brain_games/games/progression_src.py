import random

LENGTH_START = 5
LENGTH_END = 10
STEP_FROM = 1
STEP_TO = 7
PROG_START = 1
PROG_END = 50

PROGRESSION_PROMT = 'What number is missing in the progression?'


def generate_question_progression(progression_start,
                                  progression_diff,
                                  progression_length):

    question_progression = list(range(progression_start, progression_start
                                      + progression_diff * progression_length,
                                      progression_diff))
    return question_progression


def to_string(progression, hidden_term_index):
    result = list(map(lambda x: str(x), progression))
    result[hidden_term_index] = ".."
    result = " ".join(result)

    return result


def get_question_and_answer():
    progression_length = random.randint(LENGTH_START, LENGTH_END)
    progression_diff = random.randint(STEP_FROM, STEP_TO)
    progression_start = random.randint(PROG_START, PROG_END)
    hidden_term_index = random.randint(0, progression_length - 1)

    question_seq = generate_question_progression(progression_start,
                                                 progression_diff,
                                                 progression_length)

    question_prog_str = to_string(question_seq.copy(), hidden_term_index)
    true_answer = question_seq[hidden_term_index]

    return question_prog_str, str(true_answer)
