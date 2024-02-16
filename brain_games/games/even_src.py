import random
from brain_games.const import RND_MIN, RND_MAX

EVEN_PROMT = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value) -> bool:
    return value % 2


def get_randint_and_answer() -> tuple:
    question = random.randint(RND_MIN, RND_MAX)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
