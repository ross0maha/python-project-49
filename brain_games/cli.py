import prompt


def welcome_user() -> str:
    """Welcome user funcion"""

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
<<<<<<< HEAD


def bad_answer(true_answer: str, user_answer: str, user_name: str) -> None:
    """Function for bad answer end exit game"""

    print(f"'{user_answer}' is wrong answer ;(. "
           "Correct answer was '{true_answer}'.")
    print(f"Let's try again, {user_name}")
    exit()
=======
>>>>>>> dev
