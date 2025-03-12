#! /bin/dash

# Print prime numbers less than the specified argument

n=$1 

i=1
while [ $i -lt $n ]; do 
    if ./is_prime.sh $i > /dev/null; then 
        echo $i
    fi

    i=$((i + 1))
done