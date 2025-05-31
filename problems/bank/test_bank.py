import pytest

from bank import value


def test_value():
    #  multiple tests
    assert value("hello") == 0
    assert value("Hi") == 20
    assert value("CiAo23") == 100
