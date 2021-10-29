#!/usr/bin/python
#JJ&TF 11/12/2020

# This script is a wrapper around samtools for batch conversion,
# sorting and indexing of sam file. This version uses fork to split
# the job over multiple processors. Adjust $ncpu for the desired
# number of cpus.

#
# Usage: python sam2bam.py sam_sai/*sam
#

import sys,os,re

sam_files = sys.argv[1:]

assert sam_files, 'Need to provide sam_sai/*sam'

print('\nChanging ',len(sam_files),' sam to bam files\n')

for file in sam_files:
	sam = re.search('([-\w\.]+)\.sam$',file).group()
	name = sam.split('.')[0]
	print("Converting sam to bam.....",name)
	
	sam_arg1 = 'samtools view -b -S -o %s.bam %s' % (name,file)
	sam_arg2 = 'samtools sort %s.bam -o %s.sorted.bam' % (name,name)
	sam_arg3 = 'samtools index %s.sorted.bam' % (name)
	
	os.system(sam_arg1)
	os.system(sam_arg2)
	os.system(sam_arg3)