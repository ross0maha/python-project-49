import random
from brain_games.const import GCD_PROMT
from brain_games.engine import run_game


def get_gcd(num1, num2) -> int:
    while (num2):
        num1, num2 = num2, num1 % num2
    return num1


def get_question_and_answer():
    num1, num2 = random.randint(0, 100), random.randint(0, 100)
    answer = get_gcd(num1, num2)
    return f"{num1} {num2}", str(answer)


def run_gcd_game():
    run_game(get_question_and_answer, GCD_PROMT)
