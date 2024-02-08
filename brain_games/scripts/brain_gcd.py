#!/usr/bin/env python3
from brain_games.games.gcd_src import run_gcd_game
from brain_games.engine import run_game
from brain_games.const import GCD_PROMT


def main():
    run_game(run_gcd_game(), GCD_PROMT)


if __name__ == "__main__":
    main()
