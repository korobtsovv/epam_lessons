#!/usr/bin/bash

isnum='^[-]?[0-9]+$'
read x
if [[ $x =~ $isnum ]]; then
	echo good
else
	echo bad
fi

