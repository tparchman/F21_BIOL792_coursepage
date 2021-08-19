# Unix assignment 4

## Topics to cover
- `sed`, `awk`
- Bash scripts
- Looking ahead to Python


## 1. `sed`
 **1.A**  `sed` is useful for matching and replacing regular expressions.  You can read up on simple examples in your book and can find a wealth of information online. Use `sed` to turn the DNA sequences in the fastq file we have been using for the last few worksheets (`sample_passerina.fastq`) into RNA (all you have to do is substitute U for T). 

    $

## 2. `awk` 
Read up a bit on how `awk` works, look at examples in the slides and in the primer. Note that this versatile command can be used for all kinds of text extraction. It is heavily used because it allows for field extraction and pattern matching, so can quickly handle many data extraction routines.

**2.A** Lets work on the `yeast_genome.gff` file from last week. Use `awk` to write the 1st, 3rd, and 5th column to another file.

    $

**2.B** The 4th and 5th columns of `yeast_genome.gff` represent the starting and ending location on a chromosome of the annotated sequences represented in this file. Write out the first three columns of this file and the LENGTH of each sequence to an output file (the length would be the value of the 5th column minus the value of the 4th).

    $

**2.C** Now, lets say we want to do the same thing as above, but only for sequences that are longer than 400 bases in length. Use `awk` to extract that information (5th column minus 4th column > 400)

    $

## 3. Writing useful Bash scripts.

Here we want you to write a bash script that you can use to convert Mac line endings (`\r`) to Unix line endings (`\n`). 

**3A.** First execute your 'tr' command from the prompt on the file: ssr_results_MACendings.txt (available on the [course githubpage]()) to make sure that your 'tr' command works. You will see that this file has mac line endings. Thus, if you look into it using 'less' you will see the curious looking "^M" character. In Unix speak, this is actually '\r', but simply displays as ^M in 'less'. The Unix format for line endings is '\n'. 

    $

**3B.** Now lets make a more useful script, **which must be able to read in any number of files you feed it**. 
For this, we will work with a directory populated with remote sensed climate data from "Ibuttons", all with Mac line endings, which you can find on the github repository under week4_unixIV/sample_log_files/. Here are eight files, all with Mac line endings. First you will need to decompress all of these files 

    $ gunzip *txt

 You will want this script to be executed so that you feed it all .txt files simultaneously as arguments from the command line:

    $ bash mac2unix_line_endings *.txt
    
For help on writing a script that can handle multiple arguments from the command line refer to **section 5** of `unixIV_primer.md`. You can simply use `tr` to do this as above, but instead of just executing this from the command line for one file, you will have written a program that can do this for many files at a time. Name this script `mac2unix_line_endings.sh`, and save it for future use (you will find this repeatedly useful). You will make use of $@ (an array of arguments from the command line, the file names in this case) and a loop that processes each file, one at a time.

    $

## 4. Installing `homebrew` and updating your system to the most recent version of python

First, lets see what version of python you have, and if you need to update it in the first place. We want to be running python3, so lets check for that.

    $ which python3

If you have it already installed great. Still learn how to use brew or apt-get as below, just pick another package to install if you are already set with python (Id suggest, `htop`, `wget`, or `tree`).

## A. on mac unix:


Check to see if you already have `homebrew`

    $ which brew
  
If you dont have it, then:

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

  OR if you are running OS catalina:

    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Once you have `homebrew` installed the `brew install` command can be used to easily install any packages you need. Read up on `brew`, and try installing something (such as `wget` or `htop` for simplicity). Once you have done that, installing python3 should be easy.

    $ brew install python3
## B. on linux, try `apt` or `apt-get`

It is probably already installed but if not try with the package manager `apt-get`

    $ sudo apt-get install python idle
    