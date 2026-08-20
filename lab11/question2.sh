#!/bin/bash


if [ -f listoffiles ]; then
	echo " the file exist"
else 
echo " the file is absent"
fi


if [ -f filenew ]; then
	echo " the file exist"
else 
echo "the file dont exist"
fi


if [ -s listoffiles ]; then
	echo " the file has contents"
else
echo "the file is empty"
fi


if [ -e listoffiles ]; then
	echo "file exists"
else
echo "file absent"
fi
