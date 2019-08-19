#!/bin/bash

#print a random word from file

for ((i=1; i<=$1; i++))
do
	# $RANDOM is a random number every time	
	a="$RANDOM"
	p='p'
	c="$a$p"

# print a word at line randomly calculated
sed -n $c /usr/share/dict/american-english

done
