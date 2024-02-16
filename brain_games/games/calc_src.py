import random

RND_CALC_MIN = 1
RND_CALC_MAX = 50
OPERATORS = ['+', '-', '*']
CALC_PROMT = 'What is the result of the expression?'


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
