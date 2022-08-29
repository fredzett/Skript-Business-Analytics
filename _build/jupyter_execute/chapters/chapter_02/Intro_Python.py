#!/usr/bin/env python
# coding: utf-8

# # Einführung in Python
# 
# [PLATZHALTER - HIER KOMMEN NOCH VIELE VERÄNDERUNGEN]
# 
# Nachdem Sie im vorangegangenen Kapitel einen kurze Einführung in den Aufgaben und die Funktionsweise von Jupyter Notebooks erhalten haben, sind wir jetzt endlich soweit uns mit Python zu beschäftigen.  
# (Hinweis: technisch gesehen wurden auch die einfachen Berechnungen im vorangegangen Kapitel bereits in Python durchgeführt)
# 
# Python ist eine sogenannte **interpretierte** Programmiersprache (Interpretersprache), was bedeutet, dass die Sprache nicht wie z.B. C oder Fortran kompiliert, sonder während der Laufzeit ausgeführt wird. Dies führt dazu, dass Python deutlich langsamer ist als kompilierte Sprachen. Darüber hinaus ist Python eine **dynamisch typisierte** Sprache, was bedeutet, dass Variablen-Typen - anders als bei z.B. C - vorab nicht definiert werden müssen und diese sich während der Laufzeit ändern können.   

# ## Warum sollte man Python lernen?
# 
# Python ist eine High-Level Sprache, die sehr einfach zu erlernen ist, weil Sie durch einfache und kompakte Syntax besticht. Python Code sieht deshalb oft sehr intuitiv aus und ist gerade für Programmiereinsteiger eine ideale Sprache für den Start. Trotz dieser Einfachheit ist Python dennoch sehr mächtig und eine sogenannte "all purpose" Sprache, d.h. es gibt keinen Einsatzzweck für welchen Sie Python nicht nutzen könnten (was nicht bedeutet, dass es nicht bessere Sprachen für spezifische Zwecke gäbe). 

# ### Python ist beliebt

# Python hat in den letzten Jahren drastisch an Beliebtheit gewonnen und gilt derzeit als eine der drei weitverbreitesten Programmiersprachen der Welt. 
# 
# Siehe z.B. die zeitliche Entwicklung (in %) der Fragen auf [Stackoverflow](https://stackoverflow.com/) nach Programmiersprache:
# 
# ![Python Stackoverflow](./assets/Popular_Python.png)
# 
# oder den TIOBE Index aus März 2019:
# 
# ![Python TIOBE](./assets/Popular_Python_2.png)

# ### Python ist für Datenanalyse geeignet

# Warum ist Python derzeit so beliebt? Neben der Kombination aus Einfachheit und Mächtigkeit ist einer der Hauptgründe sicherlich, dass sich Python als die Sprache der Wahl im Bereich `Machine Learning` und insbesondere `Deep Learning` etabliert hat. So sind z.B. die zwei **führenden Deep Learning Bibliotheken** 
# 
# - Tensorflow
# 
# - Pytorch 
# 
# beide als Open Source Bibliotheken auf Python basierend  
# (Hinweis: technisch gesehen ist ein Großteil der Bibliotheken in C ausgelagert, jedoch erfolgt die Nutzung der Bibliotheken über einen Python-Wrapper). 
# 
# Dies hat dazu geführt, dass nahezu alle Anwendungen im Bereich Machine Learning oder Predictive Analytics zumindest zu Teilen in Python programmiert sind. 
# 
# Neben den Bibliotheken für Deep Learning stellt Python darüber hinaus unzählige Bibliotheken im Bereich **Machine Learning** (z.B. `scikit-learn`) und **allgemeiner Datenanalyse** (z.B. `Pandas`, `numpy` oder `matplotlib`).
# 
# Darüber hinaus eignet sich Python insbesondere auch als Backend für Webanwendungen, was der Popularität der Sprache zusätzlich Auftrieb gibt (siehe z.B. `flask` oder `django`).

# ### Kombination aus Jupyter Notebooks + Python

