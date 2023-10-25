"""Test cases for simonsays.py
"""


import simonsays

def test_valid_command():
    """Test valid_command function.
    """
    ans = simonsays.valid_command("Simon says do this")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_valid_command2():
    """Test valid_command function."""
    ans = simonsays.valid_command("do this")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# Test case to check if 'valid_command' returns True for a valid command
def test_valid_command3():
    """Test valid_command function."""
    ans = simonsays.valid_command("Simon says jump")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# Test case to check if 'valid_command' returns False for an invalid command
def test_valid_command4():
    """Test valid_command function."""
    ans = simonsays.valid_command("says Simon do this")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says do this")
    expected = " do this"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# Test case to check if 'answer' returns the correct part of the string
def test_answer2():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says jump")
    expected = " jump"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# Test case to check if 'answer' returns None for an invalid command
def test_answer3():
    """Test answer function.
    """
    ans = simonsays.answer("Do this")
    expected = None
    assert ans is expected, f"Expected: {expected}, but got: {ans}"

# Test case to check if 'answer' returns an empty string for an empty 'Simon says' command
def test_answer4():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says")
    expected = ""
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
