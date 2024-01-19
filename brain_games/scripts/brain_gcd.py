#!/usr/bin/env python3
from brain_games.cli import welcome_user, bad_answer
from random import randint
import prompt


def gcd(num1, num2) -> int:
    """Function for calculate gcd"""

    while (num2):
        num1, num2 = num2, num1 % num2
    return abs(num1)


def main() -> None:
    """
    Brain-gcd - is a thrid game to calculate gcd (greatest common divisor).
    """

    # Input user name func with prompt lib and print condition
    user_name = welcome_user()

    print("Find the greatest common divisor of given numbers.")

    for i in range(3):
        # Generate two random int from 0 to 100 and print question
        num1, num2 = randint(0, 100), randint(0, 100)
        print(f"Question: {num1} {num2}")

        # Input answer from user with prompt lib
        user_answer = prompt.integer('Your answer: ')

        true_answer = gcd(num1, num2)

        # Check user answer
        if user_answer == true_answer:
            print(f"Your answer: {user_answer}")
            print("Correct!")
        else:
            bad_answer(true_answer, user_answer, user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
