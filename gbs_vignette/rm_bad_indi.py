#!/usr/bin/python
#JJ&TF 11/12/2020
## command line construction: python rm_bad_indi.py [txt file of ls -l$ *fastq output] [minimum file size (bytes)]

import sys

infile = sys.argv[1]
min_size = int(sys.argv[2])

assert infile, 'Need txt file of ls -l *fastq output'
assert min_size, 'Need minimum file size (bytes)'

IN = open(infile,'r')
OUT = open("bad_indi.txt", 'w')

for Line in IN:
    Line = Line.strip("\n")
    perm,x,user1,user2,size,month,day,time,name = Line.split() #the default in python is to split at whitespace
    if int(size) < min_size:
        OUT.write('%s\n' % (name))
IN.close
OUT.close()