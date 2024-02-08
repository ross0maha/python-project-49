import prompt


def welcome_user() -> str:
    """Welcome user funcion"""

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
