#!/usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint
import prompt


def bad_answer(answer: str, name: str, rnd_int: int) -> None:
    """Function for bad answer end exit game"""

    true_answer = "no" if rnd_int % 2 else "yes"

    print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer}'.")
    print(f"Let's try again, {name}")
    exit()


def is_even(value) -> bool:
    """Check even function"""

    if value % 2 == 0:
        return True
    else:
        return False


def main() -> None:
    """
    Brain-Even - is a frist game to reconizing random even-number.
    """

    # Input user name func with prompt lib
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # start the cycle for three tries
    for i in range(3):

        # Generate random int from 0 to 100 and print question
        rnd_int = randint(0, 100)
        print(f"Question: {rnd_int}")

        # Input answer from user with prompt lib
        answer = prompt.string('Your answer: ')

        # Check answer
        condition = [is_even(rnd_int), answer]
        match condition:
            case [True, "yes"]:
                print("Correct!")
            case [False, "no"]:
                print("Correct!")
            case _:
                bad_answer(answer, name, rnd_int)

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
