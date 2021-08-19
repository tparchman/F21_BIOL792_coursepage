
# Unix primer 3

## topics to cover

- process control
- more on removing directories and files
- copying directories, moving batches of files
- permissions, file modes
- pipes (`|`) and redirection (`>`,`>>`)
- Interacting with remote machines
- From Haddock and Dunn: Chapters 5, 6 and 16

<p>&nbsp;</p>

## 1. Process monitoring with `top` and `ps`, running jobs in the background, killing jobs
`top` will display information on processes running on the machine you are logged into.  Doesn't matter what directory you call it from.

    $ top

`ps aux` (-a -u -x) will show all active processes. 

    $ ps aux

`ps aux | grep [search expression]` will pipe processes listed as above into `grep`, and can be used to locate PIDs for specific applications.

    $ ps aux | grep firefox-bin

If you have mutliple processes running, and want to kill one, use `kill` followed by the process ID, which you can locate with `top` or `ps`, e.g.:

    $ kill 9031

### Stopping jobs, running jobs in the background

If you have a job running in the shell that isnt doing what you want, you can easily kill from the terminal with "ctrl c". You can also temporarily kill it with "ctrl z", and then restart it in the background with `bg` typed at the prompt with no additional arguments necessary.

If you are calling a command that is going to take some time, and you dont want it to occupy the shell you are working in, you can send it to the background with `&`. Once a job is running in the background, the job will continue once you close the terminal session or exit your connection to a remote server

    $ cat *fastq > allgenomefiles.fastq &

## Practice running a program, running it in the background, and killing it ( from last weeks assignment)

`jot`  can generate strings of numbers, among other things (have a look at the `jot` `man` page). Try the following command which will print 100 random numbers:

    $ jot -r 100

Now, increase the number of random numbers until you get to a number of replicates (think millions or more) that takes your computer an appreciable amount of time to complete. If you made the number large enough, you’ll notice that you can’t do anything else with your Terminal window while it’s busy. Use `ctl c` to stop it, and then execute the commands again with an “&” at the end:

    $ jot -r 1000000000 > test.txt &

The ampersand (&) will cause the job to run in the background, you will have the normal prompt back in your terminal window, and closing it will not affect the job.  

You can use `top` or `ps` to identify the process number of the `jot` job in oder to kill it. You could more efficiently pipe the output from `ps aux` into a grep search for `jot` to return the PID of the job running in the background:

    $ ps aux | grep jot

After you identify the job id (e.g., 77654), you can kill it:

    $ kill 77564
<p>&nbsp;</p>

## 2. Removing directories and files revisited (and note of caution).

Once you changed your .bash_profile file to invoke the `-i` option, the shell should ask if you are sure you want to delete or overwrite files after using `rm`, `rmdir`, `cp`, or `mv`. *Please make certain that you have this working correctly so you dont inadvertently destroy things.* 

Things should look as below:

    $ rm british_PCA.jpg 

    remove british_PCA.jpg? 

If you are in a hurry, you can override the -i option, but be VERY careful before doing this regularly.

    $ rm -f british_PCA.jpg

Lets say you used faulty code to write 600 .txt files to a directory, and you want to clean up those files before fixing your python code. `rm` only works on one file at a time. To remove them all, without being prompted with "remove N.txt?" for each file consecutively, you can execute `rm` with the the additional arguments `r` (removes file heirarchy recursively, meaning it will remove directories and all within) and `f` (without prompting for confirmation). This is the most dangerous Unix command, with no second chances, so use with **extreme caution**. To repeat, **extreme caution**.

The below command will remove, instantly without second chances, forever, every file in the working directory that ends in txt. To repeat, **extreme caution**.

    $ rm -rf *txt
<p>&nbsp;</p>


## 3. Copying and mirroring directories within and among Unix systems: `rsync`

Use `man` to have a look at the capabilities of `rsync`. This is a versatile and frequently used command for moving, copying, or mirroring directories. You will find yourself using this command to copy directories around your computers file system as well as to storage drives, remote servers, and high performance computing systems. We will learn how this works here in a few simple contexts, but guarantee you will find yourself using this often.

