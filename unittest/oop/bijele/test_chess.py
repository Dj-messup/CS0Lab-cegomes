"""
Module to test the Chess class. 
"""

#unittest 
import unittest
from bijele import Chess

class TestChess(unittest.TestCase):

    def test_init(self):
        """Test the __init__ method"""
        chess = Chess(1, 1, 2, 2, 2, 8)
        self.assertEqual(chess.king, 1)
        self.assertEqual(chess.queen, 1)
        self.assertEqual(chess.rooks, 2)
        self.assertEqual(chess.bishops, 2)
        self.assertEqual(chess.knights, 2)
        self.assertEqual(chess.pawns, 8)

    def test_init_default_values(self):
        """Test the __init__ method with default values"""
        chess = Chess()
        self.assertEqual(chess.king, 1)  # Assuming default value is 1
        self.assertEqual(chess.queen, 1)
        self.assertEqual(chess.rooks, 2)
        self.assertEqual(chess.bishops, 2)
        self.assertEqual(chess.knights, 2)
        self.assertEqual(chess.pawns, 8)

    def test_init_negative_values(self):
        """Test the __init__ method with negative values"""
        chess = Chess(-1, -1, -2, -2, -2, -8)
        self.assertEqual(chess.king, -1)
        self.assertEqual(chess.queen, -1)
        self.assertEqual(chess.rooks, -2)
        self.assertEqual(chess.bishops, -2)
        self.assertEqual(chess.knights, -2)
        self.assertEqual(chess.pawns, -8)

    def test_str(self):
        """Test the __str__ method"""
        chess = Chess(1, 1, 2, 2, 2, 8)
        self.assertEqual(str(chess), '1 1 2 2 2 8')

    def test_str_default_values(self):
        """Test the __str__ method with default values"""
        chess = Chess()
        self.assertEqual(str(chess), '1 1 2 2 2 8')  # Assuming default values are 1 1 2 2 2 8

    def test_str_negative_values(self):
        """Test the __str__ method with negative values"""
        chess = Chess(-1, -1, -2, -2, -2, -8)
        self.assertEqual(str(chess), '-1 -1 -2 -2 -2 -8')

    def test_sub(self):
        """Test the __sub__ method"""
        chess1 = Chess(1, 1, 2, 2, 2, 8)
        chess2 = Chess(0, 1, 1, 2, 1, 8)
        chess3 = chess1 - chess2
        self.assertEqual(chess3.king, 1)
        self.assertEqual(chess3.queen, 0)
        self.assertEqual(chess3.rooks, 1)
        self.assertEqual(chess3.bishops, 0)
        self.assertEqual(chess3.knights, 1)
        self.assertEqual(chess3.pawns, 0)

    def test_sub_negative_values(self):
        """Test the __sub__ method with negative values"""
        chess1 = Chess(1, 1, 2, 2, 2, 8)
        chess2 = Chess(2, 2, 3, 3, 3, 10)
        chess3 = chess1 - chess2
        self.assertEqual(chess3.king, -1)
        self.assertEqual(chess3.queen, -1)
        self.assertEqual(chess3.rooks, -1)
        self.assertEqual(chess3.bishops, -1)
        self.assertEqual(chess3.knights, -1)
        self.assertEqual(chess3.pawns, -2)

if __name__ == '__main__':
    unittest.main()
