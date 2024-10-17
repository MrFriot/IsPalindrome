# -*- coding: ascii -*-
# by mrfriot

import tests
import functions as funcs


def main():
    tests.test()
    print("[!] START WORK")
    word = "Hello, world!"
    print(f"[*] Word: \"{word}\"")
    print(f"[*] Reverse: \"{funcs.reverse_word(word)}\"")
    print(f"[*] \"{word}\" is{'' if funcs.is_palindrome(word) else " not"} palindrome")
    word = "aboba"
    print(f"[*] Word: \"{word}\"")
    print(f"[*] Reverse: \"{funcs.reverse_word(word)}\"")
    print(f"[*] \"{word}\" is{'' if funcs.is_palindrome(word) else " not"} palindrome")
    word = input("[*] Your word: ")
    print(f"[*] Reverse: \"{funcs.reverse_word(word)}\"")
    print(f"[*] \"{word}\" is{'' if funcs.is_palindrome(word) else " not"} palindrome")
    print("[!] END WORK")


if __name__ == "__main__":
    main()
