#!/bin/bash

in=$1
out=$2

while read line; do
    range=`echo "$line" | cut -d ' ' -f 1`
    content=`echo "$line" | cut -d ' ' -f 2-100`

    if [[ ${range:0:1} = [[:digit:]] ]]; then
        start=`echo "$range" | cut -d '-' -f 1`
        stop=`echo "$range" | cut -d '-' -f 2`
        for i in $(eval echo {$start..$stop}); do
            echo "$content" >> $out
        done
    else
        echo "$line" >> $out
    fi
done < $in