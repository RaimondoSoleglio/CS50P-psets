import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("A/B")

