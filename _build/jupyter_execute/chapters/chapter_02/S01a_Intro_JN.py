#!/usr/bin/env python
# coding: utf-8

# # Einführung in Jupyter Notebooks

# What you are currently seeing (or using) is a **Jupyter Notebook**. This specific notebook is connected to a `python kernel` which can run and interpret python programming code.

# ## What are Jupyter Notebooks and do we use them?

# Jupyter Notebooks ([see here](https://jupyter.org/)) are an interactive programming environment within you can:
# 
# - run programming code 
# - visualize results and data
# - compose text (using markdown, html or latex)

# Jupyter Notebooks are extraordinary useful to combine 
# 
# 1. analysis of data
# 
# 2. description of conducted analyses
# 
# Project Jupyter started in 2014 and origins from the idea to make research papers reproducable and have significantly gained in popularity in the last years, particular in the **research community** ([see here](https://www.nature.com/articles/d41586-018-07196-1)) but also in **business** ([see here](https://netflixtechblog.com/notebook-innovation-591ee3221233)).
# 
# Jupyter Notebooks are especially useful for complex data analysis tasks as they enable exploratory analysis.

# ## How do Jupyter Notebooks work?

# Jupyter notebooks consist of `cells`. All content - including this text - exists within a cell. 
# 
# `Cells` can be distinguised in:
# 
# - text cells (i.e. Markdown)
# - code cells (in our case: Python)

# ### Text cells

# All previous cells consist of text written in `Markdown` (see [here](https://en.wikipedia.org/wiki/Markdown) and [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)). 
# 
# Markdown enables to compose easy to read text without hugh efforts of formatting or conversions. Markdown is used especially for webblogs. 
# 
# Using `Markdown` it is easy to include **pictures**
# 
# ![FH Bielefeld](https://www.dropbox.com/s/a4j2gj0bt47m3hv/FH_Bielefeld.png?dl=1)
# 
# Or **mathematical formulas** (using [latex](https://en.wikipedia.org/wiki/LaTeX))
# 
# $$f(x) = \sum_{t=1}^{T} \frac{CF_t}{(1+i)^t} + \sqrt{a^2 + b^2}$$
# 
# 

# ### Code cells

# In code cells you can write (python) programming code which is then executed just as any regular program.
# 
# The below cell is a python code cell. 
# 
# **Input** (a python expression): `3 + 3` (just a regular math operation in this case)
# 
# **Output**: result of the python expression
# 

# In[2]:


3 + 3 # This is a program!


# Some more examples:

# In[3]:


5 * 5


# In[ ]:


variable1 = 3
variable2 = 5

variable1 + variable2


# ### Creating of and switching between cell types

# Creating a new cell is done by pressing 
# 
# - `ESC` + `a` (create new cell above)
# - `ESC` + `b` (create new cell below)
# 
# Deleting a cell is done by pressing `ESC` + 2x `d` 
# 
# Turn cell into:
# 
# - markdown: `ESC` + `m`
# - code: `ESC` + `y`
# 
# 

# Alternatively one can use the `menu bar`:
# 
# 
# **Menü: Jupyter Notebooks**
# 
# 
# ![Menü_Jupyter](https://www.dropbox.com/s/968g9u2j0n7rnuh/Men%C3%BC.png?dl=1)
# 
# 
# 
# 
# 
# **Menü: Google Colab**
# 
# ![Menü Colab](https://www.dropbox.com/s/yclc5iggr6u5xq3/Men%C3%BC_Colab.png?dl=1)

# **Note**: shortcuts as well as menu bar in google colab may differ slightly. However, using google colab is fairly intuitive and self explanatory. Also, the shortcuts can be changed matching personal preferences using the menu bar.

# ### Executing cells

# All cells are executed pressing `shift` + `enter` or using the menu bar. 
# 
# When executing a code cell an **out** cell showing (i.e. printing) the result of the last line of the executed cell) is generated automatically. 

# In[ ]:


3 + 3

