import random
from brain_games.const import RND_MIN, RND_MAX

GCD_PROMT = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2) -> int:
    while (num2):
        num1, num2 = num2, num1 % num2
    return num1


def get_question_and_answer():
    num1 = random.randint(RND_MIN, RND_MAX)
    num2 = random.randint(RND_MIN, RND_MAX)
    answer = get_gcd(num1, num2)
    return f"{num1} {num2}", str(answer)
