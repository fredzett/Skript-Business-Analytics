#!/usr/bin/env python
# coding: utf-8

# # Pandas: das schweizer Taschenmesser

# Wir stellen nun das für uns wohl wichtigste Modul in Python vor: [`pandas`](https://pandas.pydata.org/getting_started.html).
# 
# Pandas baut "im Hintergrund" auf dem im vorherigen Kapitel vorgestellten Modul `numpy` auf, ist jedoch für einen etwas anderen Zweck erstellt worden. 
# 
# Im Kontext der Datenanalyse haben wir es oft mit tabularischen Daten zu tun, d.h. wir arbeiten mit Informationen und/oder Daten, die in Tabellen gespeichert sind. Typischerweise haben diese Informationen Beschriftungen und sind von unterschiedlichen Typen. Stellen wir uns dies in Excel vor: wir haben mehrere Spalten, jede Spalte hat eine Bezeichnung, die beschreibt, um welche Information es sich handelt. Einige Spalten haben numerische Informationen (z.B. Umsätze), andere haben text-basierte Informationen (z.B. Namen oder Orte), wieder andere haben ein Datum als Spalteninhalt. Pandas ist das Modul, welches für den Umgang mit dieser Art von Daten gemacht wurde. 
# 
# 
# Unseren bisherigen Beispiele basierten oft auf vereinfachenden Datensätzen, die nicht vergleichbar mit denen sind, die wir in Unternehmen typischerweise vorfinden. Diese Beispiele dienten zur Veranschaulichung der Grundlagen der (datengetriebenen) Programmierung und waren für die eigentliche Datenanalyse wie wir sie durchführen wollen nicht realistisch. Wenn wir es mit typischen Fragestellungen im unternehmerischen Kontext (aber auch in der Forschung) zu tun haben, dann besteht ein Analyseprozess oft auf verschiedenen Schritten:
# 
# 1. Einlesen von Daten
# 
# 2. Daten aufbereiten und ggf. ergänzen
# 
# 3. Daten explorativ untersuchen und zusammenfassen
# 
# 4. Daten analysieren  
# 
# 5. Daten präsentieren in Form von Tabellen oder Graphiken
# 
# Pandas unterstützt alle diese Schritte, in dem es hierfür sinnvolle Funktionalitäten bereitstellt. Die gesamte Bandbreite an Funktionalitäten ist so groß, dass es unmöglich ist, diese im Rahmen _eines_ Kurses zu erläutern und vorzustellen. Zusätzlich ist es so, dass Pandas am Besten im Zusammenspiel mit anderen Modulen (z.B. Numpy, aber auch Modulen zur Visualisierung) eingesetzt wird. Wir werden uns in diesem Kapitel auf selektive, aber - aus unserer Perspektive - wesentliche Funktionalitäten beschränken (müssen). Insbesondere werden wir uns darüber hinaus auch auf Techniken konzentrieren, die für den Einsatz von Pandas besonders geeignet sind. 
# 
# ```{admonition} Ressourcen zu Pandas
# :class: tip, dropdown
# 
# Es gibt im Internet viele frei verfügbare Ressourcen zu Pandas. Eine sehr gelungene Einführung ist das Kapitel aus [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html). Außerdem ist das [Cheat-Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) mit einer Zusammenfassung wichtiger Methoden sehr hilfreich. 
# 
# ```
# 
# In diesem Kapitel werden wir einige wichtige Grundlagen von Pandas vorstellen. Wir nutzen hierfür - wie in den vorherigen Kapiteln auch - kleine Beispieldaten. Im nächsten Kapitel werden wir dann realistischere Datensätze verwenden, um wichtige Konzepte quasi am "lebenden Objekt" zu erlernen. Wir glauben, dass Sie zunächst einige wichtige Grundlagen verstanden haben müssen und um diese zu erläutern benötigen wir keine "echten" Daten. Ab einem gewissen Punkt geht es jedoch nicht mehr darum isolierte Funktionen vorzustellen, sondern vielmehr den tatsächlichen Prozess der Datenanalyse zu durchlaufen, um dann auf reale Probleme zu stoßen und praxirelevante Lösungsansätze vorzustellen. 
# 
# Beginnen wir mit den Grundlagen.

