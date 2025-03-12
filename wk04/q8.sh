#! /bin/dash

mlalias cs2041.24T2.tutors |  
sed -n '/Addresses/,/Owners/p' |  
head -n -1 |  
tail -n +2 |   
sed -E 's/^\s*//' | 
grep -E 'z[0-9]{7}' | 
while read zid; do 
    acc $zid |
    sed -n '/^$/,/^$/p' | 
    cut -d: -f2 | 
    sed -nE 's/^.*([A-Z]{4}[0-9]{4})t[1-3]_Student.*$/\1/p'
done |
sort |
uniq -c |
sort -rn
