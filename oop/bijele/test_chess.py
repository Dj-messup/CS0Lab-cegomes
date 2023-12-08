# test_chess.py

from bijele import Chess

def test__init__() -> None:
    """Test the __init__ method"""
    chess = Chess(1, 1, 2, 2, 2, 8)
    assert chess.king == 1
    assert chess.queen == 1
    assert chess.rooks == 2
    assert chess.bishops == 2
    assert chess.knights == 2
    assert chess.pawns == 8

def test__init__default_values() -> None:
    """Test the __init__ method with default values"""
    chess = Chess()
    assert chess.king == 1  # Assuming default value is 1
    assert chess.queen == 1
    assert chess.rooks == 2
    assert chess.bishops == 2
    assert chess.knights == 2
    assert chess.pawns == 8

def test__init__negative_values() -> None:
    """Test the __init__ method with negative values"""
    chess = Chess(-1, -1, -2, -2, -2, -8)
    assert chess.king == -1
    assert chess.queen == -1
    assert chess.rooks == -2
    assert chess.bishops == -2
    assert chess.knights == -2
    assert chess.pawns == -8

def test__str__() -> None:
    """Test the __str__ method"""
    chess = Chess(1, 1, 2, 2, 2, 8)
    assert str(chess) == '1 1 2 2 2 8'

def test__str__default_values() -> None:
    """Test the __str__ method with default values"""
    chess = Chess()
    assert str(chess) == '1 1 2 2 2 8'  # Assuming default values are 1 1 2 2 2 8

def test__str__negative_values() -> None:
    """Test the __str__ method with negative values"""
    chess = Chess(-1, -1, -2, -2, -2, -8)
    assert str(chess) == '-1 -1 -2 -2 -2 -8'

def test__sub__():
    """Test the __sub__ method"""
    chess1 = Chess(1, 1, 2, 2, 2, 8)
    chess2 = Chess(0, 1, 1, 2, 1, 8)
    chess3 = chess1 - chess2
    assert chess3.king == 1
    assert chess3.queen == 0
    assert chess3.rooks == 1
    assert chess3.bishops == 0
    assert chess3.knights == 1
    assert chess3.pawns == 0

def test__sub__negative_values():
    """Test the __sub__ method with negative values"""
    chess1 = Chess(1, 1, 2, 2, 2, 8)
    chess2 = Chess(2, 2, 3, 3, 3, 10)
    chess3 = chess1 - chess2
    assert chess3.king == -1
    assert chess3.queen == -1
    assert chess3.rooks == -1
    assert chess3.bishops == -1
    assert chess3.knights == -1
    assert chess3.pawns == -2

