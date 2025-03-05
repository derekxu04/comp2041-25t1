#! /usr/bin/env dash

while read -r id mark _; do
    echo -n "$id "

    if [ "$mark" -eq "$mark" ] 2> /dev/null && [ "$mark" -ge 0 ] && [ "$mark" -le 100 ]; then
        if   [ "$mark" -lt 50 ]; then
            echo FL
        elif [ "$mark" -lt 65 ]; then
            echo PS
        elif [ "$mark" -lt 75 ]; then
            echo CD
        elif [ "$mark" -lt 85 ]; then
            echo DN
        else
            echo HD
        fi
    else
        echo "?? ($mark)" >& 2
    fi
done