#!/usr/bin/env python3
from brain_games.cli import welcome_user, bad_answer
from random import randint
import prompt


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

    # Input user name func with prompt lib and print condition
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # start the cycle for three tries
    for i in range(3):

        # Generate random int from 0 to 100 and print question
        rnd_int = randint(0, 100)
        print(f"Question: {rnd_int}")

        # Input answer from user with prompt lib
        user_answer = prompt.string('Your answer: ')

        true_answer = 'yes' if rnd_int % 2 == 0 else 'no'

        # Check answer
        condition = [is_even(rnd_int), user_answer]
        match condition:
            case [True, "yes"]:
                print("Correct!")
            case [False, "no"]:
                print("Correct!")
            case _:
                bad_answer(true_answer, user_answer, user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
