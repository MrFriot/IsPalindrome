# -*- coding: ascii -*-
# by mrfriot


def reverse_word(word: str) -> str:
    """Return word in reverse"""
    return word[::-1]


def is_palindrome(word: str) -> bool:
    """If the word is a palindrome, it will return True, otherwise False"""
    return True if reverse_word(word) == word else False
