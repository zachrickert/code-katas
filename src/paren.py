# -*- coding: utf-8 -*-

from linked_list import LinkedList

def check_parens(string_to_check):
    my_list = LinkedList(string_to_check[::-1])
    count = 0

    while True:
        try:
            current_value = my_list.pop()
        except IndexError:
            break
        if current_value == '(':
            count += 1
        elif current_value == ')':
            count -= 1

        if count < 0:
            return -1

    return int(bool(count))
