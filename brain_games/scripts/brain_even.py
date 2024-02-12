#!/usr/bin/env python3
from brain_games.games.even_src import get_randint_and_answer
from brain_games.engine import run_game

EVEN_PROMT = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(get_randint_and_answer, EVEN_PROMT)


if __name__ == "__main__":
    main()
