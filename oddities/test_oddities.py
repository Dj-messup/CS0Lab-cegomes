"""Test cases for oddities.py"""
import oddities


def test_answer():
    """Test answer function."""
    ans = oddities.answer(10)
    expected = "10 is even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_answer2():
    """Test answer function for negavitve odd number."""
    ans = oddities.answer(-199)
    expected = "-199 is odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer3():
    """Test answer function for negavitve odd number."""
    ans = oddities.answer(-199)
    expected = "13 is odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_answer():
    """Test answer function."""
    ans = oddities.answer(2)
    expected = "2 is even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# add a new test case  function to test your answer function

# add a new test case function to test your answer function


def test_odd_even():
    """Test odd_even function.
    """
    ans = oddities.odd_even(10)
    expected = "even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_odd_even2():
    """Test odd_even function for negavitve odd number
    """
    ans = oddities.odd_even(-199)
    expected = "odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

def test_odd_even2():
    """Test odd_even function for negavitve odd number
    """
    ans = oddities.odd_even(13)
    expected = "odd"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# add a new test case function to test your answer function
def test_odd_even():
    """Test odd_even function.
    """
    ans = oddities.odd_even(2)
    expected = "even"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
# add a new test case function to test your answer function