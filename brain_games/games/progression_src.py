import random
from brain_games.const import LENGTH_START, LENGTH_END
from brain_games.const import STEP_FROM, STEP_TO
from brain_games.const import PROG_START, PROG_END


def do_rand() -> tuple:
    """
    Function returned tuple:
        result - random math progression
        miss_position - position of miss numder in progression
        miss_num - random numder for question
    """

    length = random.randint(LENGTH_START, LENGTH_END)
    step = random.randint(STEP_FROM, STEP_TO)
    start = random.randint(PROG_START, PROG_END)
    result = list(range(start, start + step * length, step))
    miss_position = random.randint(0, length - 1)
    miss_num = result[miss_position]

    return result, miss_position, miss_num


def question_list_to_string(list_seq, miss_position) -> str:
    """
    Function for prepare random list to question string
    """

    result = ""
    for elem in enumerate(list_seq):
        if elem[0] == miss_position:
            result += ".. "
        else:
            result += str(elem[1]) + " "
    return result


def get_question_and_answer():
    question_seq, miss_position, true_answer = do_rand()
    question_str = question_list_to_string(question_seq, miss_position)
    return question_str, str(true_answer)


def run_progression_game():

    return get_question_and_answer
