#! /usr/bin/env dash

# This program emulates the behaviour of the 'seq' command
# Prints error message and exits if given invalid arguments

if [ $# -eq 1 ]; then
    FIRST=1
    INCREMENT=1
    LAST=$1
elif [ $# -eq 2 ]; then
    FIRST=$1
    INCREMENT=1
    LAST=$2
elif [ $# -eq 3 ]; then
    FIRST=$1
    INCREMENT=$2
    LAST=$3
else
    echo "Usage: $0 [FIRST [INCREMENT]] LAST" >& 2
    exit 1
fi

CURRENT="$FIRST"

while [ "$CURRENT" -le "$LAST" ]; do
    echo "$CURRENT"
    CURRENT=$(( CURRENT + INCREMENT ))
done
