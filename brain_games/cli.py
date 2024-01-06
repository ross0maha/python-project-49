import prompt


def welcome_user() -> None:
    """
    Welcome user funcion
    """
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
