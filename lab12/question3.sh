#!/bin/bash


echo "enter a n "
read n
m=1
until [ $m -gt 15 ]
do
	echo "$n * $m = $(( n * m ))"
	m=$[m+1]
done 
