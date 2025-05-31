import pytest


from um import count


def test_count_um_only():
    assert count("Um") == 1


def test_count_um_one_punct():
    assert count("Um?") == 1


def test_count_two_um():
    assert count("Um, ehm, um.") == 2


def test_count_um_multiple_punct():
    assert count("Um...") == 1


def test_count_um_in_word():
    assert count("Mums") == 0
