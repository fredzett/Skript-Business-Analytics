#!/usr/bin/env python
# coding: utf-8

# # Einführung in Python

# In[1]:


# Execute before using this notebook if using google colab

kernel = str(get_ipython())

if 'google.colab' in kernel:    
    get_ipython().system('wget https://raw.githubusercontent.com/fredzett/rmqa/master/utils.py -P local_modules -nc ')
    get_ipython().system('npx degit fredzett/rmqa/data data')
    import sys
    sys.path.append('local_modules')


# # Learning Python

# In this notebook we will cover some basic aspects of **Python**. 

# In the course of this class we will then gradually introduce new programming/python concepts and/or python modules (don't worry if you don't know what this means, yet) that help us in our data analysis journey. 

# We will not be able to cover all aspects of Python and will only see a tiny fraction of what you can do with Python - both for data analysis and for general programming. 
# 
# Also note that there are many ways to achieve the same thing in programming. Often times there is no such thing as *the* one right approach.

# You should also use alternative sources to broaden and/or deepen your knowledge about Python. Here are some examples:
# 
# - **tutorials**: there is a myriad of Python tutorials, e.g. [this one](https://www.w3schools.com/python/python_intro.asp) 
# 
# - **stackoverflow**: if you get stuck with a coding issue you can almost be certain that someone before has run into the same issue and posted a question on [stackoverflow](https://stackoverflow.com/)

# > **Important Note**  
# > Don't worry if you find yourself struggling to understand all the things at first. Learning to program takes some time and it is completely normal that some of the concepts seem to be difficult at first. But stick with it as you will see that eventually things become more clear. You will also realize how much more you can achieve in empirical academic research and/or business when knowing how to handle data efficiently. 

# # Mathematical expressions

# Programming languages are just like any other (human) language. Except that they are much easier and more precise. There are, of course, some rules of grammar that needs to be understood and learned. 
# 
# Perhaps the most easy rules are those of math which can be used in Python (and most other programming language) using `math operators`.
# 
# Overview of common mathematical expressions:
# 
# | Epression Type  	| Operator 	|  Example 	|   Value 	|
# |----------------	|:--------:	|:--------:	|--------:	|
# | Addition       	|     +    	|   3 + 1  	|       4 	|
# | Subtraction    	|     -    	|   3 - 2  	|      1 	|
# | Multiplication 	|     *    	|   4 * 2  	|       8 	|
# | Division       	|     /    	|   7 / 3  	| 2.66667 	|
# | Remainder      	|     %    	|   7 % 3  	|       1 	|
# | Exponentiation 	|    **    	| 2 ** 2 	| 4 	|
# | Floor division 	|    //    	| 7 // 2 	| 3 	|
# 
# Let' see how this is done in `Python`.
# 
# **Note**: press `shift` + `enter` to excecute a cell

# In[ ]:


7 // 2


# In[ ]:


3 + 1


# In[ ]:


3 - 2


# In[ ]:


4 * 2


# In[ ]:


7/3


# In[ ]:


7 % 3


# **Important**: the operator for `exponentiation` is `**` (not ^ which is common in many other languages including excel). 
# 
# so $2^2 = 4$ in Python becomes

# In[ ]:


2**2


# In[ ]:


7 // 2 # note: floor division calculates 7 / 2 = 3.5 and than removes the digits after the decimal


# Mathematical operators can be combined to compute more complex arithmetics. Python math operations obey the **same rules as in algebra**:
# 
# **Example**
# 
# Formula: $$(3+4)*2+4*\frac{4}{2} = 22$$
# 

# In[ ]:


(3 + 4) * 2 + 4 * 4/2 


# # Name assignment / Variables

# You can name any given value in Python using an assignment statement (`=`)

# In[ ]:


a = 10
b = 30
a + b


# All previously assigned names (here: `a` and `b`) can be used in any other cell once it has been created. 
# 
# **Example:** 
# - `a` and `b` have been created once the above cell was executed (using `shift` + `enter`)
# - both of them can now be used in other cells

# In[ ]:


c = a + b + 10
c


# You can overwrite existing variables names with new values by assigning a new value. Be careful to not accidentally do this!

# In[ ]:


a = -20


# In[ ]:


a + b + 10


# Names must start with a `letter` but can contain both letters and numbers. 
# 
# You should use descriptive names

# In[ ]:


revenue = 100
operating_cost = 50
interest_expense = 10
tax_rate = 0.30

profit = (revenue - operating_cost - interest_expense) * (1 - tax_rate)
profit


# # Data Types

# Python has many build-in `data types`, some of which you have already encountered. 
# 
# So far we have seen two Numeric Types `int` (integer; e.g. 4 or 2) and `float` (floating point decimal, e.g. 4.3 or 2.3456). 
# 
# Python has many other types built-in by default. For a complete list [see here](https://www.w3schools.com/python/python_datatypes.asp).
# 
# In the following we will cover two other data types which are important:
# 
# - Strings: `str`
# - Lists: `list`
# 
# During the course of the class you will encouter other data types. 

# ## Strings

# Variables don't have to be of numeric type but can also be of different types. 
# 
# Sometimes it is helpful to have a variable that stores texts (e.g. when printing a message to the console or when labellling dataframe columns).
# 
# **Example:** `Strings`

# In[ ]:


name = "Felix"
surname = "Zeidler"
full_name = name + " " + surname
full_name


# ## Lists

# Lists are collections that are changeable and orderable and allow duplicate entries. 

# In[ ]:


fruits = ["Apple","Banana","Orange"]
fruits


# In[ ]:


numbers = [1,2,56,394.34]
numbers


# Lists can be accessed in varies ways are handy if you work with collections of data. 

# In[ ]:


first = numbers[0]
first


# In[ ]:


last = fruits[-1]
last


# In[ ]:


first_second = numbers[:2]
first_second


# In[ ]:


last_two = numbers[-2:]
last_two


# List can also be amended by assigning new values to them

# In[ ]:


numbers[0] = 99
numbers


# In[ ]:


fruits[1] = "Pineapple"
fruits


# 
# (Note: next lecture we will learn about `numpy arrays` which are even more handy when doing data analysis or statistics)

# You can also apply mathematical operations to lists to create new lists, e.g.

# In[ ]:


list_apple = ["Apple"]
list_apple * 5


# # Functions

# ## Writing functions

# Python functions take data as arguments (known as parameters) and can return data as a result (here: the average). 
# 
# You have probable already encountered the concept of functions when e.g. using **Excel** where you can use functions such as `=sum(number1; number2)`.
# 
# In Python the concept is the same, however, the syntax rules are different + functions are a bit more flexibel (like using VBA in Excel if we may keep the analogy). 
# 
# Functions follow a special syntax in python
# 
# ```Python
# def name_of_function(parameter):
#     do something
#     return data
# ```

# Functions are a way of abstraction and help to avoid repetitive code.
# 
# Imagine we have a very complicated formula that takes 4 parameters as input

# In[ ]:


p1 = 10
p2 = 20
p3 = 30
p4 = 40
result_of_complicated_formula = p1/p2 + p3/p4 * p1 ** p2*4 - 3 / (p1 + p3)**p4


# What happens if we want to apply the same formula to new input? We have to repeat the entire formula

# In[ ]:


p5 = 20
p6 = 3.45
p7 = 40
p8 = 5
result_of_complicated_formula = p5/p6 + p7/p8 * p5 ** p6*4 - 3 / (p5 + p7)**p8


# This is the **perfect use case** for writing a function: it is helpful to abstract the logic of the formula away into one function and then be able to apply this function multiple times.

# Let's create a simple functions that takes the sum of two values

# In[ ]:


def add(a,b):
    return a + b


# In[ ]:


add(3,4)


# In[ ]:


a = 10
b = 12
add(a,b)


# Note that we can also write the function to use other datatypes as input. Let's create the same functionality by taking a list of two items as input

# In[ ]:


def add_list(l):
    return l[0] + l[1]


# In[ ]:


values = [3,7]
add_list(values)


# Let's apply the concept and create a function that calculates the mean of four values
# 
# $$\bar{x} = \frac{\sum_{i=1}^{N} x_i}{N} $$

# In[ ]:


def mean_ages(a,b,c,d):
    return (a + b + c +d) / 4


# In[ ]:


mean_ages(3,5,6,1)


# ## Build-in python functions

# Luckily we don't have to start from scratch and many functions are already included in Python ([see here for complete list](https://docs.python.org/3/library/functions.html)).

# Use built-in function `sum` to take the sum of a list of *numbers*

# In[ ]:


