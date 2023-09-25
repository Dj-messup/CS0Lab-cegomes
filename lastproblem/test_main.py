"""Module to test functions from main.py
"""

import sys
import Main

# test function must start with test_ prefix for pytest to recognize it


def test_answer():
    """Test answer function
    """
    ans = Main.answer("Alice")
    expected = "Thank you, Alice, and farewell!"
    assert ans == expected
    ans = Main.answer("Bob")
    expected = "Thank you, Bob and farewell!"  #fix the expected output
    assert ans == expected
    # add a new test case to test your answer function
    ans = Main.answer("Twilight")
    expected = "Thank you, Twilight and farewell!"  #fix the expected output
    assert ans == expected
    # add a new test case to test your answer function
    ans = Main.answer("Apple Jack")
    expected = "Thank you, Apple Jack and farewell!"  #fix the expected output
    assert ans == expected
    # add a new test case to test your answer function
    ans = Main.answer("Fluttershy")
    expected = "Thank you, Fluttershy and farewell!"  #fix the expected output
    assert ans == expected
    # add a new test case to test your answer function
    ans = Main.answer("Rainbow Dash")
    expected = "Thank you, Rainbow Dash and farewell!"  # fix the expected output
    assert ans == expected
    print("All test cases passed...", file=sys.stderr)


if __name__ == "__main__":
    test_answer()
