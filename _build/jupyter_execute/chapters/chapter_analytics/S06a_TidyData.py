#!/usr/bin/env python
# coding: utf-8

# # Tidy Data

# In[475]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from patsy import dmatrices


# # Introduction

# So far we have been mostly using the following modules:
# 
# - `scipy`: for probabilties and simulations
# - `numpy`: for numerical operations
# - `matplotlib`: for plotting (note: partly disguised by helper functions provided for this class (e.g. `plot_line`) which abstract away use of matplotlib)
# 
# We have only recently introduced `pandas` as a new module to work with dataframes. When referring to dataframes we mean data objects similar to an **excel sheet** where we would typically have:
# 
# - header describing the column data
# - each column data could be of different types (numeric, qualtiative, text etc.)
# - each row is labelled
# 
# **Dataframes helpful for reserach**  
# Working with dataframes is helpful in quantitative research as our data typically doesn't fully consist of numerical data and we also want to give our variables explanatory names. 
# 
# **Organization of data is important**  
# Quantitative research involves many steps. The data analysis part involves e.g.: 
# 
# - generating data: e.g. via survey, web scraping, gathering from different sources etc.
# 
# - preprocessing data: i.e. preparing the data for analysis; e.g. cleaning the data, filtering data, rearranging data, combining data sets etc.
# 
# - exploring data: plotting raw data, calculating descriptive statistics etc.
# 
# - analyzing data: e.g. running a regression analysis
# 
# - presenting data: e.g. plotting data or creating summary tables
# 
# Most university courses focus on the generation and analysis part of the data analysis part. Up unitl now this was also our focus (and will continue to be). However, in practical research one of the most **time consuming** steps is the **preprocessing** step. Some [authors](https://www.wiley.com/en-us/Exploratory+Data+Mining+and+Data+Cleaning-p-9780471268512) claim that this part of the data analysis pipeline takes up about $80$% of the work. 
# 
# 
# To this end, the this lecture has two purposes:
# 
# 1. explain how to work with `pandas`
# 
# 2. explain how to set up a dataframe best suited for quantitative analysis and statistics
# 
# Both shall help you to be able to prepare data for your research. 

# # Pandas

# Before we want to understand how to best set up a dataframe to serve your research / analysis purposes, let's have a look at the `pandas` module in detail. 

# In[7]:


import pandas as pd # import pandas module and use it by prefix "pd"


# ## Creating pandas dataframes

# We can create pandas dataframes in two basic fashions:
# 
# 1. from scratch using other datatypes
# 
# 2. from reading in a file 

# **Creating dataframe from scratch using numpy**

# In[10]:


data = np.array(((1,2,3),(1,2,4),(35,7,3)))
data


# In[11]:


pd.DataFrame(data)


# We can also give both index and columns specific names

# In[17]:


df = pd.DataFrame(data, index=("a","b","c"), columns=("H1","H2","H3"))
df # a common general name for a variable holding a dataframe is "df"


# **Creating dataframe from scratch using dictionaries**

# In[18]:


data = {"H1":[1,2,3], "H2":["A","B","C"]}
df = pd.DataFrame(data)
df


# **Index and columns names**

# We can access both index and columns using

# In[28]:


df.index


# In[29]:


df.index = ["A","B","C"]


# In[30]:


df


# In[31]:


df.columns


# In[32]:


df.columns = ["New1", "New2"]
df


# **Creating dataframe from files**

# In research it is common that we have data and need to load it into a dataframe. This can be easily done using the 
# 
# - `pd.read_` commmand
# 
# which gives you a range of file types that you can read from
# 
# ![pd.read](https://www.dropbox.com/s/4zx16ag09vcjt6t/pdread.png?dl=1)
# 
# Let's look at an example and read in the file `Auto.csv` which is in the folder `data` which is located in the same folder as this notebook.

# In[81]:


fpath = "./data/Auto.csv"
df = pd.read_csv(fpath)
df


# All `pd.read_` functions provide a wide variety of loading options. 

# In[41]:


#pd.read_csv? # see load in options


# For example I could read in the same file with only a specific set of columns (columns 2 and 6). 

# In[46]:


pd.read_csv(fpath, usecols=[2,6])


# ## Data selection

