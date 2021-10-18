# Python assignment 4, Data Science for Biology
## Topics to cover
- Working with files: Input/Output
- `for` loops, processing files one line at a time.
- using `.readline()` within `for` loops to process one line at a time.
- Regular expressions to find exact matches, and to find varible length repeat matches.
- `sys.argv`, `re.search`
<p>&nbsp;</p>

# Summarizing DNA sequence motifs in genomes‬‬‬‬‬‬
‬
This week we will work with DNA sequence data from several different species. These are coding DNA sequences, and happen to be from a bird (Manacus vitellinus; Manacus_vitellinus.gene.cds.fa.gz) and two pines (Pinus contorta; contorta_454.fa.gz, and Pinus taeada; Pta.seq.uniq.gz). You can pull these from the course website (you will need to `gunzip` them). The data sets are either from whole genome or whole transcriptome sequencing projects, and represent most of the protein coding sequence.
<p>&nbsp;</p>

### **Task 1**: write a script that counts the number of restriction enzyme cut sites in the genome assemblies. We are going to look for three DNA sequence motifs that are represented by the exact DNA sequences:

- EcoRI cut site: GAATTC
- Mse1 cut site: TTAA
- HindIII cut site: AAGCTT

Print to screen or write to an outfile that contains a report with several features of this data set:

1. The total number of sequences in each file. (hint: Ctr += 1)

2. The number of EcoRI, MseI, and HindIII restriction enzyme cut sites. This will involve counting the number of exact matches for the cut site sequences in each line, and summing that over all of the lines. The primer for this week and one of the slides from class has an example of how to keep count of multiple regular expression matches in a scalar, and another slide has an example of how to add these counts onto a total with each iteration through a for loop.
<p>&nbsp;</p>

### **Task 2**: Here we want to use some more flexible regular expressions to find and count all of the microsatellite loci that represent several types of repeats in these files. Microsatellites or simple sequence repeats (SSRs) are long stretches of repetitive DNA that are often targeted for genotype development to their high polymorphism levels. A simple microsatellite would be a long stretch of AT repeated: 
## ATATATATATATATATATATATATATAT...........
<p>&nbsp;</p>

Your script should 

1. Count the number of AT (dinucleotide) microsatellites that have at least 4 repeats.
2. Count the number of ATC (trinucleotide) microsatellites that have at least 4 repeats.
3. Count the number of GA (dinucleotide) followed by anything microsatellites with at least 4 repeats

4. Let’s say we are not only counting SSRs, but that we want to build primers or DNA baits to specifically genotype SSR regions in these genomes. To do this, we would want to identify the SSRs, but then also write to a different file all of the sequences containing SSRs. So, the sequences containing SSR, along with their Fasta identifier lines (those starting with ">") matches should be written to a file.


Hints: 

1). This will involve using a regular expression that has a more flexible match. The primer for this week as well as one of the slides from class illustrate examples for this type of expression.
2. You will need to process 2 lines each round through a for loop. Below is a hint on how to do this:

    for Line in IN:
	    Line = Line.strip("\n")
	    Fasta = Line
	    Seq = IN.readline()
	    Seq = Seq.strip("\n")

The above code will efficiently process lines of data in pairs. So, for alternating lines that look like:

	>seq2.prot.hox3 pos:1122424444
	ATATATATCGGGCGTAAAATGGCGCTAGTTTGGGCCAATATTTTTTTAAAAAAAAAAAAAAAAAAAAA

The first line will be stored in the Fasta variable, and the second line will be stored as Seq. Thus, each time through IN, two lines will be processed. One with the fasta ID, and one with the DNA sequence content.

<p>&nbsp;</p>

### **Extra optional task**: Modify you script to read in as many .fasta files as you want to feed it, and write a report file that summarizes the number of restriction enzyme cut sites as in A and the number of microsatellite repeats as in B for each input file. In this case, you want to be able to feed it the three data sets that I provided on the course website. So, you should be able to process from the command line as:

$ python cutsite_micro_multi_exportSSR.py Manacus_vitellinus.gene.cds.fa contorta_454.fa Pta.seq.uniq.fa

