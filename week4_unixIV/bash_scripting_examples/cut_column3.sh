#!/bin/bash
## cut_column3.sh
## description: cuts 3rd column from any number of input files
## usage: bash cut_column3.sh STDIN


for myfile in $@; do
cut -f 3 $myfile &> column3_$myfile
done

