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
# chess.py

class Chess:
    def __init__(self, king=1, queen=1, rooks=2, bishops=2, knights=2, pawns=8):
        self.king = king
        self.queen = queen
        self.rooks = rooks
        self.bishops = bishops
        self.knights = knights
        self.pawns = pawns

    def __str__(self):
        return f'{self.king} {self.queen} {self.rooks} {self.bishops} {self.knights} {self.pawns}'

    def __sub__(self, other: 'Chess'):
        k_diff = self.king - other.king
        q_diff = self.queen - other.queen
        r_diff = self.rooks - other.rooks
        b_diff = self.bishops - other.bishops
        kn_diff = self.knights - other.knights
        p_diff = self.pawns - other.pawns
        return Chess(k_diff, q_diff, r_diff, b_diff, kn_diff, p_diff)

def main() -> None:
    # the actual chess pieces count
    actual_chess = Chess(1, 1, 2, 2, 2, 8)

    # read the chess pieces count from the input
    pieces = tuple(map(int, input().split()))
    given_chess = Chess(*pieces)

    # print the difference between the actual and input chess pieces count
    ans = actual_chess - given_chess
    print(ans)

if __name__ == "__main__":
    main()

