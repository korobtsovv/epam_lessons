#!/bin/bash

tmp=tmp.txt
echo '' > $tmp

read -r -p "Enter file name: " file
head -c 4KB /dev/urandom > $file
stat=$(($(stat -c %s $file) / 1000))
echo "File '$file' created with size $stat KB"

until [[ $stat -gt 1024 ]]; do
	cp $file $tmp
	cat $tmp >> $file
	stat=$(($(stat -c %s $file) / 1000))
	echo "Filesize: $stat" 
done

echo
rm -rf $tmp
rm -rf $file
echo "Temp files removed"
