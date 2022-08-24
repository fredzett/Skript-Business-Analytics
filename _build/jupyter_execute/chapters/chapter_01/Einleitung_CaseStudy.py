#!/usr/bin/env python
# coding: utf-8

# In[8]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')


# Wir beenden dieses Kapitel mit einer Fallstudie. Ziel dieser Fallstudie ist es, darzustellen, wie Sie mit relativ wenig Programmierung detaillierte Analysen durchführen können. In dieser Fallstudie werden Dinge vorgegriffen, die Sie an dieser Stelle noch nicht zu 100% nachvollziehen können. Ziel der Fallstudie ist nicht, dass Sie jede Code-Zeile nachvollziehen können. Vielmehr sollen Sie einen Eindruck davon vermittelt bekommen, was Sie in diesem Kurs erwartet bzw. was Sie - vorausgesetzt Sie arbeiten kontinuierlich mit - am Ende in der Lage sind selber umzusetzen. 
# 
# Gehen Sie diese Fallstudie also nicht mit dem Anspruch durch, alles bereits verstehen und selber umsetzen zu müssen. Vielmehr sollten Sie die übergeordnete Fragestellung durchdenken, um dann zu sehen, wie diese Fragestellung mittels Python beantwortet wird. 

# 
# ```{Warning}
# Dies ist eine Warnung!
# ```

# In[1]:


```{sidebar} Merke!
My sidebar content
```


# # Fallstudie: Investieren in ETFs

# Sie haben ihr Studium beendet und gelten in ihrer Familie nun als Expert*in für finanzielle Fragestellungen. Ihr Onkel, der überraschend einen größeren Geldbetrag geerbt hat, kommt auf Sie zu und fragt Sie, wie er das Geld sinnvoll anlegen könne. Sie raten Ihm dazu das Geld in einen breiten Aktienindex (passiv) zu investieren. Ihr Onkel winkt direkt ab, weil ihm Aktien "viel zu riskant" seien. Da könne man ja auch sehr viel Geld bei verlieren. 
# 
# Einerseits wollen Sie ihrem Onkel nicht raten das Geld in Immobilien oder in Festgeld zu investieren. Anderseits kommen Sie selber ins Grübeln, ob eine Investition in Aktien nicht vielleicht doch zu riskant ist. Sie beschließen deshalb der Frage empirisch nachzugehen. 
# 
# Konkret wollen Sie versuchen zu analysieren, wie riskant eine Investition in Aktien tatsächlich ist. 

# ## Risiko: Investition in DAX 40

# Obgleich es sich bei unserer Fragestellung um eine "persönliche" Analyse handelt, steht diese doch stellvertretend für ein typisches **Business Analytics**-Problem, bei dem es darum geht eine konkrete Fragestellung datenbasiert zu beantworten. 
# 
# Für unsere Analyse bedarf es daher:
# 
# 1. Fragestellung, die konkret bzw. "operationalisierbar" ist
# 
# 2. Daten, die wir zur Beantwortung der Frage nutzen können. 
# 
# Die bisherige Fragestellung ist noch zu unkonkret. Was bedeutet "riskant" bzw. "Risiko"? In welche Aktien wollen wir investieren?
# 
# Aus Vereinfachungsgründen definieren wir **Risiko** in unserem Fall als die **Wahrscheinlichkeit einen Verlust zu erleiden**. Wir fragen uns also konkret: wie wahrscheinlich ist es, dass ihre Investition innerhalb der nächsten Jahre weniger Geld wert ist, als Sie eingezahlt haben. Wir nehmen an, dass wir in den DAX 40 investieren wollen. 
# 
# Die konkrete Fragestellung lautet also: wie Wahrscheinlich ist es, dass wir in den DAX 40 investieren und dabei einen Verlust erleiden. 
# 
# Die Frage ist natürlich nicht sicher bzw. eindeutig zu beantworten. Wir bräuchten dafür die DAX-Stände der nächsten Jahren; wir müssten also die Zukunft vorhersehen. Wir haben die "perfekten" Daten nicht.  Stattdessen können wir jedoch historische Daten nehmen und schauen, wie eine Investition in den DAX in der Vergangenheit verlaufen wäre und wie hoch die Wahrscheinlichkeit eines Verlustes war. Wir könnten z.B. analysieren, was wäre passiert, wenn wir vor 7 Jahren 10.000 EUR in den DAX investiert hätten. Was wäre nach einem, nach zwei, usw. Jahren mit unserer Investition passiert. 

# Für die konkrete Analyse werden wir nur die folgenden Schritte durchlaufen:

# 1. Daten einsammeln und einlesen
# 
# 
# 2. Daten aufbereiten und transformieren: d.h. die Daten für die Analyse in eine geeignete Form und Qualität bringen
# 
# 
# 3. Daten analysieren: d.h. die Daten hinsichtlich der Fragestellung untersuchen 
# 
# 
# 4. Daten präsentieren: d.h. die Daten sinnvoll visualisieren und kommunizieren

# 

# ### 1. Daten einsammeln und einlesen
# 
# Aktienkursdaten sind - zumindest für unsere Zwecke - einfach und kostenlos zugänglich. Wir werden als Quelle [Yahoo Finance](https://de.finance.yahoo.com/quote/%5EGDAXI?p=%5EGDAXI&.tsrc=fin-srch) nutzen. 
# 
# Zum Einsammeln der Daten gibt es zwei Wege: 
# 
# 1. Manuell
# 
# 2. via Programmierschnittstelle
# 
# Manuell können wir die Daten herunterladen und als CSV-Datei speichern (siehe unten). 
# 
# ![](../assets/Yahoo_download.gif)
# <break></break>
# 
# Der manuelle Download ist einfach. Vorteilhafter ist es aber, den Download via eine Programmierschnittstelle vorzunehmen. In unserem Falle bedeutet dies, dass wir die Daten direkt via Python downloaden. 
# 
# Um dies zu erreichen gibt es viele Wege. Hier ist ein Weg der im Rahmen dieses Kurses genutzt werden kann. 
# 
# Der untenstehende Programmcode importiert eine Funktion `load_stockdata`, die es ermöglicht unter Angabe des Aktientickers (hier: ^GDAXI für Dax) und weiterer Parameter, wie z.B. den Start- und Endzeitpunkt, die Daten von Yahoo-Finance herunterzuladen. 
# 
# Bit

# In[5]:


from utility import load_stockdata


dax_data = load_stockdata(ticker="^GDAXI", frequency="1d", start="1-1-1980", end="7-31-2022")
dax_data


# In[2]:


from utility import plot, load_stockdata
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




