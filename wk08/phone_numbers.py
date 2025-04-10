#!/usr/bin/env python3

import sys, subprocess, re

url = sys.argv[1]

process = subprocess.run(f"wget -q -O- {url}", shell=True, capture_output=True, text=True)

output = process.stdout

for match in re.findall(r'\d+', output):
    print(match)
