#!/bin/bash


echo "enter argument:"
read a
read b
read c
read d
var1=$a
var2=$b
var3=$c
var4=$d
var5=$($var1 + $var2 + $var3 + $var4)
if [ $var5=4 ]; then
	echo "all arguments exist"
        echo "argument1:" $a
        echo "argument2:" $b
        echo "argument3:" $c
        echo "argument4:" $d
else 
	exit 5
fi 


