import pytest
from datetime import timedelta

from seasons import td_to_minutes, minutes_to_literals


def test_convert_date_to_minutes():
    assert td_to_minutes(timedelta(days=17149)) == 24694560
    assert td_to_minutes(timedelta(days=365)) == 525600


def test_convert_minutes_to_literal():
    assert minutes_to_literals(24694560) == "twenty-four million, six hundred ninety-four thousand, five hundred sixty"
    assert minutes_to_literals(525600) == "five hundred twenty-five thousand, six hundred"



