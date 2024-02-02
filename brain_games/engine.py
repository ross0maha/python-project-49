import prompt
from brain_games.const import AMOUNT_OF_ROUNDS


def run_game(get_question_and_answer, game_promt):
    user_name = prompt.string("Welcome to the Brain Games!\n"
                              "May i have you name? ")
    print(f"Hello, {user_name}!\n"
          f"{game_promt}")

    for _ in range(AMOUNT_OF_ROUNDS):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f"Question: {question}\n"
                                    "Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f"Congritulations, {user_name}!")
