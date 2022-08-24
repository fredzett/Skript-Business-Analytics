#!/usr/bin/env python
# coding: utf-8

# # Einführung in Numpy

# Numpy is one of the most important libraries / modules in python. It is especially useful when working with numerical arrays (which researchers usually do). 
# 
# **Why is `numpy` so important:** 
# 
# - useful when working with numerical arrays (which researchers usually do)
# - enables store and manipulate in-memory data in Python
# - very fast (roughly $~50x$ faster than python's lists (which makes a hugh difference when working with large datasets)
# 
# Numpy's functionality is very broad and we will not be able to cover all of it in this course. We will, however, focus on some basic functionality that will make your life easier when working with (research) data. 
# 
# Also don't forget that you can always use `np.<TAB>` to display contents of functionality.

# # Creating arrays

# Creating a scalar

# In[1]:


import numpy as np


# In[ ]:


scalar = np.array(12)
scalar


# This is not very useful, however. Let's create some arrays from lists (or lists of lists) and from scratch using numpy.

# ## from lists

# Arrays (such as vectors or matrices) can be created from Python's lists

# In[ ]:


vector = np.array([1,2,3,4,5])
vector


# Unlike lists `np.array` must only contain one data type (such as int, float, str). So the following is possible, but it converts all three data types to string.

# In[ ]:


lst = [1,2,3,"A","B",True]
str_vector = np.array(lst)
str_vector


# Using numpy one can also create multidimensional arrays. 

# In[ ]:


matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix


# ## from scratch

# For larger arrays it is usually more efficient to create arrays from scratch using internal NumPy functionality. 

# In[ ]:


# Create an array filled with a linear sequence starting at 0 and ending at 40, step size = 4
array = np.arange(0,41,4) # Note that np.arange defines intervals [a,b), i.e. the upper limit is not included
array


# In[ ]:


# Create an array of 20 values evenly distributed between 10 and 40
array = np.linspace(10,40,20)
array


# In[ ]:


# Create an array of dimension 4x5 filled with zeros
np.zeros((4,5))


# In[ ]:


# Create an array of dimension 2x5 of random values between 0 and 1 (uniform distribution)
# Note that numbers change if you execute cell again
np.random.random((2,5))


# In[ ]:


# Create an array of dimension 3x3x4 of random integers between [5,12)
# Note that numbers change if you execute cell again
np.random.randint(5,12,(3,3,4))


# ## Checking shape and size of an array

# Using `.shape` returns the dimension of the array

# In[ ]:


matrix = np.random.randint(10,20,(4,3))
matrix.shape


# In[ ]:


matrix_3d = np.zeros((4,5,6))
matrix_3d.shape


# Using the `.size` function returns the size (i.e. the number of elements)

# In[ ]:


matrix_3d.size # 4 x 5 x 6 = 120


# # Accessing arrays

# Numpy arrays can be accessed via indexing and slicing.
# 
# **Note**: as with lists the first element is at index level 0!

# ## Indexing

# In[ ]:


x = np.array([6,1,42,2,8,9])
x


# In[ ]:


x[0] # get 0th element


# In[ ]:


x[2] # get second element


# In[ ]:


x[-2] # get second last element


# Multidimensional arrays can be accessed using indices separated by commas

# In[ ]:


x = np.array([[1,2,3],[6,5,4],[100,200,300]])
x


# In[ ]:


x[0,2] # get element in 0th row and 2nd column 


# In[ ]:


x[2,0] # get element in 2nd row and 0th column


# Value assigment on existing numpy arrays using the above index rules is possible

# In[ ]:


x[2,0] = 123
x


# ## Slicing

# Numpy arrays can be sliced meaning taking elements from index $i_{start}$ to $i_{end}$.
# 
# Instead of a single index we simply pass a slice: `start:end` or `start:end:step`

# In[ ]:


arr = np.arange(0,21)
arr


# In[ ]:


arr[2:4] # get elements 2 and 3


# In[ ]:


arr[:5] # get first 5 elements


# In[ ]:


arr[-5:] # get last 5 elements


# In[ ]:


arr[5:16:2] # between elements 5 and 16 get every second element


# The same can be done using multidimensinal arrays

# In[ ]:


mat = np.random.randint(0,10,(5,3))
mat


# In[ ]:


mat[:2,2] # from rows 0 and 1 get the second column


# In[ ]:


mat[1,:] # from row 1 get all columns


# In[ ]:


mat[2:4,1:3] # from rows 2 and 3 get columns 1 and 2


# # Reshaping of arrays

# Sometimes it is necessary to reshape arrays. Here are some examples

# In[ ]:


x = np.arange(1,21,1) # create array of shape (20,), i.e. a column vector with 20 elements
x, x.shape


# In[ ]:


x = x.reshape((1,20)) # convert column vector into row vector
x, x.shape


# In[ ]:


x = x.reshape(5,4) # convert vector into 5x4 matrix
x, x.shape


# # Concatenation

# One can join two arrays in NumPy several ways. The three most useful functions are: `np.concatenate`, `np.vstack`, `np.hstack`

