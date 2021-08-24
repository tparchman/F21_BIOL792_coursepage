# BIOL 792-1028. Unix week one tasks 


## Common commands

Below is a sample list of commonly used UNIX commands. You might want to use this to take notes on commands as you work through the tutorial, or just as a checklist so that you know you’ve covered all the bases.

It is useful to note that the `up` and `down` arrow keys scroll through recently used commands, and `tab` key completes the name of a file, directory, unix command, or piece of installed software. You will want to use `tab` heavily for two reasons. 1. it will save you most of your typing time, 2. autocomplete is more accurate than your  typing.

    ls          mkdir           cd          pwd
    cp          mv              rm          rmdir 		
    cat         less            head        tail
    grep        wc              uniq	    top



## `man` pages
For any Unix command (there are thousands) you can find the full information on that command by using  `man`. 

For example: 

    $ man pwd

This will tell you what `pwd` does, command line options, etc. Here you will see the information on `pwd` displayed in a text viewer called `less`.  `man` pages are always opened with `less`, a command you will use heavily to view the contents of files. 

To navigate/control `less`:
- `space bar` to advance one page
- `b` to go back one page
- `q` to exit less and regain command line prompt
- `/` to enter a pattern search

Next, look at:

    $ man wc

You will see that `wc` in its simplest invocation counts words characters and lines, but command line options allow more. Want to know how many lines of data are in a large file? 

    $ wc -l name_of_file.txt
Try:

    $ man grep

 Upon scrolling through the `grep` man page, you will see that `grep` has many command options and is a flexible, powerful, and commonly used text processing tool. Use the `man` command to explore the functionality and command line options for some the common commands listed above.

## Directory navigation

You can move directly to your home directory from anywhere with the two shortcuts below.

    $ cd ~

    $ cd 

Moving directly to `root` is similarly easy.

    $ cd /

Moving up into unnamed directories is easy, as below.

To move up one directory:

    $ cd ../

To move up two directories, and so on:

    $ cd ../../



You can also move a file from your directory to any directory by displaying the whole path from root (starting with / which is the top of your directory tree. That is, all directories descend from root).

The following command would move a file into the directory Macintosh HD, which all Macs have:

    $ mv filename /Volumes/Macintosh\ HD

Note: there is a `\ ` before HD. This is because the directory name (“Machintosh HD”) has a space in it.

*In general, when making and naming directories in unix, you will want to avoid using spaces because they require extra typing and the `\ ` needs to be used instead of just “ “. SPACES IN DIRECTORY NAMES = BAD.* Don't do it. Ever.

What do you think the following command will do? Try it and find out:

    $ mv ../filename .

“.” Represents the current directory. Anytime you `cp` or `mv` something from some distant directory (or another computer for example) to the directory you are working in, you will use “.”  as the destination directory.

You have already seen the use of `ls -l`. You might have noticed that command reported file sizes in units that were not easy to interpret. 


Take some time to move around other directories, listing their content and moving to more distant directories. Familiarize yourself with how directories are listed and organized.

Use `cd` to enter a directory\
Use `cd ../` to go back a directory\
Use `cd` (with no arguments) to jump directly to your home directory, and\
Use `cd` to jump directly to root


To quickly remind yourself of where you are in a directory tree from anywhere on your system:

    $ pwd

## Stopping jobs, exiting programs in the terminal

It is often necessary to put a stop to things that are happening in the terminal, but the means to that end can be context dependent. Here are two simple options that usually work:

`^c` will cancel a process that is running (the “^” there represents the control key)

`^z` will cancel a job but store in the background. More on this later.

`q` exits a number of programs, including less and top

## Basic process monitoring (more detail later)

    $ top

Will list processes running on your machine.

Open another terminal window (`command n`) and use `less` to look at the top of a text file. Type `top` in the other terminal and look for the line showing that less is running.


## Using basic Unix to explore features of a file of Illumina DNA sequencing data.

Make a directory in your home directory (e.g., /Users/parchman/) entitled BIOL792.

Make a file called unix1_log.txt in the BIOL792 directory. When you are done with this assignment, record everything you did from the command line in this log file (learn to use `touch` to make a new file).

Inside this directory, make three other directories named:
- data
- scripts
- resources
		
Download the example file “sample_passerina.fastq” from the course website for the unix1 assignment, and use the command line move it into the data directory you made above. 

- What is the size of this file, and when was it last modified? 
- How many lines are in the file?
- `grep` is a powerful pattern matching utility in unix. Executed to find a simple pattern match, it will print to screen every line that contains the specified text or flexible pattern (we call the expressions to fit these matches "regular expressions" and will learn much more on this later in the course). The file you are working with here is raw data from an Illumina sequencer. Each DNA sequence is represented by information on four lines. The lines starting with “@” are the IDs for each sequence, the following lines are always a DNA sequence (2nd), a quality ID (3rd), and the quality score for the previous sequence (4th). Study the `grep` `man` page, and use grep to find and count lines that start with "@". This will allow you to count the number of DNA sequences in the file.

Try the `history` command. What do you see? You could find this quite useful. When you use the up and down arrow keys from the prompt, you are basically navigating up and down through this list. Try that out, and take note that you will probably use this feature regularly. 


Try some other useful commands:

    $ whatis date
    $ whatis grep
    $ whatis less 
    $ date
    $ whoami
    $ cal


## Unix tutorials: **complete the first 2-3** sections of each of the below tutorials. This will help you get up to speed and or solidify introductory Unix commands.

Lastly for our first week, work through the first two sections of this tutorial to reiterate your introduction.

- Useful primer from "Unix and Perl to the Rescue", by Bradnam and Korf. For this course, the [unix_primer](http://korflab.ucdavis.edu/Unix_and_Perl/current.html) is hard to beat. Please bookmark this and get familiar with part 1 and part 2.

- Also, please have a look at the excellent [tutorial from software carpentry](http://swcarpentry.github.io/shell-novice/). For this week and next, follow steps 1 through 3.

- quick guides to basic Unix commands can be found in [Appendix 2](https://github.com/tparchman/BIOL792/blob/master/unix_resources/Haddock_and_Dunn_quickguide_Appendices.pdf) of Haddock and Dunn and the course page has numerous 'cheat 'sheets' under unix_resources, such as this [unix cheat sheet](https://github.com/tparchman/BIOL792/blob/master/unix_resources/unix_cheat_sheet.pdf). These will be extremely useful.

Also, please have a look at the excellent [tutorial from software carpentry](http://swcarpentry.github.io/shell-novice/). For this week and next, follow steps 1 through 3.
