#!/usr/bin/env python3

import sys
import re

def main():
    address = sys.argv[1]

    # is address an integer or regex
    try:
        address = int(address)
    except ValueError:
        address = re.compile(address[1:-1])

    for line_number, line_content in enumerate(sys.stdin, start=1):
        if line_content[-1] == '\n':
            line_content = line_content[:-1]

        if isinstance(address, int):
            if line_number == address:
                break
        else:
            if address.search(line_content):
                break
        
        print(line_content)
    
    print(line_content)


if __name__ == "__main__":
    main()
