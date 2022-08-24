#!/usr/bin/env python
# coding: utf-8

# # Deskriptive Statistik
# 

# This notebook is a refresher on basic **descriptive statistics**. It is assumed that this material has been covered in an undergraduate statistics course before. We will use our existing knowledge and practically apply it in Python. 
# 
# To this end, the main learning goals of this Chapter are:
# 
# **A/ Provide you with a quick refresher on**
# 
# - measures of location: mean, median, percentiles, quartiles
# - measures of variability: range, variance, standard deviation
# 
# **B/ Practice coding in Python**
# 
# - we will implement most concepts from scratch
# - we will learn that most concepts applied in this course have already been programmed in python and packaged into modules
# - we will start using some relevant modules
# 

# # Measures of location

# A location parameter of a (probability) distribution is a scalar parameter, which determines the "location" or shift of the distribution. 
# 
# We will be using the following monthly sales data from **Statistics Inc.**:
# 
# | Month | Sales |
# |:-----:|:-----:|
# |   1   |  2020 |
# |   2   |  2075 |
# |   3   |  2125 |
# |   4   |  2040 |
# |   5   |  1980 |
# |   6   |  1955 |
# |   7   |  2050 |
# |   8   |  2165 |
# |   9   |  2070 |
# |   10  |  2260 |
# |   11  |  2060 |
# |   12  |  2040 |

# In[2]:


def load_sales(): 
    return [2020,2075, 2125, 2040, 1980, 1955, 2050, 2165, 2070, 2260, 2060, 2040]


# In[3]:


sales = load_sales()


# ## Mean

# ### Definition

# Likely the most important and most known measure of location is the `mean`, also called average value for a given variable.
# 
# Two different means depending on the data:
# 
# 1. if data from a sample: mean is denoted by $\bar{x}$
# 
# 2. if data from a population: mean is denoted by $\mu$
# 
# The value of variable $X$ for the $i^{th}$ observation is denoted by $x_i$.

# **Sample mean** for a sample with $n$ observations:
# 
# $$\bar{x} = \frac{\sum{x_i}}{n}$$

# **Population mean** is the same (except for different notation):
# 
# $$\mu = \frac{\sum{x_i}}{N}$$

# where 
# - sample: a set that contains some members of a population 
# - population: a set that contains all members of a group
# 

# > **Note** The result for sample and population mean is identical. We use different notation only to indicate whether mean is from population or sample. 

# ### Implementation 

# The mean can easily be calculated using the below python code

# In[4]:


x_bar = sum(sales)/len(sales)
x_bar


# If we intend to apply the calculation of a mean on various variables, it is handy to put the concept into a function

# In[5]:


def mean(lst):
    return sum(lst)/len(lst)


# In[6]:


mean(sales)


# ## Median

# ### Definition

# The median is another measure of location. The median is the middle value when data is sorted in ascending order. 
# 
# The **median** of a variable is defined as:
#   \begin{equation}
#     median=
#     \begin{cases}
#       x_{((n + 1)/2)}, & \text{if $n$ is odd} \\
#       \dfrac{1}{2}\big(x_{n/2} + x_{(n/2 + 1)}\big), & \text{if $n$ is even}
#     \end{cases}
#   \end{equation}
# 
# The median is less sensitive to outliers than the **mean** and hence is a more robust measure of the center of a distribution.
# 
# Therefore, the following steps need to be processed to calculate the median
# 
# 1. Arrange the data in ascending order
# 2. Determine number of elements
# 3. Calculate median:
#     1. for an odd number of observations, the median is the middle value
#     2. for an even number of observations, the median is the average of the two middle values

# ### **Naive implementation**

# A simple and naive implementation of mean would look as follows:
# 
# Elements: 0 1 2 3 4 **5 6** 7 8 9 10 11
# 
# We need to take the average of indices 5 and 6. 

# In[ ]:


(sales[5] + sales[6])/2


# In[ ]:


mean([sales[5], sales[6]])


# This approach is, however, not reproducabel with other lists. 

# ### **Better implementation**

# Let's calculate the mean of the sales data by following the above steps in a more general form. We need to introduce 
# 
# - `list.sort()`: a method (i.e. function) for lists sorting lists in ascending order
# - `comparison operators`: operators to compare two values (e.g. if a is greater than b)
# - `if conditions`: instruct python what to do something if a statement is true or false

# **1. Sort sales data in ascending order**

# In[ ]:


sales.sort()


# **2. Determine number of elements**

# In[ ]:


n = len(sales)


# **3. Calculate median depending by checking if odd or even number of elements**

# In[ ]:


if n % 2 == 0: # List has even number of elements (used remainder operator to check this)
    el1 = sales[n//2] # Floor division 7 / 2 = 3.5; 7 // 2 = 3
    el2 = sales[n//2 - 1]
    median = (el1 + el2)/2
else: # List has odd number of elements
    median = sales[n//2]
median


# In[ ]:


def median(lst):
    lst.sort()
    n = len(lst)
    
    if n % 2 == 0: # List has even number of elements
    
        el1 = lst[n//2]
        el2 = lst[n//2 - 1]
        median = (el1 + el2)/2
    
    else: # List has odd number of elements
        
        median = lst[n//2]
    
    return median


# In[ ]:


numbers = [1,2,3,4,5,6]
median(numbers)


# Advantage of median of mean: mean is influenced by small or large outliers. This is not the case for the median. 
# 
# Example:

# In[ ]:


sales_with_outliers = sales + [100_000]
sales_with_outliers


# In[ ]:


mean(sales_with_outliers)


# In[ ]:


median(sales_with_outliers)


# ## Mode

# ### Definition

# Another measure of location is the `mode`. 
# 
# **Mode**: the mode is the value that occurs most often within a set of numbers.
# 
# If there are no repeats in the data the mode is not defines. 
# 
# The mode is an important measure of location for qualitative data (i.e. non numeric data). A data set can have more than one mode. A data set with two modes is called bimodal. A data set with more than two modes is called multimodal. 
# 
# Similar to the median the mode is not affected by extreme outlieres.

# ### Implementation from scratch

# While the statistical concept is straight forward the implementation in Python is not trivial for beginners.
# 
# Here is one possible implementation from scratch (don't worry if it is not entirely clear to you)

# In[ ]:


max(set(sales), key=sales.count)


# ### Implementation using modules

# We have reached a point where it becomes quite tedious to implement all concept from scratch. Luckily, most of the concepts we will be using in this class (or actually most concepts in statistics or data analysis) have already been implemented in Python and can `imported` into python. 
# 
# We need to introduce a new concept:
# 
# - `import modules`: use (e.g. statistical) concepts that have already been implemented in Python

# In[ ]:


import statistics


# In[ ]:


statistics.mode(sales)


# In[ ]:


letters = ["a","b","b","a","d","a","a","c"]
statistics.mode(letters)


# ## Percentiles

# ### Definition

# A percentile provides information about how the data is spread over the interval from smallest value to largest value.
# 
# > **Percentile** is defined as:
# > 
# > The $p^{th}$ percentile is a value such that *at least* $p$ percent of the observations are less than or equal to this value and *at least* $(100 - p)$ per cent of the observations are greater than the value.
# 
# In statistics percentiles are often used to 
# 
# (i) express the spread of data and 
# 
# (ii) to remove outliers (e.g. every value $> 95^{th}$ percentile is removed).

# **Calculation** of the $p^{th}$ percentile is done in three steps:
# 
# 1. Sort the data in ascending order (i.e. smallest to largest value)
# 
# 2. Compute an index $i$
# 
# $$i = \bigg(\frac{p}{100}\bigg)\times n$$
# 
# where $p$ is the percentiles of interest and n is the number of observations. 
# 
# 3. Two options:
# 
#     - $i$ *is not* an integer: the next integer greater than $i$ denotes the position of the $p^{th}$ percentile
# 
#     - $i$ *is* an interger: the $p^{th}$ percentile is the average of the values in positions $i$ and $i + 1$
# 
# 
# 
# **Note** 
# 
# - there are different conventions to calculate percentiles (e.g. round down if $i$ is not an integer). The specific method become less important the more observations we have. 
# 
# - the 50th percentile is equal to the median
# 

# ### Implementation

# Let's use our sales data and calculate the $85^{th}$ percentile. 

# In[ ]:


sales = load_sales() # Reload clean sales data


# **Step 1:** Sort the data in ascending order (using `sort`)

# In[ ]:


sales.sort()
sales


# **Step 2:** compute index $i$

# In[ ]:


idx = (85/100)*len(sales)
idx = idx - 1 # Note: in Python the first position has the index 0 (not 1)
idx


# **Step 3:** calculate percentile
# 
# First, we need to determine if `idx` is an integer. Second we need to round up if the number is not an integer. For this we need one new function and one new module
# 
# - `is_integer()`: To check if a number is an integer (i.e. a whole number)
# - `import math`: import module with math functionality

# In[ ]:


import math 

if idx.is_integer() == False: # Note: use stackoverflow to get help
    position = math.ceil(idx)
    percentile = sales[position]
else:
    idx = int(idx)
    percentile = (sales[idx] + sales[idx +1 ])/2
percentile


# $85\%$ of all sales values are below $2.165$. 
# 
# Let's put everything together into one function. The function should take two arguments:
# 
# - list of values: denoted `lst`
# - $p^{th}$ percentile: denoted `p`

# In[ ]:


def percentile(lst, p):
    lst.sort()
    idx = (p/100)*len(lst) - 1
    
    if idx.is_integer() == False:
        position = math.ceil(idx)
        percentile = lst[position]
    else:
        idx = int(idx)
        percentile = (lst[idx] + lst[idx +1 ])/2
        
    return percentile


# We can now calculate percentiles for any given $p$.
# 
# For example: let's calculate the $15^{th}$ percentile by using our funtion.

# In[ ]:


percentile(sales, 85)


# ### Implementation using `numpy`

# In practice researchers or data analysts wouldn't implement these "algorithms" from scratch. Instead modules that provide such functionalities are used. 
# 
# We can easily calculate percentiles using a new module:
# 
# - `import numpy`: numpy is one of the most fundamental packages providing functionality for scientific computing

# In[ ]:


import numpy as np


# In[ ]:


sales = load_sales()
percentile = np.percentile(sales, q=85)
percentile


# Note that the result using numpy differs from previous result. This is due to the percentile function applying a different method for interpolation. We can fix this by providing an additional parameter

# In[ ]:


np.percentile(sales, q=85, interpolation="higher")


# In[ ]:


np.percentile? # np.percentile??


# ## Quantiles

# ### Definition

# In statistics it is often helpful to divide data into equally sized groups called **quantiles**.
# 
# The include quartiles (dividing the observation into 4 groups) and percentiles (100 groups)#:
# 
# - $Q_1$ = lower quartile, $25^{th}$ percentile
# - $Q_2$ = median, $50^{th}$ percentile (equal to the median)
# - $Q_3$ = upper quartile, $75^{th}$ percentile
# 
# 
# 
# 
# 
# 

# The difference between the upper and lower quartiles is called the **interquartile range** and measures the spread of a distribution

# ### Implementation

# Using `numpy` you can easily calculate quartiles as follows:

# In[ ]:


sales = load_sales()
quartiles = np.quantile(sales,q=[0.25,0.5,0.75])
quartiles


# You can also use other quantiles, e.g.

# In[ ]:


quantiles = np.quantile(sales, q=[0.1,0.5,0.9])
quantiles


# In[ ]:


interquartile_range = quantiles[-1] - quantiles[0]
interquartile_range


# # Measures of Variability

# ## Standard deviation & variance

# ### Definition

# The **standard deviation** measures the average deviation from the mean and is defined as follows:
# 
# **Sample** standard deviation:
# 
# $$s = \sqrt{\frac{1}{n-1}\sum_{i=1}(x_i - \bar{x})^2}$$
# 
# **Population** standard deviation:
# 
# $$\sigma = \sqrt{\frac{1}{n}\sum_{i=1}(x_i - \mu)^2}$$
# 
# where $\mu$ is the population mean and $\bar{x}$ is the sample mean.
# 
# The **sample variance** is the given by $s^2$, the **population variance** is the given by $\sigma^2$

# ### Implementation

# In[ ]:


def std(lst, dof=0):
    n = len(lst)
    mean = sum(lst)/n
    dev = sum([(x - mean)**2 for x in lst])
    return (1/(n - dof) * dev)**(1/2) 
    


# In[ ]:


std_pop = std(sales)
std_smpl = std(sales, dof=1)
std_pop, std_smpl


# Going forward we will use `numpy` for many of our calculations. 

# In[ ]:


np.std(sales), np.std(sales,ddof=1)


# ## $z$-Scores

# ### Definition

# Represents the number of standard deviation an observation is above or below the mean. 
# 
# The **$z$-score** for the $i_{th}$ observation of (sample) variable $x$ is defined as:
# 
# $$ \text{$z$-score of $x_i$}= \dfrac{x_i - \bar{x}}{s_x} $$
# 
# where $\bar{x}$ and $s_x$ are the mean and the standard devation of x, respectively.
# 
# The $z$-score standardizes a variable so its unit of measurement no longer matters. To this end, it is not sensitive to how the variable is scaled and/or shifted.
# 
# **Example**: if the $z$-score of a particular observation equals 2.5, the observation is 2.5 standard deviations above the mean. 
# 

# ### Implementation

# In[ ]:


sales = load_sales()
mean = np.mean(sales)
std = np.std(sales)
z_scores = (sales - mean) / std
z_scores


# In[ ]:


def zscore(lst):
    return (lst - np.mean(lst))/np.std(lst)


# In[ ]:


zscore(sales)


# # New Python concepts

# ## New functions

# list.`sort()`: 
# 
# - sorts a list in ascending order and can be applied to any list object. 
# - is an inplace method meaning the method doesn't return a new list, but sorts the existing list

# In[ ]:


names = ["Denise","Beatrix","Adam", "Zack"]
names.sort() # or names.sort(reverse=False)
names


# In[ ]:


names.sort(reverse=True)
names


# In[ ]:


get_ipython().run_line_magic('pinfo', 'list.sort')


# `float.is_integer()`:
# 
# - checks if a float (a number with digits) is a whole number (e.g. 3.0)
# - can only be applied to numbers with digits

# In[ ]:


number = 3.0
number.is_integer()


# In[ ]:


number = 5.9
number.is_integer()


# In[ ]:


number = 3
#number.is_integer() # Does not work as an integer object doesn't have a method "is_integer()"


# ## Comparison operators

# With these operators we can compare two variables. In Python you can use the following comparison operators
# 
# | Operator | Name                     |
# |:--------:|--------------------------|
# |    ==    | Equal                    |
# |    !=    | Not equal                |
# |     >    | Greater than             |
# |     <    | Less than                |
# |    >=    | Greater than or equal to |
# |    <=    | Less than or equal to    |
# 
# Comparison operators return `true` if comparison is true else they return `false`.
# 
# Let's look at some examples:

# In[ ]:


a = 10
b = 12
a > b


# In[ ]:


a != b


# In[ ]:


name1 = "Felix"
name2 = "Riza"
len(name1) < len(name2)


# In[ ]:


n1 = [1,2,3,4]
n2 = [4,3,2,1]
sum(n1) == sum(n2)


# ## If condition

# If statements are very useful as the run code depending on a test condition. 
# 
# So syntax in Python is as follows:
# 
# ```Python
# if condition:
#     do something
# ```
# 
# We can also write:
# 
# ```Python
# if condition:
#     do something
# else: 
#     do something differently
# ```
# 
# If we want to test more than one condition we can do this with the `elif` keyword
# 
# ```Python
# if condition1:
#     do something
# elif condition2: 
#     do something differently
# else:
#     do something by default
# ```
# 
# **Example**: let's write a function that tests if a number is big or not. Any number above $100$ is defined as big

# In[ ]:


def is_big(number):
    if number > 100:
        print(number, "is a big number")
    else: 
        print(number, "is a small number")


# In[ ]:


is_big(12)


# In[ ]:


is_big(101)


# ## Importing modules

# Most of the functionality we are using has been programmed and packaged into a specific module. We can access a module with the keyword `import`. After importing a module we can then use it and access the associated objects and methods.
# 
# ```Python
# import module_name
# 
# module_name.module_function()
# 
# ```
# 
# > **Note**: importing a module requires most modules to be downloaded and installed first. This will be explained in more detail in due course
# 
# **Example**: below we are importing the module`statistics` which provides basic functionality for statistical analysis.

# In[ ]:


import statistics


# Once the above cell is executed we can use the module. Here we are using the `mean` function from statistics

# In[ ]:


visitors = [80000, 75000, 78000,80500, 80140]
statistics.mean(visitors)


# **Example**: below we are importing `math` which provides basic math functionality

# In[ ]:


import math


# In[ ]:


math.pi # calculates pi


# In[ ]:


math.ceil(3.4) # rounds up


# **Example**: `numpy`

# Let's introduce one of the most important modules for data analysis: `numpy`. 
# 
# Numpy [see here](https://numpy.org/) is one of the most fundamental packages of python and provides a vast amount of functionality for scientific computing and is used by researchers throughout the world to facilitate there research (e.g. numpy played an important role in creating the first picture of a black hole; [see here](https://numpy.org/case-studies/blackhole-image/))
# 
# Many other fundamental modules are built on or rely heavily on numpy (e.g. most of the modules we will use during our course).  
# 
# For more background please also refer to the recently published paper in Nature ([paper](https://www.nature.com/articles/s41586-020-2649-2))

# In[ ]:


import numpy as np


# In[ ]:


numbers = [1,2,4,5,6]
np.sum(numbers)


# In[ ]:


np.percentile(numbers, q=85, interpolation="higher")


# We will gradually introduce some additional modules that are integral for doing data analysis in python. Some of the most important package we will learn about are:
# 
# - `pandas`: module for tabular data and dataframes
# - `matplotlib`: module for visualizations
# - `scipy`: module for scientific analysis
# - `sklearn`: module for machine learning
