import pytest

from tasks.iteration02_strings import(
    remove_duplicates_preserve_order
)

def test_remove_duplicates_preserve_order_basic():
    assert remove_duplicates_preserve_order([1, 2, 2, 3, 1]) == [1, 2, 3]