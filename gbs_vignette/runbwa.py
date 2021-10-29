#!/usr/bin/python
#JJ&TF 11/12/2020

## run bwa aln and samse on fastq files passed from the commandline
##note -n set to 5 for symphonia due to high divergence

## USAGE: python runbwa.py /fullpath/to/files/*fastq

import sys,os,re

fastq_files = sys.argv[1:]

assert fastq_files, 'Need to provide /fullpath/to/files/*fastq'

print('\nAligning ',len(fastq_files),' to reference assembly\n')

# makes a sam_sai directory for output files if doesn't exist already
# NOTE: will create and output files where ever you run this script
if os.path.isdir('sam_sai') == False:
    os.mkdir('sam_sai')

for file in fastq_files:
	fastq = re.search('([-\w\.]+)\.fastq$',file).group()
	name = fastq.split('.')[0]
	print("Mapping reads for.....",name)
	
	bwa_arg1 = 'bwa aln -n 4 -l 20 -k 2 -t 22 -R 20 -q 10 -f sam_sai/aln_%s.sai sheep_ref %s' % (name,file)
	bwa_arg2 = "bwa samse -n 1 -r \'\@RG\tID:LOC_%s\' -f sam_sai/aln_%s.sam sheep_ref sam_sai/aln_%s.sai %s" % (name,name,name,file)
	
	os.system(bwa_arg1)
	os.system(bwa_arg2)