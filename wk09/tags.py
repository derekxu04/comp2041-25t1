#! /usr/bin/env python3

# fetch specified web page and count the HTML tags in them

import sys, subprocess, re
from collections import Counter

def main():
    url = sys.argv[1]

    # Fetch html
    process = subprocess.run(["wget", "-q", "-O-", url], capture_output=True, text=True)
    webpage = process.stdout

    # Extract tags
    tags = re.findall(r"<(\w+)", webpage)

    tags_counter = Counter(tags)
    # print(tags_counter)

    for tag, count in sorted(tags_counter.items()):
        print(f"{tag} {count}")

    # tags_counter = Counter()
    # for tag in tags:
    #     tags_counter[tag] += 1
    
    # print(tags_counter)

if __name__ == "__main__":
    main()