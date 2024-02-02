import random
from brain_games.const import PROGRESSION_PROMT
from brain_games.engine import run_game


def do_rand() -> tuple:
    """
    Function returned tuple:
        result - random math progression
        miss_position - position of miss numder in progression
        miss_num - random numder for question
    """

    length = random.randint(5, 10)
    step = random.randint(1, 7)
    start = random.randint(0, 50)
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

    run_game(get_question_and_answer, PROGRESSION_PROMT)