The basic use of `rysnc` might look like what you see below:

    $ rsync -av source_directory/ destination_directory/

I like to use the command line arguments `-a` and `-v`, which invokes archive mode and increases verbosity. This will print information to the screen as copying proceeds.

A couple of minor details control the placing of directories and their contents. In the above example, there is a trailing forward slash in front of the source directory (if the directory doesn't already exist). This will write the **contents** of the source directory into the destination directory. I dont like doing that often, as it can make a mess. The below example, without the trailing `/` on the source directory will copy the directory itself (as a container) to the destination.

    $ rsync -av source_directory destination_directory/


`rsync` is extremely useful for mirroring directory contents between computers, or for managing backups. For example, it can be used to copy the entire contents of your laptop to an external drive or remote server, but then used daily or weekly (or however often you like) to update a backup. While the first action may take a bit, once a version of the source_directory/ exists within destination_directory/, the command below will only update destination_directory/ to reflect changes in source_directory/ since the last iteration of `rsync`. New and modified files will be copied. The `--delete` allows files that were deleted from source directory to be deleted from the destination_directory. Be cautious with this until you are completely comfortable to avoid potentially major mistakes with deleting things you don't want deleted.

    $ rsync -av --delete source_directory/ destination_directory/

<p>&nbsp;</p>

## 4. Permissions and file modes

As Unix systems are  multi-user, the control of permissions on directories and files is critical for security, privacy, and collaboration. Typing `ls -l` (or `ll` depending on how you modified your bash_profile) will show you the permissions associated with files in your current directory.

    $ ll -h

    -rw-rw-r--.  1 parchman parchman  51G Jul 25  2017 J1b.clean.fastq
    -rw-rw-r--.  1 parchman parchman  51G Jul 22  2017 J1.clean.fastq
    -rw-rw-r--.  1 parchman parchman  44G Jul 22  2017 J2a.clean.fastq
    -rw-rw-r--.  1 parchman parchman  44G Jul 22  2017 J2b.clean.fastq
  

 A glance at this output illustrates how permissions are displayed. 3 permissions are defined for each owner level (`user`, 'owner'; `g`, 'user group'; `o` 'other'), only the owner of a file or directory can change the permissions therein. The first position from the output above specifies file type, the following 3 have permissions for 'user', then three for 'group', then 3 for 'other'. Permission is indicated by the letters below, a lack of permission with a `-`.
- Read (`r`): Permission to open and read a file, for a directory allows the listing of content.

- Write (`w`) Permission to modify the contents of a file, or for a directory, to add, remove and rename files.

- Execute (`x`): Permission to run an executable program.


Here are some examples of symbolic notation:

- `-rwxr--r--`: 'User' has read/write/execute permission, 'group' and 'other' have only read permissions.
- `drw-rw-r--`: A directory where 'user' and 'group' have read and write permissions, while 'other' has only read.
- `-rwxr-xr-x`: A file, 'user' has read/write/execute, 'group' has read/execute, and 'other' has read/execute.

The `chmod` command is used to alter permissions. The command can be controlled by either numeric or symbolic codes, the latter are illustrated below. You can find useful guides to the numeric system [here](https://gist.github.com/juanarbol/c44e736be70279c1fd5d68aa24f9d8be).

| Operator | Action/level |
|----------|--------|
|  +        | user/owner     |
|  -       | Remove  |
|  =       | sets permission|
|  r        | read    |
|  w       | write  |
|  x       | execute|  

<p>&nbsp;</p>

  
| Abbreviation | User level |
|----------|--------|
| u      | User     |
| g       | Group  |
| o       | Other|
| a       | All|
<p>&nbsp;</p>

We are going to try to avoid messing with permissions to much in this course, but if you go on to use remote or cluster computing systems with other groups, understanding permission in more detail is essential. There are, however, a few simple things we will do, and below are some examples. 

Convert the .sh shell script to an executable for all users.

    $ chmod a+x first_shell_script.sh

Convert the .sh shell script to write for all users.

    $ chmod a+w first_shell_script.sh

This script can then be executed from the currently directory:

    $ ./first_shell_script.sh
<p>&nbsp;</p>

## 5. Pipes (`|`)

Pipes, called with the `|`, are used to send stdout from a command directly as input into another. Lets say you have DNA sequence data from a large number of individuals, all in separate .fastq files, in a project directory. To be sure of your sample size, you want to count the number of files in that directory. `ls` normally sends directory content, one line at a time, to stdout. Here we are piping that output directly into `wc -l` which will count the number of lines, which will represent the number of files.

    $ ls | wc -l

Pipes are obviously useful to send output from one Unix command to another, yet the above examples only use a single `|`. In fact, many bioinformatic "pipelines" are actually built from strings on unix commands piped into one another. The example below does something real and useful:

    $ samtools mpileup -P ILLUMINA --BCF --max-depth 100 --adjust-MQ 50 --min-BQ 18 --min-MQ 18 --skip-indels --output-tags DP,AD --fasta-ref buckwheat_ref.fasta aln*sorted.bam | bcftools call -m --variants-only --format-fields GQ --skip-variants indels | bcftools filter --set-GTs . -i 'QUAL > 19 && FMT/GQ >9' | bcftools view -m 2 -M 2 -v snps --apply-filter "PASS" --output-type v --output-file variants_rawfiltered_12JULY18.vcf  &

<p>&nbsp;</p>

## 6. Interacting with remote locations
<p>&nbsp;</p>

### retrieving content from web addresses 
It is quite common to download files, or large batches of files, from web addresses or remote servers. 

`curl` can be used to easily pull data from anywhere. The `-o` option below sets the name of the file in the current directory. 

    $ curl -o genbankreadme.txt ftp://ftp.ncbi.nlm.nih.gov/genbank/README.genbank

`wget` is similarly useful, and similar to execute

    $ wget "https://github.com/tparchman/BIOL792_course_site/blob/master/week1_unixI/science.txt"

If you don't have `wget` installed on your Mac Unix system, we will cover how to install packages next week. For the above link, `curl` would work similarly, although you would need to click on the 'raw' or 'download' buttons in github to get a workable link (notice the difference between the url above and below).

    $ curl -o sci.txt "https://raw.githubusercontent.com/tparchman/BIOL792_course_site/master/week1_unixI/science.txt"
<p>&nbsp;</p>

### Connecting to remote servers and HPC (High Performance Computing) systems

`sftp` (secure file transfer protocol) is a set of Unix tools for secure transfers between remote addresses. We probably won't use it in this course, but it will invetibly be used by anyone retrieving or transferring large amounts of data (i.e., DNA sequencing centers). 

`ssh`: We will learn more about this later in the semester when we connect to remote servers to do work.
<p>&nbsp;</p>

## 7. Writing bash scripts 

Here we will Unix commands to learn to write your first simple programs. We will cover this quickly today, and come back for more next week.

We call scripts, or programs, that execute Unix commands "bash" scripts because we are typically operating in the bash shell. Simply put these are programs consisting of Unix code and arguments that can be written to do simple or surprisingly complicated jobs.

For this, our code will simply be written and stored in a text file. We will use the extension `.sh` rather than `.txt` to signify that this is a Unix or bash script. The first line of such a file (or program) is the "shebang" followed by the location of the bash interpretter on your system.

    #!/usr/bin/bash

To warm up to this idea, lets just print something to screen here. Your bash script thus should have exactly what is below.

    #!/usr/bin/bash 
    echo "Welcome the the Biggest Little City"

Save the file as something like firstbash.sh. Then, you can execute from the command line in one of two ways. One, you can simply type:

    $ bash firstbash.sh

Two, you can change the file to executable, then run, as follows:

    $ chmod a+x firstbash.sh
    $ ./firstbash.sh