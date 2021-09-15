#!/bin/bash
## mac2unix.sh
## description: converts mac (\r) to unix (\n) line endings, writes new file.
## usage: bash mac2unix.sh STDIN


for myfile in $@; do
echo $myfile:
head -n5 $myfile
done


