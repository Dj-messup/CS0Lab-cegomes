"""Modue to test file_io.py
"""

import fileio

def test_sort_descending1():
    my_nums = [0, -10, -1, 5, 100]
    fileio.sortListInDescendingOrder(my_nums)
    assert my_nums == [100, 5, 0, -1, -10]

def test_sort_ascending2():
    # Add your test case here
    my_nums = [5, 2, 8, -3, 1]
    fileio.sortListInAscendingOrder(my_nums)
    assert my_nums == [-3, 1, 2, 5, 8]

def test_sort_ascending3():
    # Add your test case here
    my_nums = [3, 3, 3, 3, 3]
    fileio.sortListInAscendingOrder(my_nums)
    assert my_nums == [3, 3, 3, 3, 3]

def test_sort_descending2():
    # Add your test case here
    my_nums = [7, -2, 4, 0, 9]
    fileio.sortListInDescendingOrder(my_nums)
    assert my_nums == [9, 7, 4, 0, -2]

def test_sort_descending3():
    # Add your test case here
    my_nums = [1, 2, 3, 4, 5]
    fileio.sortListInDescendingOrder(my_nums)
    assert my_nums == [5, 4, 3, 2, 1]

