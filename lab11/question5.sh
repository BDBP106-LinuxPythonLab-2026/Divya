#!/bin/bash


val1=Testing
val2=testing
if [ $val1 > $val2 ]
then
	echo " $val1 is greater than $val2 "
else
	echo " $val1 is lesser than $val2 "
fi

#echo "$val1" >testfile
echo " $val2 $val1 "  >>teststringfilie
sort teststringfilie
