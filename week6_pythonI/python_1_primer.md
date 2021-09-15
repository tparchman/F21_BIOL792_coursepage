# Why Python ?

The idea of this course is to introduce biologists without any, or much, prior programming experience to a language that can be useful for their needs. The choice of the first programming language to learn may not be as important as you think; once you have learned one, learning additional languages will be much much easier, and you are nearly guaranteed to utilize additional languages at some point in your career. Nonetheless, the two scripting languages that have been most heavily used in bioinformatics and data science are **Perl** and **Python**. I have primarily used Perl for my needs, and have taught this course with Perl in the past. However, given a general shift in usage trends and training opportunities, beginning this semester, Ive decided to shift to Python. There are a number of reasons for this:

- It is one of the most common languages used in biology and other fields of science. Thus, you will be able to find a lot of documentation, guidance, examples, and opinion on the web.
- It has excellent capabilities for manipulating text, suiting it well to bioinformatics and data science.
- It uses consistent syntax, which makes learning specific code relatively easy.
- It has many built in libraries to facilitate common tasks
- Python is very widely used, across science and inustry. 

<p>&nbsp;</p>

# Getting started with Python. 

## Topics to cover
- installing/updating python
- writing your first python script(s), `print` statements
- working with strings and integers
- controlling float precision
- using the interactive prompt to test code in the terminal
- `help()` and `dir()`
- Haddock and Dunn chapter 8, and first few pages of chapter 9
<p>&nbsp;</p>

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

    $ brew install python3


### Python downloads, also useful potentially 
Go to python.org and download the latest release

    https://www.python.org/downloads/mac-osx


## Ubuntu
It is probably already installed but if not try with the package manager `apt-get`

    $ sudo apt-get install python idle
<p>&nbsp;</p>
	
# 2. Writing your first python program

As with shell scripts, the first line of python scripts should be the shebang followed by the location of python:

    #!/usr/local/bin/python3

If you are unsure where you installed python3, you can easily figure out where it is:

    $ which python3


As covered in Haddock and Dunn, pg 127, you can also use the below as your first line. This allows you to send script to `env` first, which should then locate python3, wherever it resides.

    #!/usr/bin/env python3

Either of the above will do, and are important **IF** or when you wish to convert your scripts to executable. If you want to do this, change the file mode: 

    $ chmod u+x first_python.py

And run as follows:

    $ ./first_python.py

## Your first simple program, using a `print` statement.

Sending information from your python scripts to stdout is accomplished with the `print` statement. Our first script will simply illustrate how we print specified text, and will serve to convince you that this might not be as hard as you thought it was. Use `touch` to make a blank text file, but give it a `.py` extension as is customary for python scripts. This script needs only two simple parts. First, your customary first line that should go in all of your scripts, which should be:

    #!/usr/bin/env python3
Or the path to the specific location where python lives:

    #!/usr/local/bin/python3

To illustrate the use of `comment` text, marked with `#`, lets add a comment that is for you to read, not python. 

    #this is a comment: testing my first program with a simple print statement

Note the line above will not be part of the interpreted code. Instead, you can make use of `#` to leave annotations for yourself or others in your code to explain what you are doing.

Now lets add a print statement:

    print ("Im ready to learn python, and this is my first step")

You can now run your program in two ways. Simply (which we strongly recommend for this class):

    $ python3 first_script.py 

Or, change to executable, then run:

    $ chmod u+x first_script.py
    $ ./first_script.py

If all is in order, "Im ready to learn python, and this is my first step should print to the screen", and you are ready for more.
<p>&nbsp;</p>

# `#`: comment character, annotating your code.
Anytime you use `#`, the rest of the line will be 'commented out'. This means python won't interpret what you write, and that you can write notes or annotations on what your code is doing, to help yourself and others. Make heavy use of this, and when you go back to old or strange code, you will know why you did what you did. When others make good use of this, you can learn more about why/how they did what they did. Use `#` frequently, especially in the early phases of learning python.

In example code below and in other primers, I have put comments to describe some code using `#`.

    print ("This is python code")  # this is a comment to describe the left

<p>&nbsp;</p>

# 3. Working with scalars (strings, integers, floats, etc.)
Chapter 8 of Haddock and Dunn does a nice job of walking you through a script that codes and performs various actions on strings and integers (both types of scalar variables). Lets use that example to cover a few aspects of working with strings and integers in python, including:

