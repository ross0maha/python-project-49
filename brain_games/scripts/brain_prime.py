#!/usr/bin/env python3
from brain_games.games.prime_src import get_question_and_answer
from brain_games.engine import run_game

PRIME_PROMT = 'Answer "yes" if given number is prime. ' \
              'Otherwise answer "no".'


def main():
    run_game(get_question_and_answer, PRIME_PROMT)


if __name__ == "__main__":
    main()
