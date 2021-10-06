# Python assignment 2

## Topics to cover
- More string operations
- lists
- conditionals
- for loops

<p>&nbsp;</p>


## 1. A bit more string work. This problem involves working with a DNA sequence that has some information in front of it. To start your program, type (or copy) this line into your program and assign it to a string.

    DNA_Info = 'SAMPLE_110 Pop3 atatctcgcggggtttatatatattatttaaa'

Note: Chapter 8 of Haddock and Dunn walks you through a number of very similar examples for working with DNA sequences.

A. Get rid of everything other than the DNA sequence (using `str.replace`), and save this to another string.

<p>&nbsp;</p>


B. Change the DNA sequence string to contain uppercase rather than lower case. 
<p>&nbsp;</p>

C. Count the number of Gs, Cs, Ts, and As in the DNA sequence, calculate and print out the GC content of the sequence (Number of C and G bases divided by total sequence length)
<p>&nbsp;</p>

D. Reverse the order of the DNA sequence. There are two ways to reverse strings, one involves turning the string into a list, using `.reverse` (which only works with a list), then turning the list back into a string. The other way is much simpler to type, but it looks wierd (It uses slices), as below.
    
    Seq='ATCGGGGGG'
    Rev = Seq[::-1]

<p>&nbsp;</p>

## 2. Here we are going to practice manipulating a simple list. Execute the tasks for each letter in one script and provide informative print statements to track your progress. Lets start with a single scalar:

    DNA_Seq = 'A,C,G,T,A,A,A,T,G,C,C,A,T,G,C,C,G,G,A,A,T,C,G,A,T,T,T'

A. Work with DNA_Seq above, which is currently a string. Often you will read in large files of ',' separated values one line at a time. One way to extract items from that line (or the thousands that may follow) is to split the string based on ',' and create a list out of the line. This way, you can easily use list indeces to work on specified “columns” of data, or you can loop through the list with something like `for` in order to perform the same task on each list element. Use `str.split` to turn this string into an list where each element is something contained between the commas. Note that if you were to try to use `list()` to convert the string to a list, you would end up with commas as additional list elements.
<p>&nbsp;</p>

B. Note that `.join` is the opposite of `str.split`, and can be used to turn an list back into a string. The syntax is a bit different for `.join`, where the delimiter must be specified before the `.`. This is a task you might routinely encounter. Use `.join` to turn the list you made above back into a comma delimited string.
<p>&nbsp;</p>

C. Lets go back to the list you made in A. Add the an additional list, specified below, to the end of the first list (essentially, concatenate the two DNA sequences together.

    SeqList2 = ['A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T']

D. Make a new list that only contains the first 10 bases of the list you made in C.
<p>&nbsp;</p>

E. How long is the list now? Print the length of the list, but use an `if` statement to do this only if the length is greater than 8. Then try to double the 8 to 16, to verify that you can write `if` and `else` conditionals that are doing what you want.
<p>&nbsp;</p>

F. Print the final list in reverse order.  
<p>&nbsp;</p>


## 3. Lets try something else with lists, `for`, and some conditional statements.
<p>&nbsp;</p>

A. Make a list simple list of integers, starting with 1 and going to 100
    
    NumList=list(range(1,100))


B. Using a `for` loop, print each value, a comma, the value multiplied by 2, a comma, the element that value occupies in the list, a comma, and whether the original number is even or odd. Each line of output should look like (for the first element, 1):

## 1, 2, 0, odd
<p>&nbsp;</p>

Hints: 

	 
- You will want to increment a variable each time through the loop to record array index. See the last section of the primer for this week for an example. This is done using something like `CTR+=1` So, each time through `for` the value of CTR will grow by one. By initializing `CTR=0` outside the loop, and incrementing it inside the loop, you can correctly associate each run through the list with the correct list index (e.g., the first time through the list ).

- The modulo operator `%` returns the remainder of division. You can use this to mathematically test whether a value is even or odd. You can use this in with `if` to determine if a value is even or odd. For example:

    > 4%2 will return 0

    > 4%3 will return 1


<p>&nbsp;</p>

C. When we are printing straight to the screen, we refer to this is standard out. Often you will want that information, especially when there is a lot of it, written to a file instead. Rather than printing this output to the screen, use unix redirection (like you did before we started perl) to write the output to a file.
