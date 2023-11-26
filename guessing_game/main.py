"""
Game Application - Guess the Number 
"""

__author__ = "Chica Gomes"
__date__ = "11/25"
__license__ = "MIT"
__course__ = "CSCI 110 Lab"
__semester__ = "Fall 2023"

from typing import Any, List, Dict
import time
from python_utils import functions
import settings
from game import play_game, clear_screen, pause, get_menu_option


# Import statements and other code as provided

def game_intro() -> None:
    clear_screen()
    print('Welcome to the Guess the Number game!')
    time.sleep(1)
    print(settings.ASCII)
    time.sleep(1)
    print("Let's start by entering your name.")
    print('Are you ready?')
    pause()


def main() -> None:
    """Main function for the game."""
    game_intro()
    
    data = functions.read_data(settings.SCORE_BOARD_FILE)
    if not data:
        data = []

    # Ask who's playing?
    player = functions.get_player_info()
    current_player = functions.find_player_in_db(data, player['name'])

    if current_player is None:
        data.append(player)
    else:
        player = current_player

    while True:
        clear_screen()
        option = get_menu_option()
        if option == 1:
            win = play_game(player['name'], settings.MAX_TRIES)
            if win:
                player['win'] += 1
            else:
                player['loss'] += 1
        elif option == 2:
            view_scoreboard(data)
        elif option == 3:
            functions.save_data(settings.SCORE_BOARD_FILE, data)
            print(f'Saving score board to the file {settings.SCORE_BOARD_FILE}')
            print("Goodbye!")
            input('Press Enter to exit...')
            break
        else:
            # Invalid option. Try again.
            print("Invalid option. Please enter a valid option.")

# Implement the view_scoreboard function
def view_scoreboard(data: List[Dict[str, Any]]) -> None:
    """Display data in tabular format.

    Args:
        data (List[Dict[str, Any]]): Data of all the players in the database
    """
    # Implement the logic to display the scoreboard in tabular format.
    # You might consider using the tabulate library for this purpose.
    pass  # Placeholder to keep the function body non-empty


if __name__ == "__main__":
    main()