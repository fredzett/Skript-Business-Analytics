#!/usr/bin/env python
# coding: utf-8

# # Module nutzen

# Bislang haben wir einige Grundlagen in Python kennengelernt. Wie wissen, was Listen sind, wie eigene Funktionen geschrieben werden etc. 
# 
# Grundsätzlich könnten wir also mit der Datenanalyse anfangen. Jedoch müssten wir jegliche Funktionalität (z.B. CSV-Dateien einlesen, Graphen plotten etc.) selber von Grund auf programmieren. 
# 
# Dies ist aber natürlich nicht notwendig, da Python sich eine großen Community erfreut und viele der **benötigten Funktionalitäten bereits von anderen programmiert** wurden. Um diese Funktionalitäten nutzen zu können (Hinweis: Python ist Open Source, d.h. der Source Code ist grundsätzlich frei zugänglich) müssen wir spezifische Module importieren. 
# 
# 

# ## Module importieren

# Dies ist in Python ziemlich einfach und wird durch den `import` Befehl erreicht.
# 
# **Ein anschauliches Beispiel:** wir möchten den Sinus der Zahl 0.5 berechnen, jedoch ist diese Funktion bei den 70 buildin Funktionen nicht enthalten. Wir können also ganz einfach das Modul `math` importieren und aus diesem Modul die Funktion `sin` nutzen. 

# ### Importieren des gesamten Moduls

# In[ ]:


import math


# In[ ]:


x = 0.5
math.sin(0.5)


# ### Importieren einzelner Funktionen oder Klassen eines Moduls

# In[ ]:


from math import sin


# In[ ]:


sin(x)


# ### Importieren und umbenennen des Moduls

# In[ ]:


import math as m


# In[ ]:


m.sin(x)


# Anmerkung: für viele Module hat sich ein de facto Standard für die Umbenennung herausgebilded. 
# 
# So werden die für uns so wichtigen Module `pandas`, `numpy` und `matplotlib` von den meisten Python-Programmieren wiefolgt importiert:
# 
# ```
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# ```

# ## Wichtige Module für die Datenanalyse

# Python hat tausende von Modulen. Für nahezu jedes Problem gibt es bereits eine Lösung. Dies gilt natürlich auch für die Datenanalyse. 

# ### [Numpy](http://www.numpy.org/)

# Numpy ist eines der wichtigsten Module in Python. Es ermöglicht schnelle (weil meist vektorisierte) Berechnungen mit Vektoren und Matrizen. Dies ist sehr hilfreich, selbst wenn man sich nicht mit Linearer Algebra beschäftigen muss oder möchte. Jede Tabelle mit Daten kann als Matrix angesehen werden (man stelle sich bspw. eine Exceltabelle vor). 
# 
# Es gibt unzählige Tutorials und Supportseiten für die Bibliothek numpy. Zwei sehr gute Tutorials finden Sie hier:
# 
# - kurze Einführung auf deutsch: [Link](https://www.grund-wissen.de/informatik/python/scipy/numpy.html)
# 
# - ausführliches Tutorial auf englisch: [Link](https://stackabuse.com/numpy-tutorial-a-simple-example-based-guide/)

# Im folgenden seien die Vorteiel von `numpy` und einer vektorisierten Form der Berechnung gegenüber einer Berechnung mit For-Schleifen dargestellt. 
# 
# **Aufgabe:** addiere die Elemente zweier (gleich großer) Vektoren. 

# In[5]:


vector1 = [1,2,3,4]
vector2 = [5,6,7,8]

vector1 + vector2 # das ist nicht was wir wollen. 


# In[6]:


[a + b for a,b in zip(vector1,vector2)]


# **Elementweise Addition mit For-Schleife**

# In[ ]:


neuer_vector = []
for x,y in zip(vector1,vector2):
    neuer_vector.append(x+y)
neuer_vector


# **Besser: mit List Comprehension**

# In[ ]:


[x+y for x,y in zip(vector1,vector2)]


# **Noch besser: mit Numpy**

# In[7]:


import numpy as np


# In[8]:


arr1 = np.array(vector1)
arr2 = np.array(vector2)

arr1 + arr2


# Die Variante via Numpy ist nicht nur syntaktisch bedeutend einfacher, sondern bei großen Datenmengen auch um ein Vielfaches schneller. Mit Numpy können so ohne Probleme Millionen von Werten errechnet, transformiert etc. werden. 

# ### [Pandas](https://pandas.pydata.org/)

