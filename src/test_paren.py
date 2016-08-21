# -*- coding: utf-8 -*-

import pytest

TEST_CONDITIONS = [
    ('()', 0),
    ('(())', 0),
    ('(()())', 0),
    (')', -1),
    (')(', -1),
    ('())(', -1),
    ('(', 1),
    ('((', 1),
    ('()(', 1),
    ('', 0),
    ('3 * (5 + 2) / (7 * (1 - 4)) = -1', 0)
]


@pytest.mark.parametrize('init_value, reply', TEST_CONDITIONS)
def test_reply_value(init_value, reply):
    """Check to see if we are getting valid relies."""
    from paren import check_parens
    assert check_parens(init_value) == reply
