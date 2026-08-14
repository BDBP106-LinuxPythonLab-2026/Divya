#!/bin/bash

echo "filename:"
read filename
if [ -f "$filename" ]; then
	if [ -x "$filename" ]; then
		echo "file exist and is executable"
	else
        echo "file exist but not executable"	
	fi
else
echo "file absent"
fi	
