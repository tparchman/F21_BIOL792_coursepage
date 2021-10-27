# Python assignment 5, Data Science for Biology
## Topics to cover
- Working with files: Input/Output
- `for` loops, processing files one line at a time.
- Regular expressions
- `sys.argv`, `re.search`
<p>&nbsp;</p>

### The project for this week will involve reorganizing many files generated from temperature loggers that Kelly Klingler (former PhD student in Peacock lab) used to collect microclimate data around pika haypiles during 2012-2014. There are 38 temperature loggers that recorded data during 2012-2013 and 37 temperature loggers that recorded data during 2013-2014 (one was lost to water damage). Each of these automatic temperature loggers generates a text file (75 text files in total) with 5 columns of information. You will notice that almost every data logger will have two text files: one for 2012-2013 (denoted as “13”) and one for 2013-2014 (denoted as “14”). In addition, two data loggers were placed at each of 19 haypile locations (H1-H19) therefore each text file should also indicate whether a temperature logger was placed at the surface “S” or at some depth with the talus slope “D”.

You can access a `.tgz` directory containing the 75 files from the course webpage. To uncompress this you will need to use the unix command `tar`:

    $ tar -zxvf logfiles.tgz

Once you have downloaded and extracted the files, have a careful look at their contents. You will notice that they all have the same format, so you can use the same code to extract similar information from each file.

You will need to use `open` inside a loop so that you can read, and work on, each of the 75 files individually. Something like below will work:

    for filename in sys.argv[1:]:
        IN = open(filename, 'r')
<p>&nbsp;</p>

A. For this weeks program you are going to read in all files and make a single file that has specified data in an easily accessible format. The data of interest in each individual logger file is arranged in 4 columns (we are going to ignore the first). We want to write the information from those four columns from each .txt file to an outfile that has all of the data we are interested in. For each .txt file that is read in from `sys.argv`, you want to write the data from each column (there are four) to a row in the outfile (which will have 4 rows for each infile). The start of each line should have the name of the infile, but different features of that name need to be comma separated so that the data can eventually be sorted by that information.

For example: 
Infile: 1901302136_H15_D_14.txt.txt

The beginning of each lines in the outfile that will have data from the infile (after you have used a regular expression to get rid of "_" and ".txt.txt"):

1901302136,H15,D,14, data…………………..

The output file should have 4 lines per logger (per infile) and should look as below. The idea here is that this file can easily be read into and worked on in R for the rest of the analyses Kelly needs to do. 

Example data for 1901302108,H7,D,13:

    1901302108,H7,D,13,10/7/2012,10/7/2012,10/7/2012,10/7/2012,
    1901302108,H7,D,13,8:00:00,8:35:00,9:10:00,9:45:00,10:20:00
    1901302108,H7,D,13,AM,AM,AM,AM,AM,AM,AM,PM,PM,PM,PM,PM,PM,
    1901302108,H7,D,13,41.4,41.4,41.4,41.4,41.6,41.7,42.0

Example data for 1901302108,H7,D,14:

    1901302108,H7,D,14,9/29/2013,9/29/2013,9/29/2013,9/29/2013,
    1901302108,H7,D,14,8:00:00,8:35:00,9:10:00,9:45:00,10:20:00,
    1901302108,H7,D,14,AM,AM,AM,AM,AM,AM,AM,PM,PM,PM,PM,PM,PM,PM,
    1901302108,H7,D,14,32.4,32.5,32.5,32.6,33.0,33.0,32.9


B. Extra. Lets say you want to to do some analyses on the temperature data alone. Write a second file that has the mean temperature for each line in the above file. 

## Hints:

**1).** The `codecs` library facilitates some safeguards on reading from files that may have multiple types of text embedded (ASCII, utf-8). For example, ASCII is often interpretted as utf-8, but the converse is not true. Using this library (or `io.open`) is a safer way to read in files that may have some strangeness. As time goes on, you will likely learn more on when you want to use alternative `open` functions, but for now just trust us. For this weeks data manipulation problem, you can save yourself a headache by using the code below to open file handles while looping through `sys.argv`.

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

**2).** There are some problematic special characters in *some* of these files. To guard against them, a line of code as below will work for cleaning these things out of each line in each file.

    stripped = stripped.replace("\0","")
