#!/usr/bin/env python3

"""
print words in file 1 but not file 2
"""

import sys

# ./missing_words file1 file2

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    words1 = set()
    with open(file1, 'r') as f:
        for line in f:
            words1.add(line.strip())

    words2 = set()
    with open(file2, 'r') as f:
        for line in f:
            words2.add(line.strip())

    for w in sorted(words1 - words2):
        print(w)

if __name__ == "__main__":
    main()