- some useful functions 
- built-in string functions
- basic mathematical operations
- using the interactive prompt to test simple code, get help, etc. (`help()`, `dir()`)
- controlling string formatting with `%`
- specifying raw input from the command line (`raw_input()`)
<p>&nbsp;</p>

## 3A. Strings 
Strings can be specified and assigned easily within scripts as below. Note that " or ' can be used to enclose strings, and strings not enclosed will return undefined.

    Team = "lakers"
    Seq_one = "actgaaa"
    Seq_two = "ATCGAA"
    Seq3 = 'atcGGGC'

Strings can be concatenated with `+`:

    Seq_one_two = Seq_one + Seq_two
    print("concatenation example: ", Seq_one_two)

Strings can be repeated with `*`:

    Seq_one_times3 = Seq_one * 3
    print("repeat by multiplier example: ", Seq_one_times3)



### Python has a diverse array of string methods, or functions, that allow efficient work with strings. A few examples below will illustrate the syntax for using these methods.
<p>&nbsp;</p>

`str.upper()` will convert string to uppercase:

    Seq_one_big = Seq_one.upper()

`str.lower()` will convert string to lowercase:

    Seq_one_lower = Seq_one_big.lower()

`str.replace()` will replace a specified character with a different specified character:

    NewSeq_one = Seq_one.replace("a","g")
    print ("Use of str.replace: ", NewSeq_one)

 `str.count()` will return a count of occurences for a specific character:

    Counta_Seq_one = Seq_one.count("a")
    print ("Use of str.count: ", Counta_Seq_one) 

 `str.isalnum()` will return *True* if all characters are alphanumeric, *False* if not.

    Seq_one_alphanum_test = Seq_one.isalnum()
    print ("Use of str.alnum: ", Seq_one_alphanum_test)

<p>&nbsp;</p>

## 3B. Basic mathematical operations
Basic mathematical operations work mostly as expected, and can be usefully tested using interactive prompt from the terminal (see below).  


| Arithmetic | Operators |
| ----------- | --------- |
| +  |  Addition |
| - |   Subtraction |
| * |   Multiplication |
| / |   Division |
| // |  Floor Division |
| % |   Modulo |
| ** |   Power |


<p>&nbsp;</p>

Comparison operators, such as those listed below, can return boolean values in some statements (True or False; 1 or 0). You will find yourself making regular use of these in conditional statements, such as `if`, `if else`, etc.

| Comparison | Operators |
|---------- | ---------- |
|==  | Equal To |
|>   | Greater Than |
|>=  | Greater Than or Equal To |
|<   | Less Than |
|<=  | Less Than or Equal To |
|!=  | Not Equal |

<p>&nbsp;</p>

Most basic mathematical operations work in an unsurprsing manner.

    Num1 = 5
    Num2 = 7
    Sum = Num1 + Num2
    Prod = Num1 * Num2
    Dif = Num1 - Num2
    Div = Num1 / Num2
    Mod = Num2 % Num1
    print (Sum, Prod, Dif, Div, Mod)

If you use the code above in a script, or more efficiently, test it out with the interactive prompt (see below), the print statement should illustrate teh expected behavior of the math statements above. **Note that "Div" (5/7) returns a float with many digits past the decimal (0.7142857142857143). This is an overkill level of precision for some uses, and you will often want to control float precision for tidiness.** We will cover that type of control below.

<p>&nbsp;</p>

# 4. Strings, Scalars, and Integers. How to specify, how to know what a scalar variable is.

## 4A. Checking variables
If you arent sure whether a variable is an integer, string, or float, you can easily check using the `type()` function.

    Var = 1.2
    type(Var)     # will return <class 'float' >

    Var = 12
    type(Var)     # will return <class 'int'>

    Seq = 'atcgaaa'
    type(Seq)       # will return <class 'str'>

If you want to change among variables, you have some options with the `float`, `int`, and `str` functions.

    Var = 1.2
    Svar = string(Var)      # makes Svar="1.2", a string
    type(Svar)
    Nvar = float(Svar)      # makes Nvar=1.2, a float

## 4B. `%` operator: controlling format of scalars in print statements 

### In print statements, the first `%` is used as a placeholder that denotes what type of variable is to be specified:  %d for integer, %f for float, and %s for string. After the quoted statement, the second `%` is used before the variabe name is provided in (). %f is also used to specify the number of digits after a decimal (see below).

