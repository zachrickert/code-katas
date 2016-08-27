# -*- coding: utf-8 -*-
import pytest

'''First three tests provided by codewars.  Last four I made to test the 
function before being put into codewars.'''

TEST_DECKS = [
    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    (list('Q286JK395A47T'), list('A23456789TJQK')),
    (list('54TQKJ69327A8'), list('A23456789TJQK')),


    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    ([], []),
    (list('33AA3424QKJ6K'), list('AA2333446JQKK')),
    (list('KTAQJ'), list('ATJQK')),
    (list('7'), list('7'))
]

@pytest.mark.parametrize('init_deck, shuffle_deck', TEST_DECKS)
def test_transform_deck_to_ints_aces(init_deck, shuffle_deck):
    from sort_card import sort_cards
    assert sort_cards(init_deck) == shuffle_deck