# Gerade bei der Datenanalyse muss oft explorativ vorgegangen werden und es ist das Ziel möglichst ohne großen Programmieraufwand fertige Prototypen zu lieferen. Hier ist die Kombination aus Jupyter Notebooks und Python sehr hilfreich. 
# 
# Der explorative Part wird durch die Funktionsweise von Jupyter Notebooks gewährleistet (Einfügen von neuen Zellen, visualisieren von Analysen etc.). Die simple Syntax von Python ermöglicht es Analysen schnell und übersichtlich zu programmieren. 
# 
# Als großer Konkurren ist hier `R` zu nennen, der über RMarkdown ebenfalls über einen Notebook-Konzept verfügt. R ist im Bereich Datenanalyse und Statistik sicherlich vielfältiger und kompletter. Jedoch ist Python in Summe die "breiter aufgestellte" Programmiersprache.

# In[ ]:





# ## Python Syntax

# Es gibt im Internet eine Vielzahl an guten Einführungen in die Syntax von Python. An dieser Stelle sollen nur ein selektiver Auszug gegeben werden,  um die Syntax und einige der Besonderheiten vorzustellen. 
# 
# Als erste Hilfe können Sie sich auf folgenden Seiten informieren:
# 
# - eine deutsche Einführung finden Sie [hier](https://www.python-kurs.eu/python3_variablen.php)
# 
# - eine englische Einführung finden Sie [hier](https://www.w3schools.com/python/python_intro.asp)
# 
# Sie werden schnell feststellen, dass es Freude mach in Python zu programmieren, weil die Syntax im Vergleich zu vielen anderen Sprachen sehr intuitiv ist. 

# ### Einfache Arithmetik

# Wie bereits im vorangegangenen Kapitel gesehen, können wir mit Python ganz einfache Berechnungen durchführen 

# In[1]:


(5 * 12) / 3 + (4 - 1) * 5 + 2


# Wie man sieht kann man - analog zu einem Taschenrechner (oder Excel) - die bekannten arithmetischen Operatoren verwenden.
# 
# `+` = Addition 
# 
# `-` = Subtraktion
# 
# `*` = Multiplikation
# 
# `/` = Division
# 
# **Vorsicht!** `**` =  Potenzieren
# 
# So ist die Schreibweise für $3^4$ in Python

# In[4]:


3**4 # = 3 * 3 * 3 * 3


# ### Zuweisen von Variablen

# Variablen können in Python ganz einfach zugewiesen werden, in dem der Variable ein sinnvoller Name gegeben wird und diesem ein Wert zugewiesen wird. Eine Angabe des Typen ist dabei nicht nötig.

# In[5]:


ganzezahl = 5
ganzezahl


# In[6]:


Komma_Zahl = 3.5
Komma_Zahl


# In[8]:


ganzezahl + 3.3


# ### Dynamische Typisierung

# Python ist eine dynamische typisierte Sprache, d.h. Variablentypen müssen nicht vorab definiert werden. Variablentypen können auch dynamisch verändert werden. 
# 
# **Hier ein Beispiel:**
# 
# Die Variable **temperatur** wird deklariert und automatisch zum Typ `Integer` (Ganzzahl). In der darauffolgenden Zelle wird die Variable zu einem Typ `Float` (Kommazahl). 

# In[ ]:


temperatur = 12
temperatur


# In[ ]:


temperatur =  temperatur + 14.4556
temperatur


# Den Typen einer Variable kann ich über das Kommando `type` feststellen.

# In[ ]:


temperatur = 12
type(temperatur), temperatur


# In[ ]:


temperatur = 12 + 14.4556
type(temperatur), temperatur


# Das variable Typisierung ist dabei nicht auf numerische Typen beschränkt. So kann die Variable "temperatur" auch dynamisch zu einem String werden. 

# In[10]:


temperatur = 12
type(temperatur), temperatur


# In[ ]:


temperatur = "ein String"
type(temperatur), temperatur


# ### Nützliche Hilfen

# **Woher weiß ich welche Methoden und Operationen für einen Typ oder Objekt verfügbar sind?**
# 
# Sie können entweder die im vorangegangenen Kapitel erwähnte `tab completion` nutzen oder aber die `Hilfe-Funktionen`. Dies gilt für alle Objekte in Python (nicht nur die String-Variable).

# In[11]:


temp1 = 12
temp2 = 15
temp3 = 19


# In[14]:


class Person():
    def __init__(self,name=None,alter=None):
        self.name = name
        self.alter = alter


# In[ ]:


# Tab Completion (drücken Sie Tab)
temperatur


# In[ ]:


# zeigt alle Methoden (hier vom Typ String) an
dir(temperatur)


# Wenn man Hilfe zu einer bestimmten Methode benötigt - hier z.B. zur Methode "replace" - kann `shift + tab + tab` helfen.
# 
# ![Tab Completion 3](./assets/Tab_Completion_3.png)

# In[ ]:


temperatur.replace


# ### Strings

# In[ ]:


string = "Ich bin ein kurzer String"


# Schreibe alles in Großbuchstaben

# In[ ]:


string.upper()


# Schreibe alles in Kleinbuchstaben

# In[ ]:


string.lower()


# Zähle, wie oft der Buchstabe Buchstaben "i" in der Variable "string" vorkommt

# In[ ]:


string.count("i")


# Ersetze das "g" durch ein "k"

# In[ ]:


string.replace("g","k")


# In Python können Methoden verkettet werden

# In[ ]:


string.replace("i","A").upper().replace("E","y")


# Splitte die Variable "string" immer dort, wo ein Leerzeichen vorkommt

# In[ ]:


wörter = string.split(" ")
wörter


# ### Listen

# Die Variable "wörter" ist eine Liste

# In[ ]:


type(wörter)


# Listen können eine beliebige Art von Elementen und unterschiedlichen Typen enthalten. 

# In[ ]:


liste = ["Erster Eintrag",2,"a",True,"!"]
liste


# Via `[idx]` kann dann auf die einzelnen Elemente zugegriffen werden.
# 
# <font color='red'>In Python beginnt das erste Element immer mit '0'</font>

# In[ ]:


el_1 = liste[0]
el_1, type(el_1)


# In[ ]:


el_4 = liste[3]
el_4, type(el_4)


# Es können auch mehrere Elemente gleichzeitig aus einer Liste extrahiert werden. Mit Hilfe der Notation `[:idx]` werden alle Elemente exklusive von `idx` extrahiert. In nachfolgenden Beispiel werden die Eintrage 0, 1 und 2 extrahiert

# In[ ]:


liste[:3]


# Hier werden die letzten drei Einträge aus der Liste extrahiert

# In[ ]:


liste[-3:]


# Listen können verändert werden

# In[ ]:


liste[2] = "neuer Eintrag"
liste


# Listen können verlängert werden

# In[ ]:


liste.append("???")
liste


# Listen können auch verbunden werden in dem diese addiert werden

# In[ ]:


liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste1 + liste2


# [<< Zurück zu Einführung Jupyter Notebooks](02_Jupyter_Notebooks.ipynb) | [ Weiter zu Einführung Datenanalyse >>](04_Einführung_Datenanalyse.ipynb)

# ### Control Flow

# Wie in den meisten Programmiersprachen können in Python sogenannte Control Flows durchgeführt werden. Z.B. ein `if statement` oder eine `for schleife`

# #### Einrücken

# Die Python-Syntax ist an dieser Stelle eher ungewohnt, da Control Flow Statements nicht z.B. durch geschwungene Klammern `{}` dargestellt werden, sondern durch einfaches `Einrücken`. Dies erfolgt über `4 Leerzeichen`, wobei Jupyter Notebooks dies eigenständig übernimmt, wenn es nötig wird.

# #### If Statements

# In[ ]:


# Einzelne If-Abfrage
variable = 1

if variable > 2:
    print("Variable ist größer als 2")


# In[ ]:


# If-Else-Abfrage
variable = 2

if variable > 2:
    print("Variable ist größer als 2")
else:
    print("Variable ist kleiner oder gleich 2")


# In[ ]:


# If-Else-Abfrage
variable = 2

if variable > 2:
    print("Variable ist größer als 2")
elif variable < 2:
    print("Variable ist kleiner 2")
else: 
    print("Variable ist gleich 2")


# Bei unterschiedlichen `boolean` Bedingungen müssen die jeweiligen Bedingungen in `()` geschrieben werden

# In[ ]:


variable1 = 3
variable2 = "Celsius"

if (variable1 <= 4) & (variable2 == "Celsius"):
    print("Vorsicht, es könnte glatt auf den Straßen sein")
elif (variable1 <=4) & (variable2 == "Fahrenheit"):
    print("Bitte nicht rausgehen. Es ist gefährlich kalt!!!!!")


# In[17]:


