import pytest

from tasks.iteration01_strings import (
    reverse_string
)

def test_reverse_string_basic():
    assert reverse_string("Hello World!") == "!dlroW olleH"
