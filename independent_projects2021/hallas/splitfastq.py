#!/usr/bin/env python3

### Written by jhallas.  splits clean fastq into individual specimen fastqs.  
### Need two input files (barcode ID (single column, format = .txt); cleaned fastq file)
### Resulting fastqs can then be used for downstream analyses 

### USAGE: python splitfastq.py BARCODE_ID.txt CLEAN.fastq

import sys
import itertools
import os

cwd = os.getcwd() # saves current working directory

if os.path.isdir('split_fastqs') == False: # creates fastq directory
    os.mkdir('split_fastqs')

IDfile = open(sys.argv[1], 'r').readlines() # opens in barcode ID file

for ID in IDfile:       # loops through barcode ID file
	ID = ID.strip('\n') # strips line endings from barcode ID file

	print(ID)           # prints specimen to screen currently being processed

	chunksize = 1000    # chuck sets a limit on how many characters (=default; will change 
						# to number of lines at line 30).  read.lines() is not used 
						# because it "explicitly guarantees that it reads the whole file 
						# into memory."  This shouldn't be done with fastq files because 
						# they can be HUGE. There are probably different packages that are 
						# designed for fastq files.
						# !!!!! IF ERROR OCCURS.  NUMBER NEEDS TO BE DEVISIBLE !!!!! 
						# !!!!! BY 4 AND SMALLER THAN THE NUMBER OF LINES IN   !!!!!
						# !!!!! THE CLEAN FASTQ FILE                           !!!!!

	with open(sys.argv[2], 'r') as Seqfile: # opens cleaned fastq sequence file

		while True:
			read_data = list(itertools.islice(Seqfile, chunksize)) 
			# uses intertools function islice to change chunksize to number of characters 
			# to line

			if not read_data:
				break
			for i in range(len(read_data)):        # loops through lines from clean fastq
								
				if ID in read_data[i].strip('\n'): # reads and strips line endings from 
                                                   # clean fastq file while matching ID

					mylines = read_data[i:i+4]     # if ID is in this line, this stores 
					                               # that line and the following 3 lines      
					                               # as mylines
					
					os.chdir('split_fastqs')       # changes directory to fastqs
					
					with open('{}.fastq'.format(ID), 'a') as fastq: # opens new ID fastq 
					                                                # file if ID is     
					                                                # matched
					                                                        
						for j in mylines:
							fastq.write(j) # writes out all four lines to new fastq
						
						os.chdir(cwd)  # changes directory back to working