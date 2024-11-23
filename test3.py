import pytest
from lesson_AT02 import count_vowels

def test_only_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_mixed_string():
    assert count_vowels("Hello World!") == 3
    assert count_vowels("PyThOn") == 1
    assert count_vowels("Beautiful Day!") == 6

def test_empty_string():
    assert count_vowels("") == 0

def test_vowels_with_spaces():
    assert count_vowels(" a e i o u ") == 5

def test_vowels_with_numbers_and_symbols():
    assert count_vowels("123@aei!") == 3