# ## Grundlagen

# Wir stellen im Folgenden ausgewählte Grundlagen des Moduls vor. Hierbei fokussieren wir uns auf 
# 
# 1. das Importieren des Moduls 
# 2. das Erstellen von `Series` und `Dataframes`

# ### Importieren des Moduls

# Bevor wir Pandas nutzen können, müssen wir das Modul zunächst importieren. Wir können hier prinzipiell wieder vorgehen, wie wir dies im Kapitel [Einführung: Module](../chapter_04/Intro_Modules.ipynb) aufgeführt haben. Typischerweise wird Pandas jedoch - analog zu Numpy - als ganzes Modul importiert und dann mit einer Kurzbezeichnung versehen. Es ist daher empfehlenswert, Pandas wie unten aufgeführt zu importieren.  

# In[1]:


import pandas as pd


# ### Series und Dataframes

# Sowie bei Numpy das Herzstück der Numpy-Array (`np.array`), ist bei Pandas das Herzstück der sogenannte Dataframe (`pd.Dataframe`). Sie können sich ein Dataframe als ein Excel-Sheet bzw. eine Excel-Tabelle vorstellen. So wie in Excel jede Tabelle aus einer Ansammlung aus Spalten besteht, ist ein Dataframe in Pandas eine Ansammlung von Series (`pd.Series`).
# 
# Schauen wir uns das untenstehende Excelbeispiel an.
# 
# ![xlsdataframe](../assets/dataframe_xls.png)

# Die abgebildete Tabelle wäre ein `dataframe`, jede Spalte eine `series`. Die Spalte "Preis" wäre eine Series mit `floats`, d.h. mit Dezimalzahlen. Die Spalte "Datum" wäre eine Series vom Typ `str` oder von einem Typ, der ein Datum abbilden kann (diesen Datentyp werden wir in diesem Kapitel noch kennenlernen).  
# 
# Schauen wir uns an, wie wir diese Daten in `pandas` abbilden. 

# ## Erstellen von Series

# Wir können - ähnlich wie beim Numpy Array - Series relativ einfach manuell erstellen. Wenn wir die Spalte "Menge" nachbilden möchten, so können wir z.B. folgendes schreiben:

# In[22]:


s1 = pd.Series([23,1,12,6,89,4], name="Menge")
s1


# Wir sehen, dass das Vorgehen fast identisch ist zur Erstellung eines Numpy-Arrays. Ein wichtiger Unterschied ist jedoch, dass ich der Series einen Namen geben kann. Wir haben hier die Namen "Menge" vergeben. Wir können uns den Namen wie die Spaltenbezeichnung in einer Exceltabelle vorstellen. Die in der Variable "s1" gespeicherte Series hat den Namen "Menge" und ist vom Typ `int`[^1]. 
# 
# [^1]: Hinweis: genauer gesagt vom Typ `int64`. Die Zahl hinter `int` macht deutlich, dass es eine 64-bit Integer ist und gibt uns damit Aufschluss über den abbildbaren Wertebereich (und damit auch über den benötigten Speicher) des Datentyps. Diese technischen Feinheiten sind für unsere Zwecke an dieser Stelle nicht relevant. Weitere Informationen dazu finden Sie z.B. [hier](https://de.wikipedia.org/wiki/Integer_(Datentyp)).
# 
# 
# Erstellen wir nun eine Series, die die Spalte "Preis" abbildet und speichern diese in der Variable "s2". Wir schreiben den ersten Wert mit Dezimalpunkt, da die Series dann automatisch erkennt, dass es sich um den Datentyp `float` handelt. 

# In[23]:


s2 = pd.Series([10., 5, 9, 3, 5, 10], name="Preis") # Der Dezimalpunkt signalisiert "float"
s2


