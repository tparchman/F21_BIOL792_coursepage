#!/bin/bash
## file_preview.sh, takes a list of files as arguments. Prints file name and first five lines of each file to screen
## usage: bash file_preview.sh STDIN


for myfile in $@; do
echo $myfile:
head -n5 $myfile
done