# In[ ]:


a = np.array([10,11,12])
b = np.array([100,200,300])
c = np.random.random(2)


# One can use `np.concatenate` to join both arrays by passing both of them in a list (or tuple).

# In[ ]:


np.concatenate([a,b])


# You can also concatenate more than two arrays.

# In[ ]:


np.concatenate((a,b,c))


# When working with arrays of different dimensions you can use `np.vstack` and `np.hstack`

# In[ ]:


a = np.array([1,2,3])
b = np.array([[4,5,6], [7,8,9], [10,11,12]])
a, b


# In[ ]:


a.shape


# In[ ]:


np.vstack((a,b)) # Stack arrays vertical


# In[ ]:


a = a.reshape(3,1) # Column vector
np.hstack((b,a)) # stack arrays horizontally


# # Splitting

# Instead of joining you may want to split arrays. The tree most useful functions are: `np.split`, `np.vsplit`, `np.hsplit`. 
# 
# All functions basically do the opposite of their concatenation counterparts.

# In[ ]:


a = np.arange(1,10,1)
a


# In[ ]:


a1, a2 = np.split(a,[3])
a1, a2


# In[ ]:


a1, a2, a3 = np.split(a,[4,7])
a1,a2,a3


# In[ ]:


matrix = np.arange(0,16).reshape((4, 4))
matrix


# In[ ]:


np.vsplit(matrix,[2])


# In[ ]:


np.hsplit(matrix,[3])


# # Calculating with arrays

# Using NumPy for calculations has many advantages. Especially it is much faster and often more convenient than using lists and for loops. 

# When using lists calculations can become quite tedious. 
# 
# Example: let's take a vector, add a scalar to that vector (elementwise) and then take the sum.

# In[ ]:


data = [1,2,3,4,5]
data_plus_5 = [i + 5 for i in data]
sum(data_plus_5)


# This is much easier and more intuitive in NumPy as we are not required to use for loops but instead apply the operation "+ 5" to each element of the vector automatically (note: this is done using vectorization).

# In[ ]:


data = np.array([1,2,3,4,5])
sum(data + 5) # alternatively you can also use np.sum


# Turns out this approach is also much faster than using for loops (in below example iit is roughly $1000x$ times faster)

# In[ ]:


data = np.arange(1,10_000)


# In[ ]:


get_ipython().run_line_magic('timeit', 'np.sum(data + 5) # takes about 10 micro seconds (10/1000000 seconds)')


# In[ ]:


def add_5(data):
    output = np.empty(len(data))
    for i in range(len(data)):
        output[i] = data[i] + 5
    return output


# In[ ]:


get_ipython().run_line_magic('timeit', 'add_5(data) # takes 3.7 milli seconds (3.7/1000 seconds)')


# ## Arithmetic operators

# One can use all reguar arithmetic operator.

# In[ ]:


data = np.arange(10)
print("data", data)
print("data + 5", data + 5)
print("data - 5", data - 5)
print("data * 5", data * 5)
print("data / 5", data / 5)
print("data ^ 5", data ** 5)


# ## Exponents and logarithms

# In[ ]:


x = np.array([1,2,3])
print("x    =", x)
print("e^x  =", np.exp(x))
print("5^x  =", np.power(5,x))


# In[ ]:


x = np.array([1,2,4,10])
print("x        =", x)
print("ln(x)    =", np.log(x))
print("log2(x)  =", np.log2(x))
print("log10(x) =", np.log10(x))


# 
# 
# **Note** Recap logarithm:
# 
# $$a^b = c$$
# 
# where:
# 
# $a = $ base
# 
# $b = $ exponent
# 
# Logarithm:
# 
# $$ log_a(c) = b$$
# 
# **Example**:
# 
# $$2^5 = 32$$
# 
# $$log_2(32) = 5$$

# In[ ]:


np.log2(32)


# ## Arithmetics on multiple arrays

# In[ ]:


x = np.arange(1,10)
y = np.arange(11,20)
x + y


# ## Aggregating values in an array

# In[ ]:


x = np.array([1,2,3,4])


# In[ ]:


np.sum(x) # 1 + 2 + 3 + 4


# In[ ]:


np.prod(x) # 1 * 2 * 3 * 4


# In[ ]:


np.min(x) # Minimum value of x


# In[ ]:


np.max(x) # Maximum value of x


# In[ ]:


np.argmin(x) # index where minimum value


# In[ ]:


np.argmax(x) # index where maximum value


# In[ ]:


np.std(x) # Standard deviation (of population)


# In[ ]:


np.std(x,ddof=1) # Standard deviation (of sample)


# ....

# For multidimensional arrays these functions can also be used and be applied to either rows or columns.

# In[ ]:


X = np.arange(1,101).reshape(20,5)
X


# In[ ]:


np.sum(X,axis=0) # take sum for each column


# In[ ]:


np.sum(X, axis=1) # take sum for each row


# ### Example: calculate z-score

# Let's assume we have tabular data with 5 columns. Each column represents a certain feature each of which we want to normalize using a **z-score**.
# 
# For this we need:
# 
# - to know the mean and the standard deviation for each column 
# - to apply (column specific) mean and standard deviation to each element of a column
# 
# Using NumPy we can do this in one line of code

