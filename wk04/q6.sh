#! /bin/dash

mlalias cs2041.24T2.tutors | 
sed -n '/Addresses/,/Owners/p' | 
head -n -1 | 
tail -n +2 |  
sed -E 's/^\s*//' |
grep -E 'z[0-9]{7}'