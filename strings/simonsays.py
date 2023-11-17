def main():
    # Step 1: Read the number of commands (N)
    N = int(input())

    # Step 2: Repeat steps 3 and 4 N times
    for _ in range(N):
        # Step 3: Read the input command
        command = input()

        # Step 4: Call the process_command function and print the result if not None
        result = process_command(command)
        if result is not None:
            print(result)

def process_command(command: str) -> str:
    """Returns the rest of the command after "Simon says" if the command starts with it, None otherwise.

    Args:
        command (str): The input command.

    Returns:
        str|None: The rest of the command after "Simon says" if the command starts with it, None otherwise.
    """
    # Step 5: Check if the command begins with 'Simon says'
    if command.startswith('Simon says '):
        return command[len('Simon says '):]
    else:
        return None
    

def answer(command: str) -> str:
    """Returns the rest of the command after "Simon says" if the command starts with it, None otherwise."""
    if command.startswith('Simon says '):
        return command[len('Simon says '):]
    else:
        return None


def valid_command(command: str) -> bool:
    """Returns True if the command starts with "Simon says," False otherwise."""
    return command.startswith('Simon says ')


if __name__ == "__main__":
    # Call the main function if the script is run from the command line
    main()

