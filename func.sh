#!/usr/bin/env bash

function addone () {
	local FUNC="$@"
	$FUNC
	expresult=$?
	total=$(( expresult+1 ))
	echo $total
}

function exp () {
	local result=$(( $1**2 ))
	return $result
}

for i in $@; do
	addone exp $i
	echo
done
