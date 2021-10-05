# Python primer II, Data Science I, Fall 2020. 

## Topics to cover
- lists
- `if`, `else`, and `elif`
- `for` loops
- Haddock and Dunn chapter 9
- updated document that has corrections for python3 where necessary (PythonLesson2_Chapter9.pdf)
<p>&nbsp;</p>

# 1. Lists
Lists store vectors of information, and you will commonly use them. They are convenient because they can be used with loops to execute the same blocks of code on each element.

Hardcoding lists within your scripts is good for learning, although once you start working with real data you will learn to build lists quickly on the fly. To build lists, we enclose the set in brackets. The contents of a list can be a mixture of data types, although you will usually work with lists of only one type (strings, integers, floats)

    NameList = ['Jim', 'Bob', 'Amy', 'Beth']    # list of strings
    NumList = [9, 28, 18, 83, 85]   # list of integers
    BothList =['Jim', 'Bob', 'Amy', '3', '5', '7']

List elements are accessed by their indeces, 0 coming before the first list element. Rather than thinking of each element as matching its index, think of the indeces as representing the boundaries between elements. (see page 159 of Haddock and Dunn for explanation)

    List=('a', 'b', 'c', 'd', 'e')
    print(List[0])  # will print a
    print(List[2])  # will print c
 
List elements are accessed by their indices, -1 is the last list element.

    List=('a', 'b', 'c', 'd', 'e')
    print(List[-1])  # will print e
    print(List[-3:-1])  # will print ('c', 'd') 

Specifying ranges of elements is done using `:`, with indices corresponding to boundaries between elements (see page 159 of Haddock and Dunn for explanation).

    print(List[0:3])  # will print ('a', 'b', 'c')
    print(List[1:4]) # will print ('b', 'c', 'd')
    print(List[-3:]) # will print ('c', 'd', 'e')

Note, that information from strings can be similarly extracted. One difference is that you can not modify a portion of a string, but you can modify portions of a list.

    Names = "TomJoshTrevor"
    print(Names[0:3]) # prints 'Tom'
    print(Names[7:]) # prints 'Trevor'

## Useful functions for working with lists:

`list()` translates a string into a list. This is useful because lists are easy to iterate through, e.g., by using `for`

    NumString="1234533324555434343"
    NumList=list(NumString)    

`str.split` splits a string by specified delimiters. This is common when you have a line of data (\t or , delimited) and you want to make that line into a list that can be worked wiht efficiently.

    Temp="65,76,77,77,65,67,65,45,45,90,91,91"
    List_Temp= Temp.split(",")

`.join()` "joins" elements of a list into a string. Delimiter, if used, is supplied before `.join`

    Bases=['A', 'G', 'G', 'C', 'TTT', 'ATC']
    ''.join(Bases) # no delimiter, creates 'AGGCTTTATC'
    ','.join(Bases) # comma delimiter, creates 'A,G,G,C,TTT,ATC'
    String=','.join(Bases[0:4]) # comma delimiter, sends to variable String

Note that strings and lists store information in a similar manner (See Haddock and Dunn pg 164)

`range()` generates lists of integers based on starting, ending, and interval values. The simplist use is to make a list of integers with specified start and stop points. Notice that the list will end ONE integer before the stop point.

    RanList = list(range(0,9))   
    print(RanList) # [0, 1, 2, 3, 4, 5, 6, 7, 8]

Another value can be added to specify interval between integers.

    RanList = list(range(0,20,2))
    print(RanList) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

`append()` used to add elements to the end of an array

    Breeds=['labrador', 'golden', 'flatcoat', 'chesapeake']
    Breeds.append('curlycoat') #adds 'curlycoat')

Joining two lists together is very simple, just use `+`

    List1 = ["a", "b" , "c"]
    List1 = [1, 2, 3]

    List3 = List1 + List2
    print(list3)

`del()` removes any specified elements from a list
    
    del(Breeds[:2]) #removes the first two elements

`.reverse()` reverses a list. **Note, this function doesn't return a value, it just reverses the existing array.**
 
    Bases=['A', 'G', 'G', 'T', 'T', 'T']
    Bases.reverse()
    print(Bases) # ['T', 'T', 'T', 'G', 'G', 'A']

