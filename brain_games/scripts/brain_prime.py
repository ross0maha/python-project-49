#!/usr/bin/env python3
from brain_games.cli import welcome_user, bad_answer
from random import randint
import prompt


def is_prime(num) -> str:
    """
    This function returns "yes" if incoming number is prime
    or no if is not.
    """

    # Get the quare root of nuber
    num_sqrt = int(num ** 0.5)
    count = 2
    while count <= num_sqrt:
        if num % count == 0:
            return "no"
        else:
            count += 1
    return "yes"


def main() -> None:
    """
    Brain-prime is the fifth game of simple number recognition.
    """

    # Input user name func with prompt lib and print condition
    user_name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(3):

        # Generate random number for question
        question = randint(1, 100)

        print(f"Question: {question}")

        # Input answer from user with prompt lib
        user_answer = prompt.string('Your answer: ')

        # Check quesion number for prime
        true_answer = is_prime(question)

        # Check condition
        if user_answer == true_answer:
            print("Correct!")
        else:
            bad_answer(true_answer, user_answer, user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
