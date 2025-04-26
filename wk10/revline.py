#!/usr/bin/env python3

"""
Write a Python script revline.py that reverses the fields on each line of its standard input.
"""

import sys

for line in sys.stdin:
    if line[-1] == '\n':
        line = line[:-1]

    words = line.split(' ')

    print(" ".join(words[::-1]))

    # s = ""
    # for word in words[::-1]:
    #     s += word
    #     s += ' '
    # print(s)