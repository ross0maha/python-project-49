#!/usr/bin/env python3
import random
from brain_games.engine import run_game
from brain_games.const import EVEN_PROMT


def is_even(value) -> bool:
    return value % 2


def get_randint_and_answer():
    question = random.randint(0, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def run_even_game():
    run_game(get_randint_and_answer, EVEN_PROMT)
