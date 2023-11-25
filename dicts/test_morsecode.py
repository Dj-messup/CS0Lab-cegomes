import morsecode

def test_convert_to_palindrome1():
    actual_ans = morsecode.convert_to_morse('AN')
    expected_ans = '.-.-'
    assert actual_ans == expected_ans

def test_convert_to_palindrome2():
    actual_ans = morsecode.convert_to_morse('SOS')
    expected_ans = '...'
    assert actual_ans == expected_ans

def test_convert_to_palindrome3():
    actual_ans = morsecode.convert_to_morse('123')
    expected_ans = '.---- ..--- ...--'
    assert actual_ans == expected_ans

def test_convert_to_palindrome4():
    actual_ans = morsecode.convert_to_morse('HELLO')
    expected_ans = '.... . .-.. .-.. ---'
    assert actual_ans == expected_ans


def test_ispalindrome1():
    ans = morsecode.is_palindrome('.--.')
    expected = 1
    assert ans == expected

def test_ispalindrome2():
    ans = morsecode.is_palindrome('....-....')
    expected = 0
    assert ans == expected

def test_ispalindrome3():
    ans = morsecode.is_palindrome('.-.-.')
    expected = 1
    assert ans == expected

def test_ispalindrome4():
    ans = morsecode.is_palindrome('..-..')
    expected = 0
    assert ans == expected