Have a look at the examples in Haddock and Dunn. Here are a few more. The first uses a string assigned to the variable name within the print statement.

    Name='Lebron'
    print("38 points, 10 assists, 16 rebounds for %s" %(Name))
    # will print: 38 points, 10 assists, 16 rebounds for Lebron

The example below stores three integers. They are each separately printed within quotes in the print statement, using `%d` notation for each. Note, that the order of those variables is then 

    P=38
    A=10
    R=16
    print("%d points, %d assists, %d rebounds for Lebron" %(P, A, R))
    # will print" 38 points, 10 assists, 16 rebounds for Lebron


In python, floats can be represented with full precision, or controlled to a set number of positions. The latter will often be desirable to keep things tidy. The statements below will print 0.6666666666666666.

    Prod = 2/3
    print ("2/3 should equal roughly %.3f" % (Prod))
    # This will print "2/3 should equal roughly 0.667"

# 5. Using the interactive prompt to test statements or blocks of code outside of your scripts, and/or to get help (`help()`, `dir()`)

### 5A. A useful feature of python is the interactive prompt, which you can invoke by simply typing python (or python3, depending on your set up), as below.

    [tparchman@Thomass-MacBook-Pro python1]$ python
    Python 3.8.5 (default, Aug 16 2020, 12:28:59) 
    [Clang 9.0.0 (clang-900.0.39.2)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

 You can usefully use the interactive prompt to test statements or operations while you are writing scripts. Some find it useful to keep the interactive prompt open next to their text editors while writing python code (Haddock and Dunn page ). Follow the example below, which demonstrates the use of +=.  

    >>> a = 7
    >>> a += 7
    >>> a
    14  

Here is another example, where I am demonstrating string assignment, and the use of `str.replace`:

    >>> Seq='ATCGGGGGGG'
    >>> Rep_Seq = Seq.replace('G','T')
    >>> print(Rep_Seq)
    ATCTTTTTTT

Finally, have a look at what happens when the code you are trying ISN'T right. Below, a string is not formatted correctly in the variable assingment statement.

    >>> Seq= ATCGCCCCC
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'ATCGCCCCC' is not defined

In another example, I forgot to place parentheses around the variable which I am sending to the `print` function. Note here that the `^` is helpfully placed as a suggestion of where the error is coming from, and the correct syntax is suggested in the `SyntaxError` statement.

    >>> print Rep_Seq
    File "<stdin>", line 1
    print Rep_Seq
          ^
    SyntaxError: Missing parentheses in call to 'print'. Did you mean print(Rep_Seq)?

Note, for the examples shown above in sections 3A and 3B could be tested using the interactive prompt.
<p>&nbsp;</p>

### 5B. The interactive prompt is also useful for using `help()` and `dir()`. Try these with a few functions, you will quickly see the usefulness.
<p>&nbsp;</p>

### `help()` will print manual page descriptions of the function placed in parentheses. 

    >>> help(print)

    Help on built-in function print in module builtins:

    print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

<p>&nbsp;</p>

### `dir()` returns all properties and methods associated with the specified variable. Below the function is being used with a string.
    Name='Costanza'
    dir(str)
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

<p>&nbsp;</p>

# 6. Pulling raw input from the command line (`raw_input()`)
We will learn more about getting input of all sorts into our python programs in the coming weeks. During the early weeks, we will most often work with variables we build within scripts. Haddock and Dunn cover the `input()` function in chapter 8, which we will reiterate here, and which you will use for the python assignment exercises this week. **Note: this function was named `raw_input` in python2, and is covered as such in Haddock and Dunn. The updated document available under week6 ("PythonLesson1_Chapter8.docx") reflects this and other modifications to python3.**

    name3 = input("Enter a string: ")

If you add the statement above to a script, two things will happen.
After executing the script, you will be prompted at the command line with "Enter a string". Here you can enter any string you like, and hit enter. The provided text will then be stored as the variable as specified in your code.

<p>&nbsp;</p>
<p>&nbsp;</p>


# Python documentation and other useful resources

[Python documentation](https://www.python.org/doc/)

[Python for Biologists](https://pythonforbiologists.com/introduction)

### Chapter 8 differences between python2 and python3 (syntax changes that will require slight modification of book examples)

1. print statements in python3 should use (). 
2. `raw_input()` has become just `input()`