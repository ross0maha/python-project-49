import random
from brain_games.const import RND_MIN, RND_MAX


def is_prime(num):
    num_sqrt = int(num ** 0.5)
    count = 2
    while count <= num_sqrt:
        if num % count == 0:
            return False
        else:
            count += 1
    return True


def get_question_and_answer():
    question = random.randint(RND_MIN + 1, RND_MAX)
    true_answer = 'yes' if is_prime(question) else 'no'
    return question, true_answer
