# Python primer V, Data Science I, Fall 2020. 

## Topics to cover

- more work regular expressions
- Input/Output: using loops to process many files at once.
- Printing feedback statements using `sys.stderr.write()`

## Useful materials
- Haddock and Dunn chapters and 10, bit of 11 
- updated document that has corrections for python3 where necessary (PythonLesson2_Chapter9.pdf, PythonLesson3_Chapter10.docx)
- regular expression cheat sheet (python-regular-expressions-cheat-sheet-1.pdf)
- [regular expression tester](https://regex101.com).
<p>&nbsp;</p>

## Expanding Input/Output options

We have learned how to use `open()` to make file handles for reading and writing. For individual, or small numbers of files, this is straightforward by now. Over the last two weeks, you might have used statements below to open file handles for reading and writing:

    IN = open(sys.argv[1], 'r')
    OUT = open("myout.txt", 'w')

This week we will start writing code built to process many files at once (as many as you like as a matter of fact). As `sys.argv` itself is a list, we can use `for` to loop through that list, opening each file one at a time, and running whatever code is necessary. This won't actually be that much different than what you had done up until now, as it will just entail writing all of your code to work on each file inside of a `for` loop that works through the input argument list `sys.argv`.

Let's imagine we have a directory with 1000 text files that all end in `.fasta`. We want to write code that works on ALL of these files and can be executed from the command line as:

    $ python fasta_cleaner.py *fasta

## Using `sys.argv` to process multiple files.

Remember, `sys.argv` is simply a list of strings provided on the command line when a python script is executed. For the example below, sys.argv[0] would be `file_proc.py`, `sys.argv[1]` would be `file1.txt`, `sys.argv[2]` would be `file2.txt`, and `sys.argv[3]` would be `file3.txt`. 

    $ python file_proc.py file1.txt file2.txt file2.txt

So, opening file connections to each of those files simply requires a `for` loop to work through `sys.argv[1:]`, where `[1:]` means from the `1` element to the end of the list. Anytime you want to do this, something similar to below will do the trick.

    for filename in sys.argv[1:]:
        IN = open(filename, 'r')

To build on the above example, lets look at some  code which illustrates how to open file connections in a `for` loop using `sys.argv`, and then looping through each file, one line at a time. I have added the print statement below in order to print each scalar (in this case, the file names provided as command line arguments) in the `sys.argv` list as the for loop iterates.

    import sys
    for file in sys.argv[1:]:
	    print(file)
	    IN=open(file, 'r')
	    for Line in IN:
		    Line=Line.strip("\n")
		    print(Line)
	    IN.close()

## Adding statement to open and write to new files *each time through* the loop

The code below is similar to above, but statements have been added to open a file to write to **each** time through the loop. This will create a new output file for each separate input file. So, if you processed 100 input files, you would create 100 output files. 

    import sys
    for file in sys.argv[1:]:
        print(file)
        IN=open(file, 'r')
        OUT=open("out_" + file, 'w')
        for Line in IN:
            Line=Line.strip("\n")
            OUT.write(Line + "\n")
        IN.close()
        OUT.close()

Notice above in the statment `OUT=open("out_" + file, 'w')` is creating file names that have `out_` appended to the file name variables contained in `sys.argv`. This means that output files will match input file in filenames, albeit with `out` added as a prefix.Thus, if the code below was run, the files `out_file1.txt`, `out_file3.txt`, and `out_file3.txt` would be generated.

    $ python file_proc.py file1.txt file2.txt file2.txt

## Reading multiple files, writing to a single file

Writing data to a single file after extracting and processing data from multiple files is common. To control writing in this manner, the file handle for the file being written to simply needs to be created.

    import sys
    OUT=open("out.txt", 'w')
    for file in sys.argv[1:]:
	    print(file)
	    IN=open(file, 'r')
	    for Line in IN:
	    	Line=Line.strip("\n")
	    	OUT.write(Line + "\n")
	    IN.close()
    OUT.close()


## Another useful library: `codecs`

The `codecs` library facilitates some safeguards on reading from files that may have multiple types of text embedded (ASCII, utf-8). For example, ASCII is often interpretted as utf-8, but the converse is not true. Using this library (or `io.open`) is a safer way to read in files that may have some strangeness. As time goes on, you will likely learn more on when you want to use alternative `open` functions, but for now just trust us. For this weeks data manipulation problem, you can save yourself a headache by using the code below to open file handles while looping through `sys.argv`.

    import codecs
    import sys
    OUT=open("out.txt", 'w')
    for file in sys.argv[1:]:
	    IN = codecs.open(file, 'r', encoding='utf-8', errors='ignore')
	    for Line in IN:
		Line=Line.strip("\n")
		OUT.write(Line + "\n")
	    IN.close()
    OUT.close() 

## Printing feedback using `sys.stderr.write()`

Print statements are sometimes used to print messages to screen while a program is running, but they are also often used to print data meant be redirected to a file (using `>` or `>>`). `sys.stderr.write()` allows for printing to screen through a different stream, which wont interfere with output being generated with `print`. This is a useful function for sending updates to screen while your program is running, and is especially useful as a debugging tool. Usage is similar to `.write()`, as demonstrated below.

    import sys
    for file in sys.argv[1:]:
	    sys.stderr.write("Processing file: %s \n" %(file))
	    IN=open(file, 'r')
	    OUT=open("out_"+ file, 'w')
	    sys.stderr.write("Opened file for writing: out_%s \n" %(file))
