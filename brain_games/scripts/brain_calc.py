#!/usr/bin/env python3
from brain_games.cli import welcome_user, bad_answer
from random import randint, choice
import prompt


def main():
    """
    Brain-Calc - is a second game. User must calculate math expression.
    """

    # Input user name func with prompt lib
    user_name = welcome_user()
    print("What is the result of the expression?")

    for i in range(3):
        # Generating two random number for e[pression]
        num1, num2 = randint(1, 50), randint(1, 50)

        # Random chiose operator
        operator = choice(["+", "-", "*"])

        # Input answer from user with prompt lib
        print(f"Question: {num1} {operator} {num2}")
        user_answer = prompt.integer('Your answer: ')

        # Calculate true answer
        match operator:
            case '+':
                true_answer = num1 + num2
            case '-':
                true_answer = num1 - num2
            case '*':
                true_answer = num1 * num2

        # Check user answer
        if user_answer == true_answer:
            print(f"Your answer: {user_answer}")
            print("Correct!")
        else:
            bad_answer(true_answer, user_answer, user_name)

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
