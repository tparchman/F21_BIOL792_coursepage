# Unix primer 4

## topics to cover

- $PATH
- line endings
- advanced text processing tools (`sed`, `awk`)
- Shell scripts: loops
- Package installers/managers
- From Haddock and Dunn: Chapters 6 and 16
- Bradnam and Korf primer through U45


## 1. $PATH      
This is an environment variable that lists the location of directories storing executables on `Unix` systems. See for yourself:

    $ echo $PATH

The `/bin`, `/usr/bin`, and `/usr/local/bin` directories are normally part of the `$PATH` environment variable, but different users may have different directories listed in `$PATH` depending on  system and user preferences. Executables that are in `$PATH` directories can be called from any location in your file system with out specifying their location.

In this class, you can store your scripts however you want. You can put them in a directory that you add to `$PATH`, and then you call them from anywhere without providing location information. 

**IF** you want to store executable scripts in a directory you add to `$PATH`, two steps are necessary. First, you must convert such scripts to executable.

    $ chmod u+x mac2unix.sh

Second, you need to add the directory you store such scripts in to `$PATH`. If you follow the suggestion of Haddock and Dunn (pg. 87), create a scripts directory (scripts/ for e.g.) within your home directory and add that to `$PATH` by adding the below line to `.bash_profile`, `.profile`, or `.zprofile`:

    export PATH="$PATH:$HOME/scripts

Once you have done the above, you can call such scripts from the command line simply by typing them from the prompt:

    $ mac2unix.sh filewithMAClineending.txt

For this course, we don't actually suggest doing this because you will be constantly altering scripts, and they may be more effectively stored in the directories where you are organizing your learning and course projects. In this case, you can simply call them with their absolute or relative paths (regardless of whether you want to change them to executable).

For e.g, if you wrote a script, `mac2unix.sh`, and stored it in `~/Documents/BIOL792/week4/`, you could call it directly if you were working in that directory:

    $ bash mac2unix.sh filewithMAClineending.txt 

Or simply call by completing its path:

    $ bash ~/Documents/BIOL792/week4/mac2unix.sh filewithMAClineending.txt

## 2. Line endings revisited, text processing commands (`tr`)

As Unix commands, and many scripting languages, often entail processing one line at a time, line ending format really matters. `Unix` systems use `\n`, Mac systems use `\r`, and Microsoft systems use `\r\n`. For working in a Unix environment, files ideally need to use `\n` line endings. Because much of what you do in Linux, Perl, or Python will process text one line at a time, you will find that improper line endings will often cause problems. So how can we recognize when files have the wrong line endings?

Take a look at `grouse_barcodes.csv` in the github repository for this week . This file should contain three columns of information seperated by commas, but you'll notice that all of the information appears on a single line, and the highlighted symbol `^M` exists where line endings should. Here, the `^M` is showing you every place where a Mac line ending (`\r`) exists in the file. There are multiple ways that you could easily change the line endings.

You could open the file in `Text Wrangler` or a similar editor. At the bottom of the window, you will see the words `Legacy Mac OS (CR)`, which tells you that this file is using Mac line endings. If you click that drop down menu, change the line endings to `Unix (LF)`, and save the file. `NOTE`: the `\r` line ending is called a carriage return (CR), whereas the `\n` line ending is called a line feed (LF). 

Alternatively, we can use text processing commands such as `tr`, a transliterator function. You can think of `tr` as a find and replace command, where you specify a match to find (which can be specific, or a flexible regular expression) and 2) some replacement text. Check out the `man` page for `tr` before moving forward. 

Try changing the line endings of `grouse_barcodes.csv` using `tr`, and use `less` to confirm that it worked. In the command below, the first text in quotes designates the match to find, and the second represents the replacement text. In this case, we are finding Mac line endings (`\r`) and replacing them with Unix line endings (`\n`). We use `cat` to send the file contents to stdout, and then pipe that into the `tr` command.

    $ cat grouse_barcodes.csv | tr '\r' '\n' > grouse_barcodes_unix.csv
   
## 3. substituting matches with `sed`

