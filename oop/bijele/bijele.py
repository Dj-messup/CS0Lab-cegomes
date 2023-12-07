"""
Date: unknown
by: Chica Gomes

Using OOP concept, solve: Bijele - https://open.kattis.com/problems/bijele 

Algorithm:
    1. Create chess.py module to define the the Chess class
    2. Define the __init__ method to initialize the Chess class
    3. Define the __str__ method to return the string representation of the Chess class
    4. Define the __sub__ method to return the difference between two Chess objects
    5. print the difference as shown in the sample output
"""

from chess import Chess

def main() -> None:
    # the actual chess pieces count
    actual_chess = Chess(1, 1, 2, 2, 2, 8)

    # read the chess pieces count from the input
    pieces = tuple(map(int, input("Enter the counts of kings, queens, rooks, bishops, knights, and pawns separated by spaces: ").split()))
    given_chess = Chess(*pieces)

    # create a Chess object using the input data
    # print the difference between the actual and input chess pieces count
    ans = actual_chess - given_chess  # creates a new Chess object
    print(ans)

if __name__ == "__main__":
    main()
