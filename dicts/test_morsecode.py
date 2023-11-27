"""Module to test functions in morsecode.py 
"""

import morsecode

# Test cases for convert_to_palindrome function
def test_convert_to_palindrome1():
    actual_ans = morsecode.convert_to_morse('AN')
    expected_ans = '.- -.'
    assert actual_ans == expected_ans

#  - Write 3 more test cases to test convert_to_palindrome function

def test_convert_to_palindrome3():
    actual_ans = morsecode.convert_to_morse('123')
    expected_ans = '.---- ..--- ...--'
    assert actual_ans == expected_ans

def test_convert_to_palindrome4():
    actual_ans = morsecode.convert_to_morse('HELLO')
    expected_ans = '.... . .-.. .-.. ---'
    assert actual_ans == expected_ans


# Test cases for is_palindrome function
def test_ispalindrome1():
    ans = morsecode.is_palindrome('.--.')
    expected = 1
    assert ans == expected

# - Write 3 more test cases to test is_palindrome function

def test_ispalindrome3():
    ans = morsecode.is_palindrome('.-.-.')
    expected = 1
    assert ans == expected

# Additional test cases for is_palindrome function
def test_ispalindrome5():
    ans = morsecode.is_palindrome('---...---')
    expected = 1
    assert ans == expected

def test_ispalindrome7():
    ans = morsecode.is_palindrome('-.-.-.-')
    expected = 1
    assert ans == expected

