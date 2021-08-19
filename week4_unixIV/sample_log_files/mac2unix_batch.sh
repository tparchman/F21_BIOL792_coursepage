#!/bin/bash
echo $@
echo $1
echo $2
for file in $@; do
cat $file | tr '\r' '\n' > unix_$file
done 