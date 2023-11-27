"""
Module to test functions.py.
"""

from utility import functions


def test_save_data() -> None:
    """Tests save_data function.
    """
    data = {"name": "John Smith", "win": 2, "loss": 1}
    file_name = "test_data.yaml"
    functions.save_data(file_name, data)
    my_data = functions.read_data(file_name)
    assert data == my_data


def test_save_data1() -> None:
    """Tests save_data function.
    """
    file_name = "test_data1.yaml"
    data = [{"name": "John Smith", "win": 2, "loss": 1},
            {"name": "Jake Smith", "win": 1, "loss": 0}]
    functions.save_data(file_name, data)
    my_data = functions.read_data(file_name)
    assert data == my_data


def test_save_data_multiple() -> None:
    """Tests save_data function with multiple records.
    """
    file_name = "test_data_multiple.yaml"
    data = [{"name": "John Smith", "win": 2, "loss": 1},
            {"name": "Jake Smith", "win": 1, "loss": 0},
            {"name": "Jane Doe", "win": 3, "loss": 2}]
    functions.save_data(file_name, data)
    my_data = functions.read_data(file_name)
    assert data == my_data


def test_get_random_number() -> None:
    """Tests get_random_number function.
    """
    random_number = functions.get_random_number()
    assert 1 <= random_number <= 20


def test_check_guessed_true() -> None:
    """Tests check_guessed function when the guess is correct.
    """
    assert functions.check_guessed(5, 5) is True


def test_check_guessed_false() -> None:
    """Tests check_guessed function when the guess is incorrect.
    """
    assert functions.check_guessed(5, 10) is False
