import pytest
from task3 import count_vowels

def test_only_vowels():
    # Тест для строки, состоящей только из гласных (должно вернуть 10)
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    # Тест для строки без гласных (должно вернуть 0)
    assert count_vowels("bcdfg") == 0

def test_mixed_string():
    # Тест для строки с гласными и другими символами
    assert count_vowels("Hello World!") == 3  # "e", "o", "o"
    assert count_vowels("PyThOn") == 1        # "O"
    assert count_vowels("Beautiful Day!") == 6  # "e", "a", "u", "i", "a", "y"

def test_empty_string():
    # Тест для пустой строки (должно вернуть 0)
    assert count_vowels("") == 0

def test_vowels_with_spaces():
    # Тест для строки с гласными и пробелами (должно вернуть 5)
    assert count_vowels(" a e i o u ") == 5

def test_vowels_with_numbers_and_symbols():
    # Тест для строки с гласными, числами и символами (должно вернуть 3)
    assert count_vowels("123@aei!") == 3