# There are several ways how to work with data stored in dataframes. Note that one way is to convert the data into numpy arrays and work with them the usual way. This has the advantage of working with data objects we already are familar with. It has the disadvantage that we loose some information (such as header) and functionality (e.g. it is much harder to work with non-numerical data). 

# In[75]:


df.head() # .head() shows first 5 rows of data (note that .tail() shows last five rows


# In[76]:


df_numpy = df.values # .values extracts the numpy data underneath the dataframe


# In[77]:


df_numpy[:5]


# 

# **Selecting columns**
# 
# Let's continue and work with the dataframes directly

# In[78]:


df["mpg"] # selecting one column


# In[79]:


df[["mpg", "year"]] # selecting two columns


# In[84]:


# adding a new column by selecting two columns and applying calculation
df["horsepower_per_lbs"] = df["horsepower"] / df["weight"]
df.head()


# **Selecting columns using `loc` and `iloc`**

# Commonly we want to select subsets of a dataframe (i.e. we want to select rows and columns). This can be done via 
# 
# - `iloc`: selecting as it we were working with numpy array (i.e. use numerical indexing)
# - `loc`: selecting using explicit index and/or column names

# In[85]:


df.head()


# Using `iloc` indexer

# In[87]:


df.iloc[1:4,2:6] # selecting subset consisting of row 1 to row 3 and columns 2 to columns 5


# In[89]:


df.iloc[:,3:7]


# In[93]:


df.iloc[[2,4,5,70],[5,7,4]]


# Using `loc` indexer

# In[103]:


df.loc[:, ["cylinders", "year", "origin"]]


# In[104]:


df.loc[1:12, "cylinders":"weight"]


# **Using more sophisticated indexing**

# In[105]:


df.head()


# In[114]:


df.loc[df["horsepower"]>120, ["horsepower", "year", "weight"]] # for columns horsepower, year and weight, select all rows where horespower > 120


# ## Operations on dataframes

# Pandas is designed to work with numpy which means that most numpy functions work on pandas

# In[121]:


# take the natural logarithm of "mpg"
np.log(df["mpg"])


# You can also conduct regular operations on dataframes. Example:

# In[127]:


random_calc = (4 * df["mpg"]) / (df["acceleration"] + df["origin"])
random_calc


# Columns and row wise operations

# In[133]:


# Create random dataframe
rnd_data = np.random.randint(1,100, (10,5))
df_rnd = pd.DataFrame(rnd_data,columns=list("abcde"))
df_rnd


# Add row 8 from all other rows

# In[137]:


df_rnd + df_rnd.loc[8,:]


# Substract column "b" from all columns

# In[136]:


df_rnd.subtract(df_rnd["b"], axis=0)


# ## Aggregating data

# We can also - as with numpy arrays - aggregate data using pandas.

# In[222]:


df_rnd


# In[224]:


df_rnd.mean() # take mean over each column


# In[225]:


df_rnd.mean(axis=1) # taken mean over each row


# In[230]:


df_rnd[df_rnd["a"]>50].sum() # take sum over each column only taking rows into account where column a > 50


# ## Handling missing data

# In real life you will have to handle missing data (in python called `nan`, i.e. not a number). It is important to be able to deal with missing data, e.g.
# 
# - filter out all observation where certain variable data is missing (e.g. in a survey people didn't answer certain questions)
# 
# - specify how to deal with missing data when calculating descriptive statistics (e.g. the mean)
# 
# Let's look at how to deal with missing data

# In[164]:


data = np.array(((1,np.nan, 3,4), (5,6,np.nan, np.nan), (8, 9, 10, np.nan), (12,13,14,15))).T
df = pd.DataFrame(data, columns=list("abcd"))
df


# **Determine nans**

# In[165]:


df.isnull() # True if nan, False if not nan


# In[166]:


df.notnull() # True if not nan, False if nan


# **Filtering out nans**

# In[167]:


df.dropna() # drop all rows that contain nans (equal to df.dropna(axis=0))


# In[168]:


df.dropna(axis=1) # drop all columns that contain nans


# In[170]:


df.dropna(subset=["a", "c"]) # drow all rows that contain nans in columns "a" and/or "b"


# In[180]:


df.dropna(thresh=3) # drop all rows that have less than 3 non-nan values


# In[183]:


df.dropna(thresh=4, axis=1) # drop all columns that have less than 4 non-nan values


# **Filling nan values**

