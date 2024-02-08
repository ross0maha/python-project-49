import random
from brain_games.const import LENGTH_START, LENGTH_END
from brain_games.const import STEP_FROM, STEP_TO
from brain_games.const import PROG_START, PROG_END


def generate_question_string(string_lenght, string_step, string_start):

    question_string = list(range(string_start, string_start + string_step
                                 * string_lenght, string_step))

    return question_string


def question_list_to_string(list_seq, position):

    result = list(map(lambda x: str(x), list_seq))
    result[position] = ".."
    result = " ".join(result)

    return result


def get_question_and_answer():
    question_string_length = random.randint(LENGTH_START, LENGTH_END)
    question_string_step = random.randint(STEP_FROM, STEP_TO)
    question_string_start = random.randint(PROG_START, PROG_END)
    miss_position = random.randint(0, question_string_length - 1)

    question_seq = generate_question_string(question_string_length,
                                            question_string_step,
                                            question_string_start)

    question_str = question_list_to_string(question_seq.copy(), miss_position)
    true_answer = question_seq[miss_position]

    return question_str, str(true_answer)


def run_progression_game():
    return get_question_and_answer