numbers = [1,2,3,4,5]
sum(numbers)


# Use built-in function `len` to determine the length of the list *numbers*

# In[ ]:


len(numbers)


# Let's improve our mean function using two build in functions:
# 
# - `sum`
# - `len`
# 
# (Note that we need to group our variables togehter in a new data type called `list`)

# In[ ]:


def mean_ages_new(list_of_names):
    return sum(list_of_names)/len(list_of_names)


# Another important build-in function in `print`. It prints out the parameters that are included in this function which is very helpful. 
# 
# It enables us, for example, to print out any variable within a code cell

# In[ ]:


a = 10
b = 12
c = a + b
print(c)
d = c + 10
d


# ## Class functions

# Python objects can also have functions attached to them. A good example for a object is the data type `list` we have previously seen. Lists have functions associated with them.
# 
# We can find out about these functions:
# 
# - by looking up the details of lists in the python documentation ([see here](https://docs.python.org/3/tutorial/datastructures.html))
# 
# - by using **tab completion** by pressing `tab` in Jupyter Notebook or `CTRL` + `SPACE` in Google Colab
# 
# Let's take an example 

# In[ ]:


liste = [1,2,4,5]
liste.append(12) 
liste


# You can learn about the function by typing out the function followed by a `?`

# In[ ]:


get_ipython().run_line_magic('pinfo', 'liste.append')


# In[ ]:


liste = []
liste


# In[ ]:


liste.append(1)
liste


# In[ ]:


liste.append([1,2,3])
liste


# In[ ]:


liste.append("Peter")
liste


# We will gradually introduce many of these associated functions (class methods) as they will make our life easier and avoid coding things from scratch that already exist.

# # For Loop

# ## Regular for-loop

# Imagine for example you have a list with numbers and want to add some constant to this list. 
# 
# Unfortunately, the following operation does not work:

# In[ ]:


numbers = [1,2,3,4,5]
constant = 12
# numbers + constant # Will not work


# We could, of course, achieve this adding the constant to each individual element of the list

# In[ ]:


numbers[0] = numbers[0] + constant
numbers[1] = numbers[1] + constant
numbers[2] = numbers[2] + constant
numbers[3] = numbers[3] + constant
numbers[4] = numbers[4] + constant
numbers


# This seems tedious given the operation is nearly identical each time. In many situation - including the above - we want to repeat the same operation multiple times. 
# 
# In Python - as in many other programming languages - you can achieve this using a `for loop`. The syntax for `for loops` is the following:
# 
# ```Python
# for element in elements:
#     do something
# ```
# 
# Note that elements must be an iterator (e.g. a list)

# In[ ]:


fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print("I like", fruit)


# > **Note**: the inner part of the for loop is indented by four spaces (or tab). This is important! 
# 

# Our previous problem of adding a constant to our list of numbers can be solved using a for loop as follows:

# In[ ]:


numbers = [1,2,3,4,5]
constant = 12


# In[ ]:


numbers_plus_constant = []
for n in numbers:
    numbers_plus_constant.append(n+constant)
numbers_plus_constant


# ## List comprehension

# One specialty about python are `list comprehensions` which are a special (condensed) form of a for loop and provide a concise way to create lists. 
# 
# The pyhton syntax for `list comprehsions` is as follows:
# 
# ```python
# [do something for element in elements]
# 
# ```
# 
# Let's try to solve the previous numbers example using a list comprehension.

# In[ ]:


numbers = [1,2,3,4,5]
constant = 12


# In[ ]:


numbers_plus_constant = [number + constant for number in numbers]
numbers_plus_constant


# Here are some more examples:

# In[ ]:


names_lower = ["Felix", "Murat", "Sibel", "Abdulmutalip"]
names_length = [len(n) for n in names_lower]
names_length


# # Syntax errors

# Whenever your code does not follow the correct language rules (here: python syntax) the system returns a `error message`. These error messages are a somewhat intimidating and cryptic at the beginning. However, they are actually helpful to identify issues with your analysis.
# 
# Let's produce an error message by running the below code

# In[ ]:


name = "Felix"
name / 2


# Usually the last line of the error message gives some hint as to what went wrong. In this case the error message returns a *TypeError* stating that you cannot devide a string (i.e. text) by an integer (i.e. a number). 
# 
# You will run into many error messages in the beginning which is part of the learning process. 
