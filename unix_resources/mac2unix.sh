#!/usr/bin/bash


# usage: $ mac2unix.sh file_with_maclineendings.txt

cat $1 | tr '\r' '\n' > u_$1
