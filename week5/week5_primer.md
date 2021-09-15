# Why Python ?

The idea of this course is to introduce biologists without any, or much, prior programming experience to a language that can be useful for their needs. The choice of the first programming to learn may not be as important as you think; once you have learned one, learning additional languages will be much much easier, and you are nearly guaranteed to utilize additional languages at some point in your career. Nonetheless, the two scripting languages that have been most heavily used in bioinformatics and data science are **Perl** and **Python**. I have primarily used Perl for my needs, and have taught this course with Perl in the past. However, given a general shift in usage trends and training opportunities, beginning this semester, Ive decided to shift to Python. There are a number of reasons for this:

- It is one of the most common languages used in biology and other fields of science. Thus, you will be able to find a lot of documentation, guidance, examples, and opinion on the web.
- It has excellent capabilities for manipulating text, suiting it well to bioinformatics and data science.
- It uses consistent syntax, which makes learning specific code relatively easy.
- It has many built in libraries to facilitate common tasks
- Python is very widely used, across science and industry. 

<p>&nbsp;</p>

# Getting started with Python. 

## Topics to cover
- installing/updating python
- writing your first python script(s), `print` statements
- working with strings and integers
- Haddock and Dunn chapter 8, and first few pages of chapter 9

# 1. Installing/updating to python 3 current version
As we did with Unix, we are going to start slow and basic, ramping up as the weeks go on. First we are going to make sure everyone has the most recent version of Python installed. While doing this, we are going to take a slight detour to learn how incredibly easy it can be to download and install packages for Unix commands or programs that are not installed in the base system. For this, we will demonstrate the use of `brew`, which is command line utility for locating, downloading, and installing Unix packages on Mac computers.

First check to see if you have python3 installed.  Open the shell and type

    $ python --version

If you get anyting that looks like version 2 not 3 or if you get an error that you dont have python. Then you will need to install version 3.


## Installing or updating Python on Mac Unix using homebrew

If you have already installed Homebrew - you dont need to do this. Check if you have it:

    $ which brew
  
If you dont have it, then:

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Then install python3 

    $ brew install python3bcftools/1.9


### Python downloads, also useful potentially 
Go to python.org and download the latest release

    https://www.python.org/downloads/mac-osx


## Ubuntu
It is probably already installed but if not try with the package manager `apt-get`

    $ sudo apt-get install python idle
	
# 2. Writing your first python program

As with shell scripts, the first line of python scripts should be the shebang followed by the location of python:

    #!/usr/local/bin/python3

or, depending on your system:

    #!/usr/bin/python3


If you are unsure where you installed python3, you can easily figure out where it is:

    $ which python3


As covered in Haddock and Dunn, pg 127, you can also use the below text as your first line. This allows you to send script to `env` first, which should then locate python3, wherever it resides.

    #!/usr/bin/env python3

Either of the above will do, and are important **IF** or when you wish to convert your scripts to executable. If you want to do this, change the file mode: 

    $ chmod u+x first_python.py

And run as follows:

    $ ./first_python.py

## Your first simple program, using a `print` statement.

Sending information from your python scripts to stdout is accomplished with the `print` function. Our first script will simply illustrate how we print specified text, and will serve to convince you that this might not be as hard as you thought it was. Use `touch` to make a blank text file, but give it a `.py` extension as is customary for python scripts. This script needs only two simple parts. First, your customary first line that should go in all of your scripts, which should be:

    #!/usr/bin/env python3
Or the path to the specific location where python lives:

    #!/usr/local/bin/python3

To illustrate the use of `comment` text, marked with `#`, lets add a comment that is for you to read, not python. 

    #this is a comment: testing my first program with a simple print statement

Note the line above will not be part of the interpretted code. Instead, you can make use of `#` to leave annotations for yourself or others in your code to explain what you are doing.

Now lets add a print statement:

    print ("Im ready to learn python, and this is my first step")

You can now run your program in two ways. Simply (which we strongly recommend for this class):

    $ python3 first_script.py 

Or, change to executable, then run:

    $ chmod u+x first_script.py
    $ ./first_script.py

If all is in order, "Im ready to learn python, and this is my first step should print to the screen", and you are ready for more.


<p>&nbsp;</p>
<p>&nbsp;</p>

# 3. Additional resources to help with learning Python

## Jupyter QtConsole (enhanced interactive prompt), and Spyder IDE

Python has command line interactive prompt (we will get into this next week), but I suggest using one of these additional tools to aid your exploration of Python syntax while writing scripts or testing code.

Download the [Anaconda Navigator](https://www.anaconda.com/products/individual-d) suite of tools. From within this you can start the Spyder IDE and or the Jupyter QtConsole from the launch menu.


# Python documentation and other useful resources. 

I strongly recommend you explore several of the below resources and tutorials. They ALL can and will facilitate your progress greatly.

[Python documentation](https://www.python.org/doc/)

[Python for Biologists](https://pythonforbiologists.com/introduction)

[Learn Python Interactive](https://www.learnpython.org/)
 - This has a built in interpretter, so you can test code or play with code under the tutorial examples. Excellent resource.

[Python guru ](https://thepythonguru.com/)
 - This also has a built in interpretter, so you can test code or play with code under the tutorial examples. Excellent resource.


## Note on Python 3 syntax updates and Haddock and Dunn.

 If you are using Haddock and Dunn text, be aware that it is based on python2, and there are some important differences between python2 and python3 (syntax changes that will require slight modification of book examples)


1. print statements in python3 should use (). 
2. `raw_input()` has become just `input()`

