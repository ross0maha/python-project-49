#!/usr/bin/env python3
from brain_games.games.prime_src import run_prime_game
from brain_games.engine import run_game
from brain_games.const import PRIME_PROMT


def main():
    run_game(run_prime_game(), PRIME_PROMT)


if __name__ == "__main__":
    main()