# Wir könnten den Datentyp auch explizit angeben. Der untenstehende Code gibt an, dass die Series vom Datentyp `str` sein soll, so dass die Elemente Texte sind. In Pandas wird dies dann als `object` bezeichnet. 

# In[24]:


s3 = pd.Series([10, 5, 9, 3, 5, 10], name="Preis", dtype=str) 
s3


# ## Erstellen von Dataframes

# Dataframes können manuell erstellt werden oder aus eingelesenen Daten erstellt werden. Wir gehen hier zunächst auf die manuelle Erstellung ein. Diese benötigen wir in der Praxis oft gar nicht, weil wir meist auf externe Daten (z.B. Excel-, CSV-, SQL- oder TXT-Dateien) zugreifen. Dennoch ist es wichtig zu verstehen, wie Dataframes manuell erstellt werden können, da dies hilft (i) den grundsätzlichen Aufbau von Dataframes zu verstehen und (ii) manchmal hilfreich ist, um kleinere Datensätze zu Testzwecken zu erzeugen. 

# ### Manuelle Erstellung

# Wir können Dataframes auf verschiedene Art und Weisen erstellen. Wir gehen hier auf eine Variante ein, die aus unserer Sicht am sinnvollsten ist und die meisten Anwendungsfälle abdeckt: wir erstellen Dataframes über Dictionaries (`dict`). 
# 
# Den Datentyp haben wir im Kapitel **Einführung in Python** [hier](intro:dicts) kennengelernt.
# 
# Hier der Beispielcode für ein Dataframe, welcher die Spalten (in dem Falle Series) **"Preis"** und **"Menge"** beinhaltet.

# In[35]:


data = {"Menge": [23, 1, 12, 6, 89, 4], "Preis":[10., 5, 9, 3, 5, 10]}
data


# In[36]:


df = pd.DataFrame(data)
df


# Wir sehen, dass der sog. `key` des Dictionaries als Spaltenbezeichnung übernommen wird. Jedoch können wir die Spaltenbezeichnung auch explizit vorgeben. 
# 
# Dies sähe dann so aus:

# In[37]:


df.columns = ["A", "B"]
df


# 
#  
#  
#  
# Die einzelnen Werte (sog. `items`) sind in unserem Falle Listen gewesen. 
# Wir können hier jedoch auch andere Datentypen nutzen. So können wir auch Numpy-Arrays oder Series einfügen.
# 
# Hier zwei Beispiele:

# In[28]:


data = {"Menge": s1, "Preis": s2}
df2 = pd.DataFrame(data)
df2


# In[29]:


import numpy as np

data = {"Menge": np.array([23, 1, 12, 6, 89, 4]), "Preis":np.array([10., 5, 9, 3, 5, 10])}
df3 = pd.DataFrame(data)
df3


# ### Einlesen von Daten

# Wie bereits angesprochen ist es realistisch, dass wir bereits über Daten verfügen und diese in Pandas einlesen möchten. Hierfür bietet Pandas eine Vielzahl an Methoden, die es ermöglicht nahezu jeden Datentyp einzulesen. Wir werden uns in den nächsten Kapiteln auf das Einlesen von Excel- und CSV-Dateien beschränken. Das grundsätzliche Vorgehen ist jedoch - unabhängig von der Dateiform - identisch. 
# 
# Pandas bietet die Methoden zum Einlesen von externen Daten via `pd.read_` an. 
# 
# Wir können uns über `pd.read_<tab>` anzeigen lassen, welche Funktionen zur Verfügung stehen und uns die gewünschte raussuchen. 
# 
# ![pdread](../assets/pdread_tab.png)

# Zum Einlesen der gewünschten Daten benötigen wir typischerweise den Dateipfad, d.h. den Ort, in welchem die Datei auf dem Computer oder in der Cloud hinterlegt ist. 

# In[39]:


file = "../assets/datasets/small/sales.xlsx"

pd.read_excel(file)


# 
