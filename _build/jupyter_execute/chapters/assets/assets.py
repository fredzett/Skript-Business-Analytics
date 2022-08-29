#!/usr/bin/env python
# coding: utf-8

# # Generiert Graphiken für Skript

# In[335]:


import BusinessAnalytics as BA
from BusinessAnalytics import get_stock_data, plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# ## DAX 1988 - 2022

# In[336]:


dax = get_stock_data("^GDAXI", start="01-01-1987", end="31-07-2022")


# In[337]:


idx = np.argmax(dax["Adj Close"])
dax.iloc[idx]


# In[338]:


color = BA.plotting.COLORS[5]
ax = plot(data=dax, x="Date", y="Adj Close", 
     title="Entwicklung Dax\n(Dezember 1987 bis Juli 2022)", 
     ylabel="Kurs", xlabel="Jahr", show_legend=False,
     colors=color )

ax.xaxis.set_major_locator(mdates.YearLocator(3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.savefig("Dax.png", dpi=80)


# In[339]:


start = 898
ende = 3453
dax.iloc[[start, ende]]["Adj Close"].pct_change()


# 

# In[340]:


start = pd.to_datetime("12.04.2007")
ende = pd.to_datetime("19.12.2008")
dax.set_index("Date")[start:ende]["Adj Close"]

4696/7808 - 1


# ## 6 fiktive Portfolien

# In[341]:


days = np.arange(0,11)
rets = np.array([ 0.00, 0.02, 0.03, 0.04, -0.01, 	-0.02, 0.01, 0.02, 	-0.03, -0.05,0.10 ])
start = 100
index = start * np.cumprod((1+rets))
data = pd.DataFrame({"Kurs": np.round(index), "Periode": days, "rt":rets})
ax = plot(data, x="Periode", y="Kurs", 
          show_legend=False, colors=color, title="Kursentwicklung 'Index'")
ax.set_xticks(days[1:])
ax.set_xticklabels(days[1:])
plt.savefig("Index_Beispiel.png", dpi=80)


# In[342]:


def replace_first_row(_df, to_replace=np.nan, value=1):
    cols = _df.columns
    _df.iloc[0] = _df.iloc[0].replace(to_replace=to_replace, value=value)
    return _df


# In[343]:


data_new = (data
        .assign(**{f"Anlage_{i}":data["rt"].iloc[1:].add(1).shift(-i+1).cumprod() for i in np.arange(1,n)})
        .pipe(replace_first_row, np.nan, 1)
        #.melt(id_vars=["Periode", "Kurs", "rt"], var_name="Portfolio")
        )
data_new


# In[354]:


colors = BA.plotting.COLORS
ax = plot(data=data_new, x="Periode", y=[col for col in data_new.columns if "Anlage" in col], 
        colors=[colors[0], "lightgrey", "lightgrey", colors[4], "lightgrey", colors[3]], 
        show_legend=False, xlabel="Periode", ylabel="Wert", title="Wertentwicklung der 6 Anlagen über die Zeit")


xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()
ax.annotate("Anlage 1", (xmax-1, ymax), color=colors[0] )
ax.annotate("Anlage 4", (6.3, 0.92), color=colors[4] )
ax.annotate("Anlage 6", (3,0.93), color=colors[3])
plt.savefig("Anlagen_perf.png", dpi=80)


# In[524]:


bucket = rets[1:]
n = 100
t = 10
smpl = np.random.choice(bucket, (n,t), replace=True)


# In[527]:


smpl = np.column_stack((np.ones(n), np.cumprod(1+smpl, axis=1)))
np.row_stack((smpl, np.ones([1,t+3])))


# In[520]:





# In[507]:


idx_max = np.argmax(smpl[:,-1])
idx_min = np.argmin(smpl[:,-1])


# In[508]:


fig, ax = plt.subplots()
ax.plot(smpl.T, color="gray", linewidth=0.8, linestyle="dashed", alpha=0.6);
ax.plot(smpl[idx_max,:], color="green", alpha=0.4)
ax.plot(smpl[idx_min,:], color="red", alpha=0.4)


# In[509]:


probs = []
for i in np.arange(1,t):
    p = sum(smpl[:,i] < 1 ) / n
    probs.append(p)
plt.plot(probs)


# In[511]:


get_ipython().run_line_magic('pinfo', 'np.r_')


# In[484]:


plt.plot(probs)


# In[1]:


get_ipython().run_line_magic('history', '-g -f anyfilename')


# In[ ]:




