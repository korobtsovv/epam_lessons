#!/bin/bash

while true; do
	read command
	case $command in
		ls*) eval "$command" ;;
		pwd) pwd ;;
		hi) echo "Hello `whoami`" ;;
		exit) break ;;
		*) echo "Wrong command! Use: ls/pwd/hi/exit" ;;
	esac
done
