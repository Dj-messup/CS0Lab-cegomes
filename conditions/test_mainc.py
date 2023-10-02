"""Module to test important functions in main.py
"""

import sys
import mainc

# test function must start with test_ prefix for pytest to recognize it


def test_odd_even():
    """Function to test odd_even function
    """
    number = 99999
    expected = "Alice"
    ans = mainc.odd_even(number)
    assert (mainc.odd_even(number) == ans), f"Expected: {expected}, but got: {ans}"
    assert (mainc.odd_even(200) =="even"), f"Expected: even, but got: {mainc.odd_even(200)}"
    assert (mainc.odd_even(23) =="odd"), f"Expected: odd, but got: {mainc.odd_even(23)}"
    assert (mainc.odd_even(100) =="even"), f"Expected: even, but got: {mainc.odd_even(100)}"
    assert (mainc.odd_even(15) =="odd"), f"Expected: odd, but got: {mainc.odd_even(15)}"
    # Write 3rd test case
    # Write 4th test case
    print("All test cases passed for oddOrEven()...", file=sys.stderr)

# Write a function to test answer function
# Write at least 3 test cases