# In practice you don't always have to drop missing data points but could instead impute values for these missing data points. 
# 
# For example in stock market data you may have missing data for certain days (out of many days) because the data provider was experiencing a technical issue. In that specific case it may be perfectly reasonable to fill the missing data using some sort of data imputation technique. 

# In[192]:


# Create random stock data
stock1 = np.random.random(10)
stock2 = np.random.random(10)
df = pd.DataFrame({"Stock1": stock1, "Stock2":stock2})
df.iloc[3,0] = np.nan
df.iloc[6,1] = np.nan
df.index = pd.date_range(start="01/01/2020", periods=len(stock1))
df


# In[202]:


# replace with previous value
df.fillna(method="ffill") 


# In[214]:


# replace with next value
df.fillna(method="bfill") 


# In[212]:


# replace with specific value
df.fillna(value=0) # replace by zero


# In[213]:


# replace with specific value using a function
df.fillna(value=df.min()) # replace with minimum value of each stock


# ## Grouping data

# When doing quantitative analysis and statistics we are frequently applying calculations on filter and aggregations on data. 

# Let's look at a simple example dataframe: in the below dataframe we may be interested in the sum of data per key.

# In[260]:


data = {"key":list("abcabc"), "data":range(1,7)}
df = pd.DataFrame(data)
df


# This could be calculated easily with what we have seen before. We could simply apply three filters

# In[263]:


s1 = df.loc[df["key"]=="a","data"].sum()
s2 = df.loc[df["key"]=="b","data"].sum()
s3 = df.loc[df["key"]=="c","data"].sum()
s1, s2, s3


# This is tedious (although we could have made the code less repetitive and verbose using a for-loop) and sometimes not practical.
# 
# A very powerful feature of pandas is the **groupby** operation / concept which we will introduce in the following

# In[266]:


df.groupby("key")["data"].sum()


# The way this function works is illustrated in the following figure
# 
# ![groupby](https://www.dropbox.com/s/rpg9grsod2dhrh1/pdgroupby.png?dl=1)
# 
# (note: the example is taken from [Jake VanderPlas' book](https://github.com/jakevdp/PythonDataScienceHandbook)

# The "split-apply-combine" mechanic can be very helpful when grouping and aggregating data. 
# 
# Let's take our `car dataset` and apply some more methods. For example let's say we want to understand if 
# 
# - mean `mpg` differs 
# - when conditioned on 
# - origin and number of cylinders

# In[332]:


df = pd.read_csv(fpath)
df.tail()


# In[295]:


mpg_conditioned = df.groupby(["origin", "cylinders"])["mpg"].mean()
mpg_conditioned


# We can use the *as_index=False* statement to return a dataframe

# In[277]:


mpg_conditioned = df.groupby(["origin", "cylinders"],as_index=False)["mpg"].mean()


# We can use the groupby method to quickly explore our dataset when combining with other methods. Most importantly
# 
# - aggregate
# - transform
# 

# **Groupby and aggregate**

# In[300]:


df.groupby("origin").aggregate([np.mean, np.std]) # group by origin and calculate mean and standard deviation


# In[302]:


df.groupby("origin").aggregate({"mpg":np.mean, 
                                "horsepower":max})


# **Groupby and transform**

# In[328]:


def df_plus_mean(dframe):
    return dframe + dframe.mean()


# In[333]:


df.groupby("origin").transform(df_plus_mean).tail() # add mean per column per groupy to columns


# In[335]:


df[df["origin"]==1]["mpg"].mean() # mean of 20.033 is added for mpg in first row, because it is origin == 1


# ## Plotting data

# Pandas dataframes can be plotted quite easily

# In[337]:


df["mpg"].plot(kind="line")


# In[347]:


df.groupby("origin")["horsepower"].mean().plot(kind="bar", title="Mean horsepower by origin");


# In[363]:


df.groupby("origin")["horsepower"].plot(kind="kde", title="Distribution of horsepower by origin", legend=True);


# ## Pivot tables

# Pivot tables work similar to excel pivot tables and are helpful for more complex conditional filtering

# In[367]:


df = pd.read_csv(fpath)
df.head()


# Let's say we want to calculate average weight conditioned by number of cylinders and origin

# In[372]:


df.pivot_table(values="weight",index="cylinders", columns="origin",aggfunc=np.mean)


# ## Complex filtering

# Sometimes we want to apply multiple filter. Here `query` can be handy.

