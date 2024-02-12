#!/usr/bin/env python3
from brain_games.games.progression_src import get_question_and_answer
from brain_games.engine import run_game

PROGRESSION_PROMT = 'What number is missing in the progression?'


def main():
    run_game(get_question_and_answer, PROGRESSION_PROMT)


if __name__ == "__main__":
    main()