# In[ ]:


X = np.random.random((20,5)) # Define data


# In[ ]:


zscores = (X - X.mean(axis=0)) / X.std(axis=0)
zscores


# In[ ]:


print("Mean by column = ", zscores.mean(axis=0)) # should be ~0
print("Standard deviation by column = ", zscores.std(axis=0)) # should be ~1


# # Comparisons

# ## Boolean masks

# When you need to analyse an arrays with respect to some kind of criterion, masking helps. For example, you might wish to count all values greater than a certain value, or perhaps remove all outliers that are above some threshold. In NumPy, boolean masking is often the most efficient way to accomplish these types of tasks.

# Let's create some random data to show how boolean masking works. 
# 
# Here: we create an array with 10_000 elements. Each element is chosen based on a draw from a sample of number $1, 2, \ldots, 5$ with probability $p$.

# In[ ]:


data = np.random.choice([1,2,3,4,5], size=10_000, p=[0.2,0.1,0.1,0.3,0.3])
data, data.shape


# Let's count the elements that are $\geq 3$

# In[ ]:


np.sum(data >=3)


# In[ ]:


data >= 3


# Let's determine the sum of elements that are equal to 4

# In[ ]:


np.sum(data[data == 4])


# How many numbers are $\neq 4$

# In[ ]:


np.sum(data != 4)


# Are there any numbers $> 5$ in the array?

# In[ ]:


np.any(data > 5) # No!


# In[ ]:


np.all(data <= 5)


# Note that this works also for multidimensional data. 
# 
# Let's reshape the data to a $2.000 \times 5$ dimension and count number of elements equal to 2 per column

# In[ ]:


data = data.reshape(2000,5)
np.sum(data==2, axis=0)


# In[ ]:


data[data==2]


# ## Boolean operators

# We can use **boolean operators** if we have more than one condition. This is very helpfull when putting conditions on our data. Let's consider the three most useful ones:
# 
# - AND `&`
# - OR `|`
# - NOT `~` (negation)

# In[ ]:


data = np.random.randint(1,11,size=100_000) # Random data between 1 and 10
data[:5] # first 5 entries


# Let's count the number of elements that are *above 3* `AND` *below 6*. 

# In[ ]:


cond = (data > 3) & (data < 6)
np.sum(cond)


# Note: given we are looking for the number of elements that are $4$ or $5$ this should sum up roughly to $2/10$ of the data

# In[ ]:


np.sum(cond) / len(cond)


# Let's find the number of elements that have the value $1$ `OR` $7$.

# In[ ]:


cond = (data == 1) | (data == 7)
np.sum(cond)


# Let's take the opposite of the above condition and count the number of elements that are `NOT` $1$ `AND` `NOT`$7$. We can do this negating the above statement using `~`

# In[ ]:


np.sum(~cond)


# Let's check if the result makes sense. Together both statements should result in the entire data.

# In[ ]:


np.sum(cond) + np.sum(~cond) == 100_000


# # Using structured data

# Note: one can use numpy to also work with structured data. Think of structured data as an excel spreadsheet with column headers. 
# 
# Let's read in a csv file with salaries data. The data set contains:
# 
# - three columns with 100 elements each
# - columns represent work experience
#     - column 1 (0-5 years)
#     - column 2 (6-10 years)
#     - column 3 (>10 years)
#     
# > **NOTE:** we will later on use another library called `pandas` that is build on numpy and handels structured data even better

# In[ ]:


path = "./data/salaries.csv"
salaries_by_experience = np.recfromcsv(path)
salaries_by_experience


# In[ ]:


columns = salaries_by_experience.dtype
columns.names


# We can than access each individual column by its name

# In[ ]:


salaries_by_experience["610yrs"]


# Let's compare the mean salaries per experience group

# In[ ]:


names = columns.names
means = [np.mean(salaries_by_experience[n]) for n in names]
means


# > **Advanced** We can make this even more flexible and write a function that takes another function as an input

# In[ ]:


def calc_stat(arr,f):
    names = arr.dtype.names
    return [f(arr[n]) for n in names]


# In[ ]:


calc_stat(salaries_by_experience, np.mean)


# In[ ]:


calc_stat(salaries_by_experience, np.std)


# In[ ]:


def trimmed_mean(arr):
    low, up = np.percentile(arr,5), np.percentile(arr,95)
    return np.mean(arr[(arr>low) & (arr< up)])


# In[ ]:


calc_stat(salaries_by_experience, trimmed_mean)


# # Sneak Preview to `pandas`

# The above can be handeled even easier by using `pandas`. Pandas is built on numpy the functionality is very similar. 

# In[ ]:


import pandas as pd


# In[ ]:


path = "./data/salaries.csv"
data = pd.read_csv(path)


# In[ ]:


data


# In[ ]:


data.mean()


# In[ ]:


data.describe()


# In[ ]:


data.plot(kind="hist")


# In[ ]:


data.plot(kind="line")

