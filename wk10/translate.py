#!/usr/bin/env python3

import sys

lower_case = "aeiou"
upper_case = "AEIOU"

def main():
    for line in sys.stdin:
        # translated_line = ""
        # for char in line:
        #     if char in lower_case:
        #         translated_line += char.upper()
        #     elif char in upper_case:
        #         translated_line += char.lower()
        #     else:
        #         translated_line += char
        
        # print(translated_line, end='')

        translate_table = str.maketrans(lower_case + upper_case, upper_case + lower_case)

        print(line.translate(translate_table))

    

if __name__ == '__main__':
    main()