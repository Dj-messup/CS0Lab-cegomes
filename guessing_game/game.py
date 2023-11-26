""" 
Functions related to game main logic.
"""
from python_utils import functions

def play_game(name: str, max_tries: int) -> bool:
    """Main game logic of the Guess The Number game.

    Args:
        name (str): name of the player.
        max_tries (int): maximum number of tries.

    Returns:
        bool: True if the player wins, False otherwise.
    """
    print(f"Let's play the Game, {name}! Good luck...")
    rand = functions.get_random_number()
    print('I am thinking of a number between 1 and 20.')
    print('You have 5 chances to guess the number.')
    tries = 0
    while tries <= max_tries:
        # Add code to get the user's guess using the correct
        # function in utility/functions.py.
        user_guess = functions.get_user_guess()

        # check if the user's guess is correct using the correct
        # function in utility/functions.py.
        if functions.check_guess(user_guess, rand):
            # If the user's guess is correct, print a message and return True for a win.
            print(f"Congratulations, {name}! You guessed the correct number.")
            return True
        else:
            # If the user's guess is incorrect,
            # print a message saying their guess is too large or too small
            # and increment the number of tries.
            if user_guess > rand:
                print("Your guess is too large.")
            else:
                print("Your guess is too small.")
            tries += 1
    else:
        # return False for a loss
        return False

def clear_screen() -> None:
    """Clears the screen.
    """
    print("\033c", end="")


def pause() -> None:
    """Pauses the screen.
    """
    input("Press Enter to continue...")
    clear_screen()


def get_menu_option() -> int:
    """Prints menu for player to interact with.
    """

    menu = """
    Menu Options
    ============ 
    1. Play Game
    2. View Scoreboard
    3. Quit
    """
    print(menu)
    while True:
        option = input("Enter one of the menu options [1-3]: ")
        if not option.isdigit():
            print("Invalid option. Try again.")
            continue
        int_option = int(option)
        if not 1 <= int_option <= 3:
            print("Invalid option. Try again.")
            continue
        return int_option