Reversing strings is a bit less straight forward. The text below looks funny, you will learn more about the meaning of the syntax later (this involves 'slicing')

    Seq='ATCGGGGGG'
    Rev = Seq[::-1]

# 2. `if`, `else`, `elif`

Comparison operators, such as those listed below, will return boolean values in some statements (True or False; 1 or 0). You will find yourself making regular use of these in conditional statements, such as `if`, `else`, and `elif`.
<p>&nbsp;</p>

| Operators | Meaning |
|---------- | ---------- |
|==  | Equal To |
|>   | Greater Than |
|>=  | Greater Than or Equal To |
|<   | Less Than |
|<=  | Less Than or Equal To |
|!=  | Not Equal |
<p>&nbsp;</p>

Logical operators, as listed below are also useful in conditional statements.

| Operator | True if |
|---------- | ---------- |
|and  | Equal To |
|or  | Greater Than |
|not  | Greater Than or Equal To |
|(not A) or B | Less Than |
|not (A or B)| Less Than or Equal To |
<p>&nbsp;</p>

### `if` is used prior to a condition being stated, and code under `if` must be indented:
    X = 4
    if (X > 3):
        print("%d is greater than 3" % (X))

### `else` is used following `if` as below
    if (X >= 3):
        print("%d is greater than or equal to 3" % (X))
    else:
        print("%d is less than 3" % (X))

### `elif` is used when multiple conditions follow the initial `if`
    Y = 3
    if (Y > 3):
        print("%d is greater than 3" % (Y))
    elif (Y == 3):
        print("%d equals 3" % (Y))
    else:
        print("%d is less than 3" % (Y))

# 3. `for`

### `for` can be used with lists, and even strings at some points. Unlike the conditional statements above, `for` is used to loop (or iterate) through a data structure, executing the same block of code on each item. Python uses indentation in an inflexible manner (other languages often use curly brackets with indentation optional) to set apart code inside `for` loops. A common error in your python code will come from incorrect indentation.

### Using `for` to loop through a string. The code below should print each base in the DNA string on its own line of output.

    DNA = "ATCGGGAAACC"
    for Seq in DNA: 
        print(Seq)

### You will often use `for` to loop through arrays. The syntax is similar to above. Lets make a list of numbers and loop through it.

    RanList = list(range(0,100))   
    for Num in RanList:
        if Num%10==0:
            print ("multiple of 10: ", Num)

Notice above we are doing three things. 
- First, we are making a list of integers from 0 through 100. 
- We are then looping through that list with `for`. Note that the statement "for Num in RanList" uses an already named list. Because you are looping through that list, you need to name each element so that it can be referred to within your loop. You can name it whatever you want, here I used "Num". 
- We then put a conditional statement to print something only if that condition is met.
- `%` is the modulo operator. It returns the *remainder* of division. So 10%10 = 0, 20%10 = 0, etc., but 5%10=5.

### While looping through data structures, we will often want to use an incrementer or counter, to keep track of how far we have gone, how far we should go, or how many times we have encountered a particular object. The `+=` tool from last week can be very helpful for this.
    num_a = 0
    num_c = 0
    num_g = 0
    num_t = 0
    DNA_seq = "ATCGGGAAACCTTAAGCTAAA"
    for base in DNA_seq:
        if (base=="A"):
            num_a += 1
        elif (base=="C"):
            num_c += 1
        elif (base=="G"):
            num_g += 1
        else:
            num_t += 1
    
    print("There are %d A bases" % (num_a))        
    print("There are %d C bases" % (num_c))        
    print("There are %d G bases" % (num_g))        
    print("There are %d T bases" % (num_t))        

### Here is an example of how to simply increment a counter to keep track of how far you have gone through a list. If you start with zero, you will essentially be tracking correct list indices (because the first list element is 0)

    List=['1','2','3','4','5','6','7','8','9','10']
    CTR = 0
    for Num in List:
        print("List index is :", CTR)
        CTR += 1    




