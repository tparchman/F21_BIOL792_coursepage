# Python primer VI, Data Science I, Fall 2021. 

## Topics to cover

- Dictionaries
- More work with regular expressions
- Input/Output: using loops to process many files at once.

## Useful materials
- Haddock and Dunn chapters and 9, bit of 11 
- regular expression cheat sheet (python-regular-expressions-cheat-sheet-1.pdf)
- slides from class
- [python for biologists dictionaries tutorial](https://pythonforbiologists.com/tutorial/dictionaries.html)

<p>&nbsp;</p>

## Creating Dictionaries

Dictionaries (also known as associative arrays, or hashes) are data structures that store unordered pairs of objects. Each pair consists of a key and a value. These types of structures that store pairs of data are common to many programming languages for several reasons. First, we often want one piece of information to be directly connected to another (names and phone numbers; gene name and sequence; site identifier and measurement; codons and their associated amino acids). We can pair such data using lists, but this turns out to be quite slow (and clumsy) for larger data because lists have a fixed ordering of elements. Dictionaries are unordered, thus they have the advantage of allowing you to look up or access pairs of information much more quickly.


Dictionaries can be created by listing key:value pairs within curly brackets, with each pair (also referred to as an item) separated by a comma. Below illustrates how to hard code a dictionary (in this case a list of names and phone numbers) consisting of three items:

    Pbook = { 'Ken Stephens':'2599855888','Mick Collins':'3544333321', 'Jen Miles':'9875842194' }

While python has strict indent rules, statements can be split across lines when they are contained within curly brackets. This makes things much easier to read:

    Pbook = { 
        'Ken Stephens':'2599855888', 
        'Mick Collins':'3544333321', 
        'Jen Miles':'9875842194' 
    }

The entire dictionary contents can be printed (although this is seldom useful)

    print(Pbook)
    
Values are extracted from a dictionary by specifying the **dictionary name** and a key. The below would return '9875842194'

    print(Pbook['Jen Miles'])


Here is another dictionary, with western cities as keys and mid October temperatures as values.

    Ctemp = { 
        'Tucson': 95, 
        'Truckee': 65, 
        'Reno': 74,
        'Laramie': 50,
        'Flagstaff': 75,
        'Bozeman': 70,
        'Ketchum': 65 
    }

## Useful dictionary methods.

Before we think about building dictionaries while processing real data, lets use the above example dictionary to demonstrate some commonly used methods to manipulate and extract information from dictionaries.

- `.pop()`
- `.get()`
- `.items()`
- `.keys()`

We can print or assign a specific value to a different variable name simply:

    print(Ctemp['Reno'])    # prints 74 
    Rtemp = Ctemp['Reno']   # assigns 74 to Rtemp

Key:value pairs can be removed from a dictionary using `.pop()`.  

    Ctemp.pop('Tucson')  # will remove Tucson key and 95 value, returns value.
    Ctemp['Tucson']=95  # adds that key:value pair back.


`.keys()` returns a list of dict_keys, `.values()` returns a dict_values list, and `.items()` returns a list of key:value pairs


    vlist=Ctemp.values()
    for v in vlist:
        print(v)  ## prints values

    klist=Ctemp.keys()
    for k in klist:
        print(k)  ## prints keys

    ilist=Ctemp.items()
    for i in ilist:
        print(i)    ## prints items (key:value) pairs

    Ctemp.get('Tucson') ## returns 95, the value for the Tucson key

## Building dictionaries on the fly with real data

We will rarely construct dictionaries by hardcoding them, as above. Instead, we will populate them with key:value pairs as we loop through data. As with lists, we will often want to start with an empty dictionary that we populate within some form of loop. This is done simply with empty curly brackets.

    Dict = {}

Lets look at some example code below that reads in a .fasta file containing alternating lines of identifiers and DNA sequence data. Within the `for` loop, we process two lines at a time, assigning them to different variables. We then build the dictionary "ID_Seq" within the loop, using ID as keys and Seq as values. I like to name dictionaries with two part names that suggest the variables used for keys and values, but like scalars and lists, you can name dictionaries anything you want.

    IN = open(sys.argv[1], 'r')

    ID_Seq={}           # initializing the ID_seq dictionary

    for Line in IN:
	    ID = Line.strip('\n')
	    Seq = IN.readline()
	    Seq = Seq.strip('\n')
    	ID_Seq[ID]=Seq      # building the ID_seq dictionary
    #WORK ON DICTIONARY OUTSIDE OF LIST

## Iterating over dictionaries.

Much like we iterate over lists, we can iterate through dictionaries to access, and operate on, both key and value information within loops. The example code below illustrates using a `for` loop to iterate through the dictionary created above. The `sorted()` function sorts the hash by keys, which ensures that each time you loop through the hash the same order is followed.

    for thing in sorted(ID_Seq.keys()):
        print(thing)
        print(ID_Seq[thing])

Each iteration through the loop above, "thing" is assigned a key. Hence, the code will print to screen each key followed by its value on the following line.

Here are some examples, based on the little Ctemp dictionary created above, of iterating through dictionaries.

    Ctemp = { 
       'Tucson': 95, 
        'Truckee': 65, 
        'Reno': 74,
        'Laramie': 50,
        'Flagstaff': 75,
        'Bozeman': 70,
        'Ketchum': 65 
    }   

    for city in Ctemp.keys():
        print(city)
        print(Ctemp[city])

Above we iterate through the dictionary, and are assigning the keys to the the `city` variable for each time through the loop. The first print statement prints each dictionary key (assigned to `city` in this case), the second statement prints the value assigned to each key. If you look at your output below, you will see that dictionaries are unordered.


    for city in Ctemp.keys():
        print(city)
        print(Ctemp[city])    

To iterate through a dictionary in an ordered manner, we can use the sorted function to iterate by sorted key value. The difference between below and above is the elements are accessed by alphanumeric key value.


    for city in sorted(Ctemp.keys()):
        print(city)
        print(Ctemp[city])


It is often useful to iterate over both key and values (items) in a dictionary to access both simultaneously via different variable names. This is fairly straightforward as well. Using the same Ctemp dictionary as above, but assigning variable names to keys, values and using the `.items()` dictionary function:

    for city, temp in Ctemp.items():
        print(city) # do something with keys
        print(temp) # do something with values

Notic in the above example, variables are assigned between `for` and `in` with the first variable name corresponding with keys, and the second corresponding with values. As usual, the names of those variables are arbitrary.


To finish, here is an example chunk of code to open a file handle, build a dictionary, and then loop through that dictionary.


    IN = open(sys.argv[1], 'r')

    ID_Seq={}           # initializing the ID_seq dictionary

    for Line in IN:
	    ID = Line.strip('\n') # first line corresponds to an ID
	    Seq = IN.readline() #reading second line .fa, a DNA seq
	    Seq = Seq.strip('\n')
    	ID_Seq[ID]=Seq      # building the ID_seq dictionary

    #WORK ON DICTIONARY OUTSIDE OF LIST

    for id, seq in ID_Seq.items():
        if re.search("exon", id):
            OUT1.write(id, 'w')
            Acount += seq.count('A')
        else:
            print("No exon in %s \n" % (id))
       
