#! /usr/bin/env dash

top_and_bottom() {
    # $1 = filename
    echo "================="
    echo "$1"
    echo "-----------------"
    head -1 "$1"
    tail -1 "$1"
    echo "================="
}

for file in "$@"; do 
    top_and_bottom "$file"
done
