#!/bin/sh
# List the files included by the C sources files included as arguments

for file in *.c; do
    echo "$file includes:"
    grep -E '^#include' "$file" |
    sed 's/>.*$//' |
    sed 's/^.*</\t/'
done