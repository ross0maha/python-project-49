import random
from brain_games.engine import run_game
from brain_games.const import CALC_PROMT, OPERATORS


def get_eval_and_answer():
    num1, num2 = random.randint(1, 50), random.randint(1, 50)
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
    run_game(get_eval_and_answer, CALC_PROMT)
