#!/bin/bash

sum=0
for arg in $@; do
        sum=$(( $sum + $arg ))
done

echo "Sum $sum"
echo "Args number $#"
echo "Result $(( $sum / $# ))"