# In[376]:


# Standard option
df.loc[(df["cylinders"]==6) & (df["year"]==78)]


# In[377]:


# Option using query function
df.query("cylinders==6 & year == 78")


# # Tidy data

# Please refer to the great article by Hadley Wickham [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf) for a detailed discussion on tidy data.
# 
# According to Wickham, **tidy data** is a standard way of mapping the meaning of a dataset to its structure. A dataset is messy or tidy depending on how rows, columns and tables are matched up with observations, variables and types. 
# 
# In tidy data:
# 
# 1. each variable forms a column
# 
# 2. each observation forms a unit
# 
# 3. each type of observational unit forms a table 

# Why is this important: because when a dataframe is not tidy it is much harder to analyse and explore the data. 
# 
# **Example** (from Wickham)
# 
# There are different ways how to structure data

# In[441]:


data = {"Name":("John","Jane","Mary"),"Treatment_A":(np.nan, 16,3), "Treatment_B": (2,1,1)}
df = pd.DataFrame(data)
df


# Option 1

# In[436]:


df1 = df.set_index("Name")
df1.index.name = " "
df1


# Option 2

# In[437]:


df2 = df1.T
df2.columns.name = ""
df2


# Option 3

# In[448]:


pd.melt(df, id_vars="Name", var_name="treatment", value_name="treatment_result")


# When doing quantitative or statistical analysis you would typically want to conduct analysis on the two variables "treatment" and "treatment_result" which is why the third option is much more helpful when conducting analysis and is considered to be **tidy**:
# 
# - each variable forms a column: we have three variables name, treatment and treatment result
# - each observation forms a row: we have 6 observations for 3 persons two treatments
# - (number 3: not relevant)

# The following examples are taken from [Daniel Chen](https://github.com/chendaniely/pydatadc_2018-tidy/tree/master/data)

# **Example using a bigger data set**

# In[462]:


df = pd.read_csv("./data/pew.csv", sep=";")
df


# The table may be useful for presentation purposes and may be data efficient. But it is not tidy.
# 
# Why is it not tidy?
# 
# A good proxy to find out if the data is stored in a tidy format is to think about a model you want to build (e.g. a regression model) and aks yourself what possible variables for your models would be. 
# 
# In the above case it is unlikely that we would want to treat "<$10k" as a variable. Instead we would likely want to use "income type" as a variable. So the data set actually consists of three variables:
# 
# - religion
# - income
# - count (number of people)
# 
# With the data structure above we are not able to analyze the data effiently. 
# 
# For example: the following analysis would already be quite tedious:
# 
# - calculate sum of counts per religion
# 
# - run a model on different variables
# 
# The format the above table is also called **wide format**.
# 
# In order to make it tidy we need to put it into a **long format** using `pd.melt`

# In[499]:


df_tidy = df.melt(id_vars="religion", var_name="income", value_name="count")
df_tidy


# We can now already answer the first question really easy

# In[501]:


df_tidy.groupby("religion")["count"].sum()


# Although this would also be achievable using the wide format it is (i) much verbose and (ii) also would need change of code if a new income category was introduced

# **More complex example**

# Let's look at case and death number from an ebola pandemic in 2014/2015. 

# In[704]:


df = pd.read_csv("https://raw.githubusercontent.com/chendaniely/pydatadc_2018-tidy/master/data/country_timeseries.csv")


# In[705]:


df.head()


# The data is not really well structured for analysis given cases and death for each country is organized as columns. However, typically we would ask questions such as:
# 
# - what is number of death per country
# - what is average case increase per country 
# - etc.
# 
# Clearly the data is not tidy as we have the following variables in the data set:
# 
# - date
# - day
# - indicator (case or death)
# - country

# It would be very difficult to calculate simple statistics such as aggregate deaths by country.

# Let's make the dataframe tidy to be able to do these kind of calculations.

# In[706]:


df = df.melt(id_vars=["Date","Day"])
df.head()


# We are almost there. We only need to look more carefully at column "variable".

# In[707]:


df[["type", "country"]] = df["variable"].str.split("_",expand=True) # split column "variables" by "_" and store it in two columns
df.head()


# In[708]:


df  = df.drop(labels="variable", axis=1) # drop columns "variable" which is not needed anymore
df = df.dropna() # drop nans


# In[709]:


df.groupby(["country"])["value"].sum()

