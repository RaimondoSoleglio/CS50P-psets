import pytest

from twttr import shorten


def test_shorten():
    #  remember to handle multiple cases
    assert shorten("BoOb") == "Bb"
    assert shorten("1BoOb.") == "1Bb."
