#!/usr/bin/env python3
from brain_games.games.gcd_src import get_question_and_answer
from brain_games.engine import run_game

GCD_PROMT = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(get_question_and_answer, GCD_PROMT)


if __name__ == "__main__":
    main()
