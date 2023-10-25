"""
Strings and Unittest Lab
Updated By: Chica Gomes
CSCI 110 Lab
Date: Oct 12

Read and solve - Simon Says: https://open.kattis.com/problems/simonsays  

Algorithm:
    1. Read N
    2. Repeat N times:
        1. Read the input string
        2. Check if the string begins with 'Simon says'
        3. If it does, print the rest of the string after 'Simon says', otherwise ignore the string
"""


from typing import Union

def main():
    """Main function that solves the problem.
    """
    # Step 1: Read the number of commands (N)
    N = int(input())

    # Step 2: Repeat steps 3 and 4 N times
    for _ in range(N):
        # Step 3: Read the input string
        input_string = input()

        # Step 4: Call the answer function and print the result if not None
        result = answer(input_string)
        if result is not None:
            print(result)

def valid_command(command: str) -> bool:
    """Checks if the string starts with 'Simon says'.

    Args:
        command (str): string to check.

    Returns:
        bool: True if the string starts with 'Simon says', False otherwise.
    """
    # Step 5: Check if the command begins with 'Simon says'
    return command.startswith('Simon says')

def answer(command: str) -> Union[str, None]:
    """Returns the answer given the command or None if the command is not valid.

    Args:
        command (str): string to check.

    Returns:
        str|None: rest of the string after 'Simon says' if the command is valid, None otherwise.
    """
    valid = valid_command(command)
    # Step 6: If the command is valid, return the rest of the string after 'Simon says', None otherwise
    if valid:
        return command[len('Simon says '):]
    else:
        return None

if __name__ == "__main__":
    # Call the main function if the script is run from the command line
    main()
