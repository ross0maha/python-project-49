#!/usr/bin/env python3
from brain_games.cli import welcome_user, bad_answer
from random import randint
import prompt


def do_rand() -> tuple:
    """
    Function returned tuple:
        result - random math progression
        miss_position - position of miss numder in progression
        miss_num - random numder for question
    """

    length = randint(5, 10)
    step = randint(1, 7)
    start = randint(0, 50)
    result = list(range(start, start + step * length, step))
    miss_position = randint(0, length - 1)
    miss_num = result[miss_position]

    return result, miss_position, miss_num


def question_list_to_string(list_seq, miss_position) -> str:
    """
    Function for prepare random list to question string
    """

    result = ""
    for elem in enumerate(list_seq):
        if elem[0] == miss_position:
            result += ".. "
        else:
            result += str(elem[1]) + " "
    return result


def main():
    """
    Brain-progression is the fourth game in which the user must
    guess the missing number in a mathematical progression.
    """

    user_name = welcome_user()

    print("What number is missing in the progression?")

    for i in range(3):
        # Generate and unpack random values
        question_seq, miss_position, true_answer = do_rand()

        # Convert list for question to string
        question_str = question_list_to_string(question_seq, miss_position)

        print(f"Question: {question_str}")
        user_answer = prompt.integer("Your answer: ")

        # Check user answer
        if user_answer == true_answer:
            print("Correct!")
        else:
            bad_answer(true_answer, user_answer, user_name)
    
    print(f"Congratulations, {user_name}!")

if __name__ == "__main__":
    main()