import pandas as pd


# In[19]:


daten = {"A":[1,2,2,3],"B":["A","B","C","D"]}
df = pd.DataFrame(daten)
get_ipython().run_line_magic('pinfo2', 'df.asfreq')


# #### For-Schleifen

# Jede For-Schleife in Python hat die folgende grundsätzliche Strukur
# 
#     >>> for item in object:
#             do something
#             
# Jedes iterierbare Objekt kann also durch eine For-Schleife durchlaufen werden. Das `Objekt` muss also exisiterien.

# In[ ]:


ein_string = "Datenanalyse" # In Python ist ein String ein iterierbares Objekt

for buchstabe in ein_string:
    print(buchstabe)


#  Die Benennung von `item` ist dabei dem User überlassen.

# In[ ]:


for mein_name_für_ein_element in ein_string:
    print(mein_name_für_ein_element)


# In[ ]:


eine_list = ["A","b",True,1,5,6,["Eine","Liste","in einer Liste"],"letztes Element"] # in Python ist eine Liste ein iterierbares Objekt
for el in eine_list:
    print(el)


# Ein spezieles iterierbares Object ist das `range` Objekt. Möchte ich eine For-Schleife 10x durchlaufen schreiben wir

# In[ ]:


for i in range(10):
    print(i)


# #### List Comprehension

# In Python wird die Schreibweise
# 
#     >>> for item in object:
#             do something
#             
# oft vermieden und stattdessen eine sogenannte `list comprehension` durchgeführt. Dies ist immer dann der Fall wenn wir als Ergebnis einer For-Schleife eine Liste benötigen. 
# 
# Beispiel: wir wollen eine Liste mit der Anzahl an Buchstaben je Name erzeugen (Hinweis: `len` = Länge eines Objektes)

# In[22]:


namen = ["Kurt","Anton","Charlotte","Johannes","Ernst","Ida"]


# **List Comprehension**

# In[23]:


anz_buchstaben = [len(name) for name in namen] # List Comprehension
anz_buchstaben


# Diese Schreibweise ist äquivalent zu 
# 
# **For-Schleife**

# In[ ]:


anz_buchstaben = []
for name in namen:
    anz_buchstaben.append(len(name))
anz_buchstaben


# Ein erfahrener Python-Programmierer würde jedoch immer die List Comprehension bevorzugen

# List Comprehensions können auch mit anderen Control Flows kombiniert werden.
# 
# Beispiel: wir wollen eine Liste an Namen generieren, die mit einem Vokal beginnen 

# In[ ]:


vokale = list("AEIOU")


# In[ ]:


[name for name in namen if name[0] in vokale]


# Was ist hier passiert? Es wurde folgende Abfrage getätigt. 
# 
# Für jeden `name` in der Liste mit `name`. Falls das erste Element in `name` in der Liste `vokale` ist. Dann speicher den Namen in der neuen Liste

# #### While-Schleifen
# 

# Jede While-Schleife in Python hat die folgende grundsätzliche Strukur
# 
# ```
# >>> while condition:
#         do something in this
#         code block as long as condition
#         evaluates as True
# ```

# In[ ]:


# Herunterzählen von einem Counter
counter = 10
while counter >= 0:
    if counter == 0:
        print("Abflug!")
    else:
        print(f'{counter} Sekunden bis zum Abflug')
    counter -= 1 # Äquivalent zu counter = counter - 1


# ### Funktionen

# #### Python "buildin" Funktionen

# Python beinhaltet standardmäßig rund 70 Funktionen ([siehe hier](https://docs.python.org/3/library/functions.html)). Diese Funktionen können dementsprechend ohne weiteres Zutun verwendet werden. 
# 
# Ein Beispiel: die Funktion `sum`. 
# 
# (Hinweis: durch `shift + tab + tab` kann man Informationen zur Funktion finden)

# In[ ]:


liste = [1,4,5,6,7]
sum(liste)


# In[ ]:


max(liste)


# In[ ]:


max("abcdefh")


# #### Vom Nutzer definierte Funktionen

# Es ist klar, dass die 70 Standardfunktionen nicht ausreichen, um eigene Analysen durchzuführen. Insofern wird kein Nutzer drumherum kommen eigenen Funktionen zu schreiben. 
# 
# In Python ist jede Funktion wie folgt aufgebaut:
# 
#     >>> def funcname(args):
#             do stuff
#             return result
#             
# Beispiel **Hello World**

