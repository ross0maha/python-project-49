#!/usr/bin/env python3
from brain_games.games.progression_src import run_progression_game
from brain_games.engine import run_game
from brain_games.const import PROGRESSION_PROMT


def main():
    run_game(run_progression_game(), PROGRESSION_PROMT)


if __name__ == "__main__":
    main()
