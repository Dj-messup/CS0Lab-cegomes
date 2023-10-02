"""
Conditional Logic Lab
Updated By: Chica Gomes
CSCI 110 Lab
Date: September 28th

Read and solve the Kattis problem: https://open.kattis.com/problems/twostones 

Algorithm Steps:
  1. Read the number of stones
  2. Check if the number of stones is odd or even
  3. Print the winner
    3.a. If the number is odd, Alice wins.
    3.b. Otherwise, Bob wins.
"""

def main():
    """Main function that solves the problem.
    """
    #read the number of stones
    number = int(input())  # Read the number of stones as an integer

    # call answer function passing the number of stones as an argument
    ans = answer(number)

    # print the answer as shown in the sample output
    print(ans)

def odd_even(number: int):
    """Checks if the number is odd or even

    Args:
        number (int): number to check odd or even

    Returns:
        str: 'odd' if the number is odd, 'even' otherwise
    """
    #if the number divided by 2 has 0 remainder, return 'even'
    # otherwise, return 'odd'
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def answer(stone: int):
    """Creates the final answer and returns it given the number of stones

    Args:
        stone (int): number of stones

    Returns:
        str: 'Alice' if the number of stones is odd, 'Bob' otherwise
    """
    even_or_odd = odd_even(stone)
    if even_or_odd == "odd":
        return "Alice"
    else:
        return "Bob"

if __name__ == "__main__":
    main()
