#!/bin/bash

echo "filename:"
read filename
if [ -f "$filename" ]; then
	if [ -x "$filename" ]; then
		echo "file exist and is executable"
	else
        echo "file exist but not executable"
        exit 200	
	fi
else
echo "file absent"
exit 201
fi	
