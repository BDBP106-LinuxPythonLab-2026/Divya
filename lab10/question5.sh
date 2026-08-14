#!/bin/bash



echo "enter the range:"
read n

if [ "$n" -ge 90 ]; then
	echo "A"
elif [ "$n" -ge 80 ] && [ "$n" -le 89 ]; then
        echo "C"
       
elif [ "$n" -ge 70 ] && [ "$n" -le 79 ]; then
        echo "B"
	 	
else
	echo "FAIL"
fi

