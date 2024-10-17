# -*- coding: ascii -*-
# by mrfriot

import functions as funcs


def test_reverse_word():
    """Testing the reverse_word() function"""
    print("[*] Function docs:", funcs.reverse_word.__doc__)
    # Test even number of symbols
    print("[*] Test 1: ", end='')
    word1 = "hello!"
    result1 = "!olleh"
    print("OK" if funcs.reverse_word(word1) == result1 else "FAIL")
    # Test odd number of symbols
    print("[*] Test 2: ", end='')
    word2 = "world"
    result2 = "dlrow"
    print("OK" if funcs.reverse_word(word2) == result2 else "FAIL")
    # Test palindrome
    print("[*] Test 3: ", end='')
    word3 = "abcba"
    result3 = "abcba"
    print("OK" if funcs.reverse_word(word3) == result3 else "FAIL")


def test_is_palindrome():
    """Testing the is_palindrome() function"""
    print("[*] Function docs:", funcs.is_palindrome.__doc__)
    # Test even number of symbols
    print("[*] Test 1: ", end='')
    word1 = "hello!"
    result1 = False
    print("OK" if funcs.is_palindrome(word1) == result1 else "FAIL")
    # Test odd number of symbols
    print("[*] Test 2: ", end='')
    word2 = "world"
    result2 = False
    print("OK" if funcs.is_palindrome(word2) == result2 else "FAIL")
    # Test palindrome
    print("[*] Test 3: ", end='')
    word3 = "abcba"
    result3 = True
    print("OK" if funcs.is_palindrome(word3) == result3 else "FAIL")


def test():
    print("[!] START TESTING")
    print("[*]", test_reverse_word.__doc__)
    test_reverse_word()
    print("[*]", test_is_palindrome.__doc__)
    test_is_palindrome()
    print("[!] END TESTING")
