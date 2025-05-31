import pytest

from plates import is_valid

def test_is_valid():
    assert is_valid("mari77") == True
    assert is_valid("aa10") == True
    assert is_valid("1alk1") == False
    assert is_valid("a") == False
    assert is_valid("abcd7e") == False
    assert is_valid("abcd.1") == False
    assert is_valid("aa01") == False
    assert is_valid("10") == False
