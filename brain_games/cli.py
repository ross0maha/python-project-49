import prompt


def welcome_user() -> str:
    """Welcome user funcion"""
    
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
