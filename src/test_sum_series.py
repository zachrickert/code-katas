"""Test  file for sum series."""
import pytest


def test_sum_series_n1():
    from sum_series import series_sum
    assert series_sum(1) == "1.00"


def test_sum_series_n2():
    from sum_series import series_sum
    assert series_sum(2) == "1.25"


def test_sum_series_n3():
    from sum_series import series_sum
    assert series_sum(3) == "1.39"


def test_sum_series_n0():
    from sum_series import series_sum
    assert series_sum(0) == "0.00"
