# -*- coding: utf-8 -*-
"""Test module for autocompleter."""

VOCAB_LIST = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']

def test_include():
    """Test to see if autocompleter can be included."""
    from autocomplete import AutoCompleter

def test_load_vocab():
    """Test to see if a list of vocab words can be loaded."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(VOCAB_LIST)
    i = 0
    for item in auto.traversal():
        assert item in VOCAB_LIST
        i += 1
    assert i == 8


def test_init_max_completions():
    """Test to see if on init max completions is set to a given number."""
    from autocomplete import AutoCompleter
    my_max = 4
    auto = AutoCompleter(VOCAB_LIST, my_max)
    assert auto.max_completions == my_max


def test_init_max_completions_default():
    """Test to see if on init max completions is set to 5 if not soecified."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(VOCAB_LIST)
    assert auto.max_completions == 5


def test_complete_me():
    """Test to see if complete_me function will return a value."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(['apple'])
    assert auto.complete_me('a') == ['apple']


def test_complete_me_not_found():
    """Test to see if complete_me function will return an empty string."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(['apple'])
    assert auto.complete_me('b') == []


def test_complete_me_not_found():
    """Test to see if complete_me function will return an empty string."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(VOCAB_LIST, 2)
    assert len(auto.complete_me('f')) == 2


def test_complete_me_find_all():
    """Test to see if complete_me will return all answers."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(VOCAB_LIST)
    assert sorted(auto.complete_me('fin')) == sorted(['finch', 'final', 'finial'])


def test_complete_me_too_specific():
    """Test to see if complete_me will return all answers."""
    from autocomplete import AutoCompleter
    auto = AutoCompleter(VOCAB_LIST)
    assert auto.complete_me('finally') == []
