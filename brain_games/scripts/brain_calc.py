#!/usr/bin/env python3
from brain_games.games.calc_src import run_calc_game
from brain_games.engine import run_game
from brain_games.const import CALC_PROMT


def main():
    run_game(run_calc_game(), CALC_PROMT)


if __name__ == "__main__":
    main()
