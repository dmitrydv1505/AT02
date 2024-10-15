
import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("BCDFG") == 0

def test_mixed_strings():
    assert count_vowels("hello world") == 3
    assert count_vowels("PyThOn PrOgRaMmInG") == 4
    assert count_vowels("") == 0  # тест для пустой строки