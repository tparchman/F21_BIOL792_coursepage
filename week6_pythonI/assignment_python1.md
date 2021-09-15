# Python assignment 1

## Topics to cover
- Getting started
- Basic mathematical operations
- String operations
- `input()`, converting strings to floats, float precision

<p>&nbsp;</p>

# Writing some of your first Python scripts to play with scalars and scalar functions.

Before working through the below exercises, make sure to have read chapter 8, and built the specified python script as demonstrated in the chapter. This will give you some good experience/practice with assigning scalar variables and using some string functions.

### 1. In addition to standard mathematical operators, the following are commonly useful. Make sure you understand what they do. Note that += will work with strings, the others will return undefined.


    +=      *= 	    -= 	    /=	   

 ### Write a script that assigns integers, floats, and strings to some variables (perhaps as illustrated below), and test each of the above operators. Use print statements to allow you to track what is happening in your script(s).

    Int_a = 7
    Int_b = 3
    Int_c = 2
    Float1 = 3.33
    Name1 = 'shipley'
    Name2 = 'dog'

<p>&nbsp;</p>

### 2. Write a program that uses `input()` to prompt the entry of a string and an integer and then prints out the string the number of times indicated by the number on separate lines.  If the user enters “fred” and “3”, the output should be: fredfredfred. If the user enters “fred” and “299792,” there would be a lot of output.
<p>&nbsp;</p>

### 3. Write a python script to calculate expected genotype frequencies in a population under Hardy Weinberg Equilibrium based on known allele frequencies at a gene with TWO alleles. As a reminder, a population under Hardy-Weinberg equilibrium has 3 genotype frequencies predictable from allele frequencies (p and q; p + q = 1):
<p>&nbsp;</p>

### p**2 + 2pq + q**2 = 1
<p>&nbsp;</p>

### Each of the 3 terms above represent the genotype frequencies (AA [p**2], Aa [2pq], aa [q**2)]). In other words, p**2 is the predicted frequency of the first homozygous genotype, 2pq is the predicted frequency of heterozygotes, and q**2 is the predicted frequency of the second homozygous genotype. Your script should require the entry of values p and q, and should print the calculated values of each expected genotype.
<p>&nbsp;</p>

### A couple of points here:

- The program should use the `input()` function to prompt for the command line entry of two values (p and q; really you only need to supply one value because they must sum to 1) from the command line.

- Depending on how you enter a number with a decimal, such as 0.8, python may automatically call this a string. If so, you will need to convert this to a float before performing mathematical operations.

- You may also notice that the precision, and the number of digits after the decimal, for p\*\*2, 2pq, q\*\*2 will be excessive. Control the precision of the floats you print so that they only have *2 digit*s after the decimal (e.g., 0.66). For this you should use the `%` operator (e.g., `%.2f`)