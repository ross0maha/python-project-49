#!/usr/bin/env python3
from brain_games.games.even_src import run_even_game
from brain_games.engine import run_game
from brain_games.const import EVEN_PROMT


def main():
    run_game(run_even_game(), EVEN_PROMT)


if __name__ == "__main__":
    main()
