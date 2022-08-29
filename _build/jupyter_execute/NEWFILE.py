#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# # Fallstudie: Investieren via Aktiensparplan

# Enden wollen wir das einleitende Kapitel mit einer Fallstudie. In dieser Fallstudie werden Dinge vorgegriffen, die Sie an dieser Stelle noch nicht zu 100% nachvollziehen können. Ziel der Fallstudie ist nicht, dass Sie jede Code-Zeile nachvollziehen können. Vielmehr sollen Sie einen Eindruck davon vermittelt bekommen, was Sie 

# - Daten
# - Aufbereitung
# - Berechnungen
# - Analyse
# - Visualisierung / Kommunikation

# In[15]:


from UtilityCode.utility import plot, load_stockdata
from datetime import datetime
import time
import pandas as pd
pd.options.plotting.backend = 'matplotlib'


# In[16]:


df = (load_stockdata(ticker="^GDAXI", frequency="1d", start="1-1-1990", end="7-18-2022")
      .filter(items=["Date","Adj Close"])
      .plot(x="Date", y="Adj Close")
      #.pipe(plot, 
      #      x="Date", 
      #      y="Adj Close", 
      #      title="DAX-Kurs\n(1990 bis heute)",
      #      xlabel="Datum")
     )
df


# In[7]:


df


# In[158]:


df.filter(items=["Date", "Adj Close"])


# In[103]:


print("https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1657670400&period2=1658102400&interval=1d&events=history&includeAdjustedClose=true")


# In[102]:


a = int(datetime.strptime("2021-7-18 15:24:00", "%Y-%m-%d %H:%M:%S").timestamp())
f"abc{a}&bcd"


# In[72]:


https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1657670400&period2=1658102400&interval=1d&events=history&includeAdjustedClose=true


# In[74]:


datetime


# In[67]:


pd.read_csv(url)


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


import pandas as pd


# In[28]:


url = "https://query1.finance.yahoo.com/v7/finance/download/EXS1.DE?period1=1199232000&period2=1657497600&interval=1d&events=history&includeAdjustedClose=true"

data = pd.read_csv(url, parse_dates=["Date"])


# In[29]:


plot(x="Date", y="Adj Close", data=data, title="Dies ist ein Test", kind=∫)


# In[20]:


type(data["Date"][0])


# In[17]:


plt.plot(data["Date"], data["Adj Close"])


# In[68]:


data1 = {"A": [1,2,3],
        "B": list("abc")}

data2 = {"A": [3,2,1],
        "B": list("cba")}

data = [data1, data2]
df = pd.concat((pd.DataFrame(d) for d in data))


# In[72]:


plot(x="B", y="A", data=df, 
     plot_type="scatter", 
     size=(3,2),
     title="Dies ist ein Test",
     ylabel="Important label",
     xlabel="X-Achse")


# In[49]:


data["Adj Close"].plot()


# In[76]:


from glob import glob
from pathlib import Path


# In[99]:


path = Path("../Data")
list(path.glob("*"))


# In[87]:


list(path.glob("*"))


# In[88]:


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR


# In[60]:


import numpy as np

class TestMe():
    def __init__(self, x):
        self.x = x
        self.context = locals()
        
    def __enter__(self, *args):
        print("Enter") 
        #self.context = globals()
        return self
    
    def __exit__(self, *args):
        self.context = locals()
        self.test = args


# In[61]:


import pprint


# In[62]:


t = TestMe(3)
with t as model2:
    data = np.array([1,2,3,4,5])
    strategy = lambda x: x * 2
    
t.context


# In[63]:


data


# In[89]:


import threading


# In[95]:


locals()


# In[7]:


import threading


# In[10]:


threading.local()


# In[11]:


dir()


# In[ ]:




