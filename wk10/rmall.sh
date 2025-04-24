#!/bin/sh

# check whether there is a cmd line arg
case $# in
1) # ok ... requires exactly one arg
    ;;
*)
    echo "Usage: $0 dir"
    exit 1
esac

# rm_all_recursive <dir>
#    -> rm_all_recursive <subdir>
rm_all_recursive() {
    local dir

    dir="$1"
    cd "$dir" || return

    for file in .* *; do
        if test -f "$file"; then
            rm "$file"
        elif test -d "$file" && [ "$file" != "." ] && [ "$file" != ".." ]; then
            echo "Delete $file?"
            read -r answer
            if [ "$answer" = "yes" ]; then
                rm_all_recursive "$file"
            fi
        fi
    done

    cd ..
    rmdir "$dir"
}

if ! test -d "$1"; then
    echo "Not a valid directory"
    exit 1
fi

rm_all_recursive "$1"