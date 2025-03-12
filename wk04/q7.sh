#! /bin/dash

acc z5417087 | 
sed -n '/^$/,/^$/p' | 
cut -d: -f2 | 
sed -nE 's/^.*([A-Z]{4}[0-9]{4})t[1-3]_Student.*$/\1/p'