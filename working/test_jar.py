import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(5)
    assert jar.size == 6

    with pytest.raises(ValueError):
        jar.withdraw(7)
