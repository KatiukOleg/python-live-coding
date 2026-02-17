import pytest

from tasks.iteration02_strings import(
    remove_duplicates_preserve_order,
    find_min_max
)

def test_remove_duplicates_preserve_order_basic():
    assert remove_duplicates_preserve_order([1, 2, 2, 3, 1]) == [1, 2, 3]

def test_remove_duplicates_preserve_order_edges():
    assert remove_duplicates_preserve_order([]) == []
    assert remove_duplicates_preserve_order([1, 1, 1]) == [1]
    assert remove_duplicates_preserve_order([3, 2, 1]) == [3, 2, 1]

def test_find_min_max_basic():
    assert find_min_max([3, 1, 9, -2, 5]) == (-2, 9)