# In[ ]:


def hello():
    print("Hello, World!")


# In[ ]:


hello()


# **Ein etwas komplexeres Beispiel:** Umrechnung von Celsius in Fahrenheit.
# 
# $$ F = C \times 1.8 + 32$$

# In[ ]:


def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


# In[ ]:


celsius_to_fahrenheit(20)


# In Python können Funktionen sowohl mehrere Inputargumente haben, als auch mehrere Return Argumente
# 
# **Beispiel:** eine Funktion zum Verbinden von Strings. Als Input werden zwei Strings benötigt. Als Output wird (i) der verbundene String und (ii) der verbundene String in Großbuchstaben zurückgegeben

# In[ ]:


def concat_and_upper(string1, string2):
    string_new = string1 + string2
    return string_new, string_new.upper()


# In[ ]:


text1 = "Dies ist ein"
text2 = " Test, der hoffentlich funktioniert!"
output1, output2 = concat_and_upper(text1,text2)


# In[ ]:


output1


# In[ ]:


output2


# In[ ]:


output_combined = concat_and_upper(text1,text2)
output_combined, type(output_combined)


# In[ ]:


output_combined[0]


# In[ ]:


output_combined[1]


# Schreibt man eigene Funktionen, sollte man diese mit sogenannten `doc strings` versehen. Hierbei handelt es sich um einen kurzen Text, der erläutert, was die Funktion tut (wobei die Vergabe des Funktionsnamens dies idealerweise auch schon verdeutlicht). 

# In[ ]:


def sum_and_add_4(a,b):
    '''
    Summiert Input "a" und "b" und addiert 4 hinzu
    
    Input: zwei numerische Werte
    Output: ein numerischer Wert
    
    Beispiel sum_and_add_4(4,2) gibt (4+2)+4 = 10 zurück
    '''
    
    return (a+b) + 4


# In[ ]:


sum_and_add_4(4,2)


# Den beschreibenden Text wird dann via `shift + tab + tab` zugänglich. 
# 
# ![Beispiel Docstring](./assets/Beispiel_Docstring.png)

# #### Annonyme Funktionen (lambda Funktionen)

# Manchmal möchte man eine kurze Berechnung durchführne und dafür nicht extra eine eigene Funktion benennen. Hierzu bieten sich `lambda Funktionen` an. 

# In[20]:


def summe2(a,b):
    return a + b


# In[21]:


summe2(3,4)


# In[ ]:


f = lambda a,b: (a + b) + 4


# In[ ]:


f(4,5)


# Lambda-Funktionen sind insbesondere dann hilfreich, wenn ich diese innerhalb einer anderen Funktion nutzen möchte. 
# 
# **Beispiel:** Sortieren einer Liste mithilfe der buildin Funktion `sorted`

# In[ ]:


string_liste = ["Apfel","Banane","Orange","Melone"]
sorted(string_liste)


# Die Funktion sortiert die Liste nach Anfangsbuchstaben. Was wenn ich die Liste aber nach z.B. dem zweiten Buchstaben sortieren möchte? 
# 
# Zunächst stelle ich mithilfe von `shift + tab + tab` fest, dass ich der Funktion `sorted` einen weiteren Parameter `key` übergeben kann. 
# 
# 
# ![Beispiel sorted](./assets/Beispiel_sorted.png)  
# 
# <br></br>
# Hierzu könnte ich zunächst eine neue Funktion schreiben, die den zweiten Buchstaben eines jeden Wortes ausgibt

# In[ ]:


def second_letter(string):
    return string[1] # Erinnerung: ein Eintrag in Python beginnt immer mit 0, d.h. der Eintrag "1" ist der zweite Wert


# In[ ]:


sorted(string_liste,key=second_letter)


# Die Funktion `second_letter` wird eigentlich nur einmal benötigt. Hier bietet es sich an mit einer `lambda Funktion` zu arbeiten.

# In[ ]:


sorted(string_liste, key=lambda wort: wort[1])


# [<center><< zurück zu Einführung Jupyter Notebooks</center>](02_Jupyter_Notebooks.ipynb)[<center>weiter zur Module nutzen >></center>](04_Module_nutzen.ipynb)
