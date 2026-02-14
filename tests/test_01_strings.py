import pytest

from tasks.iteration01_strings import (
    reverse_string,
    reverse_words
)

def test_reverse_string_basic():
    assert reverse_string("Hello World!") == "!dlroW olleH"

def test_reverse_words_basic():
    assert reverse_words("Hello World") == "World Hello"
