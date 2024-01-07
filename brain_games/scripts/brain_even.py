#!/usr/bin/env python3
import brain_games.cli as cli
from random import randint
import prompt


def good_answer():
    print("Correct!")


def bad_answer(answer, name, key_w):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{key_w}'.")
    print(f"Let's try again, {name}")
    exit()


def main() -> None:
    """
    Brain-Even - is a frist game to reconizing random even-number.
    """
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # start the cycle for three tries
    for i in range(3):
        rnd_int = randint(0, 100)
        print(f"Question: {rnd_int}")
        answer = prompt.string('Your answer: ')
        # Answer check
        if not rnd_int % 2 and answer == 'yes':
            good_answer()
        elif rnd_int % 2 and answer == 'no':
            good_answer()
        elif not rnd_int % 2 and answer != 'yes':
            bad_answer(answer, name, 'yes')
        elif rnd_int % 2 and answer != 'no':
            bad_answer(answer, name, 'no')
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
