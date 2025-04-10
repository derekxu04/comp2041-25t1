#!/usr/bin/env python3

"""
count lines of Python source code
"""

from glob import glob

def main():
    total = 0
    for file in glob("*.[ch]"):
        with open(file, 'r') as f:
            lines = f.readlines()

            print(f"{len(lines):7} {file}")

            total += len(lines)
    
    print(f"{total:7} total")
                 
if __name__ == "__main__":
    main()