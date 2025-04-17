#! /usr/bin/env python3

# fetch specified web page and count the HTML tags in them

import sys, subprocess, re, requests
from collections import Counter
from argparse import ArgumentParser
from bs4 import BeautifulSoup

def main():
    parser = ArgumentParser() 
    parser.add_argument("-f", "--frequency", action="store_true", help="print tags by frequency")
    parser.add_argument("url", help="url to fetch")
    args = parser.parse_args()

    response = requests.get(args.url)
    webpage = response.text

    soup = BeautifulSoup(webpage, 'html5lib')
    tags = soup.find_all()
    names = [tag.name for tag in tags]

    tags_counter = Counter(names)
            
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