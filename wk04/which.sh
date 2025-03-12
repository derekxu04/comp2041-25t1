#! /bin/dash

for program in "$@"; do 
    directories="$(echo "$PATH" | tr ':' ' ')"
    for directory in $directories; do 
        path="$directory/$program"
        
        if test -x "$path"; then 
            ls -ld "$path"
        fi
    done
done 