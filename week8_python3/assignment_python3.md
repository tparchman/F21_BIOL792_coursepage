# Python assignment 3

## Topics to cover
- Working with files: Input/Output
- More with lists
- `sys.argv`, `re.search`
- `for` loops, processing files one line at a time.

<p>&nbsp;</p>


### This week you will work more with lists, and more importantly, will get comfortable reading IN and writing OUT. We are not literally reading in the contents of entire files at once, rather we are making connections (file objects or handles) between our program and these files. For each problem you will need to use a `for` loop to read data in one line at a time. The python_3_primer.md and slides from class should help to get you started.
<p>&nbsp;</p>

1).Read in the input file **genenames.txt** line by line, and add the values from the second "column" of each line to a list. This file has two columns, the second of which lists gene names. Print the list to check that your script has worked. The output should be the second "column" of the file genenames.txt.
<p>&nbsp;</p>

**Hints**: You might want to use two lists, the first of which might be created by splitting each line into a list so that you can extract the second element from it. 2. You may need to ‘add’ elements to the second list (using `.append`) with each iteration of a while loop.

<p>&nbsp;</p>

2.) Now write a similar script to read the data in flies.txt. This file has three columns: fly number, day or night, and seconds of flying time recorded. You want to read in the seconds of flying time into an list, but ONLY for the night-time values. Write the information in this list to an outfile. This problem is similar to number 1, but is asking you add (maybe using the list function `.append`) a value onto a list if a different column in the file has a certain condition (N in this case). Instead of hardcoding the file name into your script, use `sys.argv` to open a file object from the command line. You may want to initialize your list before you get into the for loop.
<p>&nbsp;</p>

3.) Some practice working with DNA sequence data. Here we are going to process a fasta file (no60_intron_IME_data.fasta) containing DNA sequence data for 59,260 intron sequences You will need to calculate some summary information for each sequence, and to write that information to a file that you are going to create in your script. 

Instead of hardcoding the file name into your script, use `sys.argv` to open a file object from the command lineWrite to an output file:

**A. the id lines**

**B. the length of each sequence**

**C. the GC content of each sequence (remember, GC content is simply the proportion of bases in a DNA sequence that are either G or C).**

**Lastly have your program print to screen the number of DNA sequences (use incrementing, e.g., TotalSeq += 1, for each time you process a DNA sequence) in the no60_intron_IME_data.fasta file and the average GC content over all of the sequences.**

**Hints:**

1). Use a `for` loop to process the file one line at a time. You may want to remove the line endings, but then you can accomplish your goals by just working with each line as a string. 

2). If you remember, `str.count('G')`, for example, can be used to count the number of Gs in a string of DNA sequence data. 

3). `+=` will be useful, as you will want to keep a running total of a few variables each iteration through your for loop in order to get the total counts of C and G and the total equence length necessary for calculating the GC content for ALL sequences in the file together. 

4).Each ID line starts with a ">". You will not want to perform any calculations on this line, but will want to print it to OUT. Hence you will need to recognize lines that start with ">".  A regular expression can do that for you. Maybe something like:

    if re.search("^>", DNAseq):

For lines that start with A, T, C, or G, you will want to do something else.

5).To calculate the GC content for teh entire collection of sequences, you will want to keep a running total of the counts of A, T, G, and C, as well as the total sequence length, and then perform a calculation on those running sums *outside of the `for` loop.*