# Pandas baut auf numpy auf, d.h. nutzt die Funktionalität von numpy und dient insbesondere der Datenanalyse. Mithilfe von Pandas können z.B. Exceldateien sehr einfach eingelesen, angezeigt und manipuliert werden.
# 
# Sehr gute Tutorials zu Pandas finden Sie z.B hier:
# 
# - ein einführendes deutsches Tutorial: [Link](https://www.statworx.com/de/blog/data-science-in-python-pandas-teil-3/)
# 
# - ein sehr ausführliches englisches Tutorial: [Link](https://bitbucket.org/hrojas/learn-pandas)
# 
# Hier ein kurzes Beispiel: Einlesen einer Excel-Datei und Berechnung des durchschnittlichen Umsatzes je Region

# In[11]:


import pandas as pd


# In[12]:


# Nutzen Sie diese Zelle in GoogleColab
#!wget -O "MyData.xlsx" "https://www.dropbox.com/s/csjk3w6hraitb86/MyData.xlsx?dl=0"
#fpath = "MyData.xlsx"


# In[12]:


# Nutzen Sie diese Zelle in MyBinder 
fpath = "data/MyData.xlsx"    


# In[13]:


get_ipython().run_line_magic('pinfo2', 'pd.read_csv')


# In[14]:


df = pd.read_excel(fpath)


# In[15]:


df.head() # Ersten 5 Zeilen des Datensatzes


# In[16]:


df.tail() # Letzten 5 Zeilen des Datensatzes


# In[ ]:


df.shape # Datensatz hat 260 Zeilen und 3 Spalten


# In[ ]:


# Durchschnittlicher Umsatz je Region
mean_per_region = df.groupby("Region").agg({"Umsatz":[np.mean]})
mean_per_region


# ### Matplotlib

# Der große Vorteil von Jupyter Notebooks und einer der Hauptgründe für den großen Erfolg ist die Möglichkeit neben Text und ausführbarem Code auch Graphiken darzustellen. Um dies zu tun benötigen Sie natürlich ein Modul zum Erstellen von Charts (es sei denn, Sie wollen diese Funktionalität von Grund auf selber implementieren). 
# 
# Es gibt unzählige Visualisierungs-Module. Das wohl beliebteste und in Summe vielseitigste ist `matplotlib`.   
# 
# Für eine gute Einführung in Matplotlib ist die offizielle Dokumentation recht hilfreich ([hier](https://matplotlib.org/users/index.html)). 
# 
# Andere gute Bibliotheken, auf die an dieser Stelle nicht weiter eingegangen werden soll, sind z.B.:
# 
# - die deklarative Visualisierungsbibliothek [Altair](https://altair-viz.github.io/)
# 
# - die webfähige Bibliothek [Plotly](https://plot.ly/python/) bzw. die darauf aufbauende Bibliothek zur Erstellung von Dashboards [Dash](https://dash.plot.ly/)

# Matplotlib ermöglicht es nahezu jedes Detail eines Charts selber zu definieren. Das wirkt zu Anfang etwas umständlich, hat aber große Vorteile, weil man nicht - wie z.B. in Excel - beschränkt ist in dem, was man darstellen möchte. 

# In[17]:


import matplotlib.pyplot as plt # Importieren der Bibliothek
# Ermöglicht die Darstellung im Jupyter Notebook direkt 
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("seaborn") # unter plt.style.available können sie sich eine Liste der verfügbaren Styles ausgeben lassen. Es ist aber auch möglich eigene Styles zu definieren


# In[ ]:


fig, ax = plt.subplots()
x = np.arange(len(mean_per_region))
y = np.array(mean_per_region["Umsatz"]).flatten()
ax.set_xticks(x)
ax.set_xticklabels(mean_per_region.index)
ax.bar(x,y, align="center", alpha=0.4);
ax.set_title("Umsatz per Region");


# Da `Pandas` und `Matplotlib` zusammenarbeiten kann man in diesem Fall jedoch den Plot auch sehr viel einfacher erstellen.

# In[ ]:


mean_per_region.plot(kind="bar", legend=False,title="Umsatz per Region");


# ## Fazit

# In Summe sollte diese Zusammenstellung zwei Dinge zeigen:
# 
# 1. Durch den Import von Modulen kann Python um speziell benötigte Funktionalitäten erweitert werden
# 
# 2. Die Bibliotheken Numpy, Pandas und Matplotlib sind drei der grundlegenden Bibliotheken zur Datenanalyse in Python
# 
# Natürlich gibt es noch unzählige weitere Bibliothken, die für die Datenanalyse wichtig sind. Mit den o.g. Bibliotheken kann man jedoch schon sehr viel erreichen.

# [<center><< zurück zu Einführung Python</center>](03_Einführung_Python.ipynb)[<center>weiter zur Datenanalyse >></center>](05_Beispiel_Datenanalyse.ipynb)

# In[ ]:




