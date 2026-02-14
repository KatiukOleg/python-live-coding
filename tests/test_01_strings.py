import pytest

from tasks.iteration01_strings import (
    reverse_string,
    reverse_words,
    is_palindrome,
    first_unique_char
)

def test_reverse_string_basic():
    assert reverse_string("Hello World!") == "!dlroW olleH"

def test_reverse_words_basic():
    assert reverse_words("Hello World") == "World Hello"

def test_is_palindrome_basic():
    assert is_palindrome("Race car") is True
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("Bobi") is False

def test_first_unique_char_examples():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
