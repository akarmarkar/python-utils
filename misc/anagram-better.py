#!/usr/bin/python

import sys
from copy import deepcopy
       

def letter_counts(word):
    d = {}
    for c in word:
        d[c] = d.get(c,0) + 1

    return d

def is_anagrams(words):
    print "words=",words
    # lcd = letter count dict
    # lcd = { words[0]: letter_counts(words[0]) }
    lcd = {}

    for word in words:
        lcd[word] = letter_counts(word)

    # compare dicts
    print "lcd=", lcd
    base_word,base_lcd = lcd.popitem()
    print "base_word=",base_word,"base_lcd=",base_lcd

    for word,lcd in lcd.items():
        if lcd == base_lcd:
            print "lcd=",lcd,"base_lcd=",base_lcd,"Offending word is ",word
            return False

    return True

if __name__ == "__main__":
	print is_anagrams("cinema","iceman")
    print is_anagrams(sys.argv[1:])

