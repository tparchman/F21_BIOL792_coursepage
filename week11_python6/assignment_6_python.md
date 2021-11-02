# Python assignment 6, Data Science for Biology
## Topics to cover
- Working with files: Input/Output
- Dictionaries
- More regular expressions
<p>&nbsp;</p>

### I. Intro to dictionary assignment. 
The purpose of this problem is for you to learn and practice how to assign keys and values to a dictionary, to use some dictionary functions to demonstrate that your dictionary is working, and to print out some useful information. We are first going to use the file SG_ref.fasta that is available on the course website. Read in the SG_ref.fasta file from `sys.argv[]` and try the following:
<p>&nbsp;</p>

A. You will want to use a `for` loop to go through your file line by line, but for this problem, you will want to access two lines at a time. This is a fairly common situation (and one we have seen before) and here is a hint on how to do this:

    for Line in IN:
        ID = Line
        Seq = Line.readline()


	
While executing the `for` loop, make one dictionary that has the fasta ids (the line that starts with `>`) as keys, and the sequences themselves as values (Seq as above).  Inside the same loop make a separate dictionary that has the fasta ids as keys and the sequence length as a value (remember that calculating the length of a scalar is easy). Now you should have two dictionaries, and you could do some things with either or both of them.

B. Use the `keys` function to put the keys for your dictionaries into their own lists and print those arrays to make sure your dictionaries are set up the way you want them to be set up. 

C. Use a `for` loop to go through your dictionary and then to print out the fasta Ids and their associated sequence length to an outfile.  This file should have a line for each key-value pair, that is each line should start with a sequence id, which should be followed by the length of the sequence associated with that id.

D. Now use a `for` loop to print out the dictionary in the same way as above, except in this case we want the keys sorted and the dictionary printed in sorted order. What does the difference between these two outputs (C and D) tell you about how dictionaries are organized?

<p>&nbsp;</p>

### II. Bonus task

Have a look at the sample_passerina.fastq.gz file we worked with early in the semester. This file has raw DNA sequencing data from an Illumina machine, each sequence with data organized into four lines (an id line, a sequence line, an additional id line, and a quality score line). The ids in this file represent individual birds (*Passerina amoena*), and there are many sequences for each individual bird. See if you can figure out how to use a dictionary to count the number of sequences associated with each individual in this file. This would involve buidling a dictionary where individual IDs (lines that start with "@") and the values represent the number of sequences that are incremented each time the same key is read.





