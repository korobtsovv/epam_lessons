#!/bin/bash

argall=( "$@" )
array=()
argnum=1
for arg in ${argall[@]}; do
	echo "Arg$argnum: $arg"
	echo
	prev=$arg
	if [ $argnum -eq $# ]; then
		next=${argall[0]}
	else
		next=${argall[$argnum]}
	fi
	sum=$((prev + next))
	array+=($sum)
	((argnum++))
done

echo ${array[@]}
echo