`sed` is an efficient tool for manipulating large numbers of text files using single lines of code, when the goal is replacing one pattern of text with another. `sed` is flexible with regular expressions, and can locate specific or highly fuzzy matches. Let's explore this command with `grouse_bams.txt`, which contains a simple list of file names from a DNA sequencing project. You'll notice that information is separated by both underscores and periods. The important information in this file lies between the first underscore and the first period (e.g., `CO_HC_20`), as this code represents the individual's geographic region (e.g., `CO`), the individual's population (e.g., `HC`), and the individual's  id number (e.g., `20`). Let's first use `sed` to delete the extra text that we might not care about. Since we need to remove different parts (`aln_` and `.sorted.bam`), we can to use a `|` in our command. Also, since periods are special characters in this case, we will need to escape them using a `\` in our substitution statement.

    $ sed "s/aln_//" grouse_bams.txt | sed "s/\.sorted\.bam//" > grouse_ids.txt

 Try adding another `sed` command to the command above that replaces underscores with commas:

    $ sed "s/aln_//" grouse_bams.txt | sed "s/\.sorted\.bam//" | sed "s/_/,/" 

You'll notice that only one underscore was replaced. This is because `sed` only replaces the first instance of the match on each line unless you tell it otherwise. In order for you to find and replace all matches on a line, you will need to add the `g` global flag:

    $ sed "s/aln_//" grouse_bams.txt | sed "s/\.sorted\.bam//" | sed "s/_/,/g" 

## 4. `Awk`: a text engine with a ton of flexibility
`awk` isn't just another `Unix` command - it is essentially a language and has books written about it. Like `sed`, `awk` can be used to solve a wide variety advanced text manipulation problems. Haddock and Dunn do not go into detail about `awk`, but we will briefly introduce it to you here by showing you some examples using the `grouse_ids.txt` file that you generated above. `awk` allows you to print out a subset of a file based on specific criteria found in your command (this info is placed within curly brackets). `NOTE`: we won't be redirecting the output of any of the commands below into a new file for simplicity, but you could easily do this if you wanted.

Most basically, you can print out the entire contents of a file:

    $ awk {'print'} grouse_ids.txt

You could also only print out certain columns of the data (e.g., only the 1st and 2nd columns, as before). `NOTE`: the default delimiter for `awk` is a tab, so you will have to specify an underscore as a delimitor below (using -F).

    $ awk -F "_" {'print $1,$2'} grouse_ids.txt

You will note that the default output field separator (`OFS`) for awk is a single space, but you can change that using the `OFS` flag:

    $ awk -F "_" 'BEGIN {OFS = "_"} {print $1,$2}' grouse_ids.txt

You can also change the order of the columns if you want. Let's write the individual id followed by the geographic region, separated by a colon:

    $ awk -F "_" 'BEGIN {OFS = ":"} {print $3,$1}' grouse_ids.txt

Matches, including those with regular expressions, can be utilized as well (using `//`). What if you only want a population list that includes individuals from the `HC` geographic region?

    $ awk -F "_" 'BEGIN {OFS = "_"} /HC/ {print $1,$2}' grouse_ids.txt

There are a ton of additional tasks that you can accomplish with `awk`, and we encourage you to explore those on your own. 

## 5. Turning useful Unix code into reusable bash scripts

### Example of a slightly more useful bash script, compared to last weeks primer.

    #!/usr/bin/bash
    cat $1 | tr '\r' '\n' > u_$1

`$1` here stores a command line argument, which in this case should be a text file with mac line endings. This will pipe the contents of that file to `tr` to replace `\r` with `\n` (thus replace mac with unix line endings), and will redirect to a file which will be named "u" plus the argument stored in `$1`.

    $ chmod u+x mac2unix.sh
    $ ./mac2unix.sh grouse_barcodes.csv

This will produce a file "u_grouse_barcodes.csv", which should have unix line endings.

## using multiple arguments and loops in bash scripts in order to process many files at once

The main reason we create scripts is to allow us to easily perform the same exact tasks without having to write new code. These scripts are most useful when you want to perform the same commands on multiple files all at once. For example, if you wanted to replace all instances of an underscore in several files with a comma and save the output as new files, you could either 1) open each file individually and use a find and replace tool; 2) write a simple unix command for each separate file; or 3) write one script that will find and replace for any number of files. While it might not seem like the third option would really save you that much time, just imagine if you wanted to do this for 1,000 different files? 

