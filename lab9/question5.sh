#!/bin/bash

echo $0
name=$1
age=$2

echo $1
echo $2

echo "The number of arguments passed to this script: $#"
echo $@
#we can store the arguments in array by enclosing $@ within ()
listofarg=($@)
#recall elements like any other array
echo ${listofarg[0]}

