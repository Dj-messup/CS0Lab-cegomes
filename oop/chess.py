"""Module to define the Chess class. 
"""


# chess.py

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