Let's say we wanted to write a script that would take any number of barcode files and 1) create an ids file (e.g., `CO_HC_20`) and 2) create a pops file (e.g., `CO_HC`). We would use this to begin each sequencing project that we are working on and ensure that the format of the new files is the exact same each time. Start by creating a new script (`make_ids_and_pops.sh`) using `touch` and adding the header line as above.

Before we begin adding commands to our script, we first need to think about the terminal command that we will eventually use to execute our script (don't type this now - you're script hasn't been made yet):

    $ bash make_ids_and_pops.sh *barcodes.csv

In this command, you are telling your computer to execute your script on every barcode file in the directory. `Unix` will then store the list of the different barcode file names as standard input (`STDIN`). The standard input will be stored in the `$@` special array, where you can easily access the file names. Let's start simple, and have the first line of code only print out the contents of `@`. Once you have added this line, use the bash command above and see what happens.

    #!/bin/bash
    echo $@

You should see `colias_barcodes.csv grouse_barcodes.csv` printed to your screen. Each of the file names is also stored separately as a special object: the first file name is stored in `$1`, the second file name is stored in `$2`, and so on. We will not be directly using those objects in this script, but they can be very useful for other tasks. Try printing them to screen.

    #!/bin/bash
    echo $@
    echo $1
    echo $2

Because we want our script to be able to handle any number of input files, we need to include a simple loop that tells the script to do execute multiple commands for each input file. Loop syntax might seem abstract at first, but it will make more sense as you familiarize yourself and practice. Before specifying the commands to execute, we first need to specify which files we want the loop to work on. We will do this by typing `for bc in $@; do`. This means: for every filename that is listed in `$@`, do whatever I type next. You are probably wondering what `bc` stands for. It's simply a placeholder object that I created for the filenames that could have been named almost anything you wanted. I chose `bc` for barcode, but you could chose `file`, `barcode`, `input`, or anything else that makes sense to you. After this, we need to add the `Unix` commands that will create the new ids and pops files. Finally, you need to type `done` on the last line.

    #!/bin/bash
    echo $@
    echo $1
    echo $2
    for bc in $@; do
        cut -f 3 -d "," $bc | grep "_" &> $bc.ids.txt
        cut -f 3 -d "," $bc | grep "_" | cut -f 1,2 -d "_" &> $bc.pops.txt
    done

You'll see that instead of specifying a specific file for the first command in each `Unix` pipe, you are instead specifying `$bc`, which is the current file name that you are currently working on in the loop. Also, instead of being able to redirect the output using `>`, you instead must use `&>` to redirect the standard output to a new file. Finally, you might be wondering why `$bc` is listed as part of the output file names. Look at the names of your new files to see what this syntax is doing. What are the `grep` commands accomplishing?


## 6. Package installation and management on Mac Unix (`brew`) and Ubuntu Linux (`apt`)
<p>&nbsp;</p>

### **A. Mac Unix: Homebrew (`brew`)** 

`homebrew` manages and installs packages on Mac OS Unix. 
To install brew (homebrew):

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

`brew` is pretty easy to use. To look at a list of commands and their uses:

    $ brew help

To search for an installable program:

    $ brew search

To install a package:

    $ brew install packagename

As a simple example, lets install a more useful version of `top`, `htop`, that has some expanded information and visuals. Using brew is quite easy, as you can see.

    $ brew install htop

A more detailed, yet basic, tutorial can be found below. As with the above, carefully review before using.

- https://wpbeaches.com/installing-homebrew-on-macos-big-sur-11-2-package-manager-for-linux-apps/


<p>&nbsp;</p>

### **B. Linux Ubuntu distributions:**

`apt` is a package management system for most Linux distributions. It facilitates the installation, management, updates, and removal of software. Using apt-get requires superuser privileges (`sudo`), and will require password entry.


You can find useful tutorials on `apt` and `apt-get` below. We suggest reviewing information, and familiarizing yourself with `sudo` carefully before using.

- https://phoenixnap.com/kb/how-to-use-apt-get-commands
- https://itsfoss.com/apt-get-linux-guide/
- https://www.control-escape.com/linux/lx-swinstall.html


To install software using `apt-get`:

    $ sudo apt-get install <package_name>

To remove software using `apt-get`:

    $ sudo apt-get remove <package_name> 

Note, the above doesnt remove configuration files associated with a package. To remove the package along and configuration files:

    $ sudo apt-get purge <package_name> 

<p>&nbsp;</p>



