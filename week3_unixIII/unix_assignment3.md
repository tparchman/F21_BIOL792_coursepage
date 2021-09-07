# Unix assignment 3

## Concepts/Tools: 
- `split`, `cat`
- pipes, redirection
- interacting with remote locations (`curl`, `wget`)
- moving large batches of files (understanding `rsync`)



## Files needed from course website:
- sample_passerina.fastq.gz (from last week)
- yeast_genome.gff

<p>&nbsp;</p>

## 1. Some additional quick file manipulations tricks

Lets go back to the `sample_passerina.fastq` file you were working with last week (Remember when you download from the Github repository, it will be compressed, and will need decompressing with `gunzip`).

**1.A** Lets say we need to split the big file into many smaller files to run parallel jobs on an HPC cluster. Use `split` to “split” `sample_passerina.fastq` into smaller files that each have 1000 lines. How would you accomplish the opposite problem, that is how would you put these files back together? Notice how `split` names files by default if not specified. Have a look at the `man` pages for `split` and `cat` to figure this out (the first command will use `split`, the second will use `cat`)

    $ split ....

    $ cat ....

**1.B** Instead, we might want to just remove the first 4000 lines of sample_passerina.fastq. Look at the `man` page for `head`, and figure this out.

    $
 
<p>&nbsp;</p>

## 2. Pipes ("|"): moving stdout from one command into another.

Decompress sample_passerina.fastq.gz and try each of the commands below, striving to understand what each  is doing. The sections in Haddock and Dunn, or the regular expression cheat sheat under [unix resources](https://github.com/tparchman/BIOL792/tree/master/unix_resources) on the github page will help you understand what `^` and `[ ]` mean for regular expressions. In addition, you will want to learn what the `tr` command does.

    $ grep ^@ sample_passerina.fastq | wc -l   

    $ grep ^@ sample_passerina.fastq | grep “NVP_CY_48147” > NVP_CY.txt

    $ grep ^[ATCG] sample_passerina.fastq | wc –l

    $ grep ^[ATCG] sample_passerina.fastq | tr ‘T’ ‘U’ | less

    $ grep ^[ATCG] sample_passerina.fastq | tr ‘T’ ‘U’ | head –n 20 > first20seqs_transliterated.txt

<p>&nbsp;</p>

**2.A**. Download **yeast_genome.gff** from the [github site](https://github.com/tparchman/BIOL792/tree/master/week2_UnixII). As you have the url from the link above, use `curl` or `wget` to pull the file from where it resides online to the directory you want to work in. This is an easy way to pull data from online locations. Hint: click on the file name in the github folder, then click 'view raw' and copy the address. You may want to use `curl -o yeast_genome.gff` followed by the address so that the file has the name you want. If you use `wget` you might find this a bit easier.

    $

    
GFF file format is used extensively in bioinformatics to store information on genomic features. This file has information on transcripts from a yeast genome. The third field in each row of this file has a description of the ‘feature’ of DNA sequence to which a region belongs. Example categories would be centromere, gene, intron, and tRNA.
<p>&nbsp;</p>

### Complete each task below, using Unix commands and pipes where ideal.

**2.B** Use pipes to connect Unix commands in order  to 1. grab the information for transcripts on chrIII, 2. Grab only the first 100 of these, 3. grab the “feature” field, and 4. Write to a file. (try a combination of `grep`, `head`, `cut`, and `>`)

    $

**2.C** Write a pipeline to output the information for sequences on chromosome III that represent CDS. (try `grep`, with or without `|`)

    $

**2.D** Write out a file that lists in sorted order, all of the unique feature categories in yeast_genome.gff. Details on the commands sort and uniq can be found in the book or in man pages. (try `cut`, `sort`, `uniq`)

    $


<p>&nbsp;</p>

## 3. Moving and syncing files and directories: backing up your work (or your entire system)


`rsync` is a tool that can be used to sync directories, copy directories, update directories, etc. Read up on `rsync`, and pay careful attention to the command line options. In the simplest sense it works like copying and pasting a directory using the finder or windows explorer, but many times faster and with many options for specifications. Anytime you move large files or directories while working on computing clusters you will make heavy use of `rsync`.

With more detailed command line options, rsync can be used to sync two directories exactly.
	
**3.A.** Make a directory called rsync_test in your BIOL792 directory. In that directory make two directories (for convenience, name them dirsource and dirdestination). Start by putting some files in the dirsource directory (maybe just 3 files). 

**3.B.** Copy the dirsource directory from one location to another, rename the copied directory. Note that whether or not you follow the directory name with a “/” will have a big effect on how this works. Specifically, if you run:
 
    $ rsync –av dirsource/ ~/Desktop

The files within dirsource will be put in the desktop directory (not inside of a dirsource directory though).

If you run:

    $ rsync –av dirsource ~/Desktop

The dirsource directory will be made in the Deskop directory.

**3.C.** Now use `rsync` to sync the dirsource and dirdestination directory. 

    $

**3.D.** Go into the dirsource directory and delete one of the files. Use `rsync` so that dirdestination mirrors dirsource. That is, so the file deleted in dirsource is now deleted in dirdestination. This will require you understanding how the `–-delete` command works.
	
    $

## 4. Writing a useful shell scripts.

**4.** Here you will write a simple bash script for rapidly syncing your working files from a certain directory (or perhaps your entire home directory) to a flash or backup drive. This will require you to understand how to write a shell script, and how to use `rsync` (pay special attention to the delete option). The end point of this assignment should be a script that you can run from the terminal that accomplishes this job merely by typing the name of the shell and the program. You will only need two lines within the script. One will be #!/usr/bin and one will be your `rsync` command.

	e.g., $ bash sync_laptop.sh

or

    $ ./sync_laptop.sh


For now, lets specifically write a program that syncs your BIOL792 directory with the same directory that you have created on either a flash drive, or an external hard drive at home. This program should result in the directory on your drive being updated to look exactly like the BIOL792 directory on your laptop. That is new files should be added to the destination directory and files you deleted from your laptop should be removed from the drive as well. When the program is done, it should print to the screen “Your BIOL792 work is now backed up”. You can look at slides from class to get more hints on how to do this.

Once you have tested this and are absolutely sure it is working the way you want, you could use the basic structure of the script to back up your entire home directory (or your entire computer) to a drive. 
		
