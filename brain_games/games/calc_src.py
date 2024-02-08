import random
from brain_games.const import OPERATORS, RND_CALC_MIN, RND_CALC_MAX


def get_eval_and_answer() -> tuple:
    num1 = random.randint(RND_CALC_MIN, RND_CALC_MAX)
    num2 = random.randint(RND_CALC_MIN, RND_CALC_MAX)
    operator = random.choice(OPERATORS)
    question = f'{num1} {operator} {num2}'

    match operator:
        case '+':
            correct_answer = num1 + num2
        case '-':
            correct_answer = num1 - num2
        case '*':
            correct_answer = num1 * num2

    return (question, str(correct_answer))


def run_calc_game():
    return get_eval_and_answer
