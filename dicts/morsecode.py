"""
Dictionary and Unittest Lab
Updated By: FIXME
CSCI 110 Lab
Date: FIXME

Solution for Kattis problem - Morse Code Palindromes - https://open.kattis.com/problems/morsecodepalindromes  

Given english text, the program finds if the corresponding morse code is a palindrome.

Algorithm steps:
1. Create a dictionary to map alphabets and numbers to morse code 
2. Read the input english string
3. Convert the string into upper case english string
4. Convert english string into Morse Code string using the dictionary
5. Check if the Morse Code string is a palindrome
    i. Print 1 if it's a palindrome
    ii Otherwise, print 0
"""

import sys

# create English to Morse Code dictionary
engToMorse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',  # map the digits to their corresponding Morse code
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}


def is_palindrome(morse_code: str) -> int:
    """Returns 1 if the morse_code string is palindrome; 0 Otherwise.

    Args:
        morse_code (str): Morse code palindrome string

    Returns:
        int: 1 or 0
    """
    # 2. if the morse_code string is empty, return 0
    # Otherwise use the algorithm:
    # 1. reverse the morse_code string and store it in a variable
    # 2. if the morse_code equals the reversed string, it is a palindrome and return 1
    # 3. return 0 otherwise
    if not morse_code:
        return 0
    reversed_morse = morse_code[::-1]
    return 1 if morse_code == reversed_morse else 0


def convert_to_morse(english: str) -> str:
    """The function converts the given English text into corresponding Morse code

    Args:
        english (str): English text converted into uppercase

    Returns:
        str: Morse code
    """
    morse_code = ''
    # Algorithm steps:
    # For each character in English,
    #   find the Morse code of the character using engToMorse dictionary
    #   concatenate Morse code to morse_code variable if key exists
    #   ignore the key/character if it doesn't exist in the dictionary
    # FIXME 3: implement the above algorithm
    for char in english:
        morse_code += engToMorse.get(char, '')
    return morse_code


def solve() -> None:
    # read/input English text as a line
    english = input()
    # FIXME 4: convert English into uppercase
    upper_english = english.upper()
    print(upper_english, file=sys.stderr)
    morse_code = convert_to_morse(upper_english)
    # FIXME 5: call is_palindrome passing proper argument and print the result
    print(is_palindrome(morse_code))


if __name__ == '__main__':
    solve()
