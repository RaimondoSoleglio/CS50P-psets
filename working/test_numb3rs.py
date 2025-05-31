import pytest


from numb3rs import validate


def test_validate():
    assert validate("0.0.0.0") == True


def test_validate():
    assert validate("cat") == False

def test_validate():
    assert validate("140.100.235.144.234") == False

def test_validate():
    assert validate("140.300.300.300") == False
    assert validate("0.0.0.0.0") == False


