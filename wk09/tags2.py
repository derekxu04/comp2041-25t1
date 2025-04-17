#! /usr/bin/env python3

# fetch specified web page and count the HTML tags in them

import sys, subprocess, re
from collections import Counter
from argparse import ArgumentParser

def main():
    parser = ArgumentParser() 
    parser.add_argument("-f", "--frequency", action="store_true", help="print tags by frequency")
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    # Fetch html
    process = subprocess.run(["wget", "-q", "-O-", args.url], capture_output=True, text=True)
    webpage = process.stdout

    # Extract tags
    tags = re.findall(r"<(\w+)", webpage)

    tags_counter = Counter(tags)
    # print(tags_counter)

    if args.frequency:
        for tag, count in reversed(tags_counter.most_common()):
            print(f"{tag} {count}")
    else:
        for tag, count in sorted(tags_counter.items()):
            print(f"{tag} {count}")

    # tags_counter = Counter()
    # for tag in tags:
    #     tags_counter[tag] += 1
    
    # print(tags_counter)

if __name__ == "__main__":
    main()