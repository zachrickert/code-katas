# -*- coding: utf-8 -*-
"""Return a set number of autocompletions"""

from trie import Trie

class AutoCompleter(Trie):
    """The Autocompleter class."""
    def __init__(self, my_input, max_completions=5):
        """
        Initialize the the class with the super class functions.
        Max_completions are the number of completions to return.
        Load will load the vocabulary into the trie.
        """
        super(AutoCompleter, self).__init__()
        self.load(my_input)
        self.max_completions = max_completions

    def __call__(self, start):
        print(self.complete_me(start))

    def complete_me(self, start):
        """Returns a list of posible completions."""
        return_list = []
        i = 0
        for word in self.traversal(start=start):
            if i < self.max_completions:
                return_list.append(word)
                i += 1
            else:
                return return_list
        return return_list
