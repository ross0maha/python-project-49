import random
from brain_games.const import PRIME_PROMT
from brain_games.engine import run_game


def is_prime(num):
    num_sqrt = int(num ** 0.5)
    count = 2
    while count <= num_sqrt:
        if num % count == 0:
            return "no"
        else:
            count += 1
    return "yes"


def get_question_and_answer():
    question = random.randint(1, 100)
    return question, is_prime(question)


def run_prime_game():
    run_game(get_question_and_answer, PRIME_PROMT)
