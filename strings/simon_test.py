# test_simonsays.py
import simonsays

def test_valid_command():
    """Test valid_command function."""
    # Test case 1: Command starts with "Simon says"
    ans = simonsays.valid_command("Simon says do this")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    # Test case 2: Command does not start with "Simon says"
    ans = simonsays.valid_command("do this")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    # Test case 3: Command starts with "Simon says" with additional text
    ans = simonsays.valid_command("Simon says jump")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    # Test case 4: Empty command
    ans = simonsays.valid_command("")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer():
    """Test answer function."""
    # Test case 1: Command starts with "Simon says"
    ans = simonsays.answer("Simon says do this")
    expected = "do this"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    # Test case 2: Command does not start with "Simon says"
    ans = simonsays.answer("jump")
    expected = None
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    # Test case 3: Command starts with "Simon says" with additional text
    ans = simonsays.answer("Simon says clap your hands")
    expected = "clap your hands"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

if __name__ == "__main__":
    # Run the tests
    test_valid_command()
    test_answer()

