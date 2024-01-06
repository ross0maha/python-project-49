#!/usr/bin/env python3
import brain_games.cli as cli
from random import randint
import prompt


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
            print("Correct!")
        elif rnd_int % 2 and answer == 'no':
            print("Correct!")
        elif not rnd_int % 2 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}")
            return 0
        elif rnd_int % 2 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}")
            return 0
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
