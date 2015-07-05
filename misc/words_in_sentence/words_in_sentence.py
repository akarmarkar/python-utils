#!/usr/bin/python
from __future__ import print_function

#Write   a   script  in  Python  that:
#    Reads   from    input   one sentence    per line    (e.g.,  'This   is  a   short   sentence.') .
#    Prints  out a   one line    per input   sentence    consisting  of  the number  of  characters  in  each
#    word    (excluding  punctuation),   with    spaces  separating  the numbers.    (e.g.,  '4  2   1   5   8').
#    Valid   input   characters  are a-z A-Z,    0-9,    single  quote,  double  quote,  period, comma   and
#    exclamation point

import sys

def word_count(line):
    print("line=",line)
    for word in line.split():
        print(len(word))

if __name__ == "__main__":
    word_count(sys.argv[1])
