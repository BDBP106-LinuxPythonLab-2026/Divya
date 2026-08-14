#!/bin/bash


echo 'Enter a number:'
read number

if [ $number -lt 0 ]; then
	echo "$number number is negative"
elif [ $number -gt 0 ]; then
        echo "$number number is positive"
else 
echo "number is zero"
fi

