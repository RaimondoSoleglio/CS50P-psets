import pytest

from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9:00 AM") == "17:00 to 09:00"


def test_midnight_convert():
    assert convert("12 AM to 12:00 PM") == "00:00 to 12:00"


def test_error():
    with pytest.raises(ValueError):
        convert("9am to 5pm")


def test_error_wrong_time():
    with pytest.raises(ValueError):
        convert("29 AM to 5 PM")


def test_error_omission():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
