#!/usr/bin/env python
# coding: utf-8

# # Generiert Graphiken für Skript

# In[5]:


import BusinessAnalytics as BA
from BusinessAnalytics import get_stock_data, plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# ## DAX 1988 - 2022

# In[6]:


dax = get_stock_data("^GDAXI", start="01-01-1987", end="31-07-2022")


# In[7]:


idx = np.argmax(dax["Adj Close"])
dax.iloc[idx]


# In[8]:


color = BA.plotting.COLORS[5]
ax = plot(data=dax, x="Date", y="Adj Close", 
     title="Entwicklung Dax\n(Dezember 1987 bis Juli 2022)", 
     ylabel="Kurs", xlabel="Jahr", show_legend=False,
     colors=color )

ax.xaxis.set_major_locator(mdates.YearLocator(3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.savefig("Dax.png", dpi=80)


# In[9]:


start = 898
ende = 3453
dax.iloc[[start, ende]]["Adj Close"].pct_change()


# 

# In[10]:


start = pd.to_datetime("12.04.2007")
ende = pd.to_datetime("19.12.2008")
dax.set_index("Date")[start:ende]["Adj Close"]

4696/7808 - 1


# ## 6 fiktive Portfolien

# In[11]:


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


# In[12]:


def replace_first_row(_df, to_replace=np.nan, value=1):
    cols = _df.columns
    _df.iloc[0] = _df.iloc[0].replace(to_replace=to_replace, value=value)
    return _df


# In[18]:


t_min = 5
n = len(data) - t_min + 1
data_new = (data
        .assign(**{f"Anlage_{i}":data["rt"].iloc[1:].add(1).shift(-i+1).cumprod() for i in np.arange(1,n)})
        .pipe(replace_first_row, np.nan, 1)
        #.melt(id_vars=["Periode", "Kurs", "rt"], var_name="Portfolio")
        )
data_new


# In[19]:


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


# In[150]:


sum(data.query("Periode == 6")["Wert"] < 1)


# ## 10 zufällige Portfolios

# In[22]:


def sample_data(data, n, t, replace=True):
    return np.random.choice(data, (n,t), replace=replace)


# In[145]:


np.random.seed(123545)
n = 10
t = 10
smpl = sample_data(rets[1:], n, t)
cum_rets = np.column_stack((np.ones(n), np.cumprod(1+smpl, axis=1)))


# In[146]:


data = (pd.DataFrame(cum_rets.T, columns=[f"Anlage_{i}" for i in range(1,n+1)])
        .assign(Periode=np.arange(t+1))
        .melt(id_vars=["Periode"])
        .rename({"variable":"Anlage", "value":"Wert"}, axis=1)
        )
ax = plot(data=data, x="Periode", y="Wert", hue="Anlage", 
     title="Mögliche Wertentwicklung bei Anlage in Beispiel-Index\n(Bei Anlagezeitraum von 10 Perioden)",
     colors=["gray" for i in range(n)], 
     show_legend=False)

idx_max = np.argmax(cum_rets[:,-1])
idx_min = np.argmin(cum_rets[:,-1])

for i,l in enumerate(ax.lines):
    l.set_alpha(0.4)
    if i == idx_max: l.set_color("green")
    if i == idx_min: l.set_color("red")

ymin, ymax = ax.get_ylim()

ret_max = np.round((cum_rets[idx_max, -1] - 1)*100,2)
ax.annotate(f"+{ret_max}%", (10,ymax*0.98), color="green", alpha=0.6)
ret_min = np.round((cum_rets[idx_min, -1] - 1)*100,2)
ax.annotate(f"-{abs(ret_min)}%", (10,ymin*1.02), color="red", alpha=0.6)
plt.savefig("Anlagen_random.png", dpi=80)


# ## 1.000 zufällige Portfolien

# In[105]:


np.random.seed(123545)
n = 1000
t = 10
smpl = sample_data(rets[1:], n, t)
cum_rets = np.column_stack((np.ones(n), np.cumprod(1+smpl, axis=1)))
data = (pd.DataFrame(cum_rets.T, columns=[f"Anlage_{i}" for i in range(1,n+1)])
        .assign(Periode=np.arange(t+1))
        .melt(id_vars=["Periode"])
        .rename({"variable":"Anlage", "value":"Wert"}, axis=1)
        )
ax = plot(data=data, x="Periode", y="Wert", hue="Anlage", 
     title="Mögliche Wertentwicklung bei Anlage in Beispiel-Index\n(Bei Anlagezeitraum von 10 Perioden)",
     colors=["gray" for i in range(n)], 
     show_legend=False)

idx_max = np.argmax(cum_rets[:,-1])
idx_min = np.argmin(cum_rets[:,-1])

for i,l in enumerate(ax.lines):
    l.set_alpha(0.1)
    if i == idx_max: l.set_color("green")
    if i == idx_min: l.set_color("red")

ymin, ymax = ax.get_ylim()

ret_max = np.round((cum_rets[idx_max, -1] - 1)*100,2)
ax.annotate(f"+{ret_max}%", (10,ymax*0.98), color="green", alpha=0.6)
ret_min = np.round((cum_rets[idx_min, -1] - 1)*100,2)
ax.annotate(f"-{abs(ret_min)}%", (10,ymin*1.02), color="red", alpha=0.6)
plt.savefig("Anlagen_random_big.png", dpi=80)


# In[144]:


import seaborn as sns
data_hist = (data
             .query("Periode == 6")
             .assign(Wert=lambda _df: _df["Wert"] - 1)
            )
mu = data_hist["Wert"].mean()
ax = sns.histplot(data=data_hist, x="Wert", color="red", alpha=0.1, kde=True)
ymin, ymax = ax.get_ylim()
ax.lines[0].set_color("red")
ax.vlines(x=mu,color="black", linewidth=3, ymin=ymin, ymax=ymax)
ax.annotate(f"arithm. Mittel: {np.round(mu,2)}", (mu*1.1,ymax), **{"fontsize": 10});


# In[ ]:



ax = plot(data=data_hist, x="Wert", plot_type="hist", 
     ylabel="Häufigkeit", 
     xlabel="Rendite in ct",
     show_legend=False)
ax.set_alpha(0.4)


# In[27]:


fig, ax = plt.subplots()
ax.plot(cum_rets.T, color="gray", linewidth=0.8, alpha=0.6);
ax.plot(cum_rets[idx_max,:], color="green", alpha=0.4)
ax.plot(cum_rets[idx_min,:], color="red", alpha=0.4)


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


# In[1]:


1 * (1.01) * (0.95) * 0.95


# In[ ]:




