#!/usr/bin/env python3
from brain_games.games.calc_src import get_eval_and_answer
from brain_games.games.calc_src import CALC_PROMT
from brain_games.engine import run_game


def main():
    run_game(get_eval_and_answer, CALC_PROMT)


if __name__ == "__main__":
    main()
