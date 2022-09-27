#!/usr/bin/env python
# coding: utf-8

# # Übungsblatt: Numpy

# ## Aufgabe 1

# Erstellen sie einen Array mit 3 Zeilen und 4 Spalten mit den Zahlen 1 bis 12

# ## Aufgabe 2

# Der folgende Array beinhaltet Zahlen zwischen 1 und 10. Bestimmen Sie die realtive Häufigkeit der jeweiligen Zahlen. Bestimmen Sie z.B. wie häufig der Wert `1` im Array vorkommt relativ zu allen anderen, d.h. z.B. 14% der Werte sind eine 1.

# In[10]:


import numpy as np
np.random.seed(13455)  


data = np.random.randint(1,10, (100,100))
data


# ## Aufgabe 3

# Bestimmen Sie vom obigen Array `data` die Summe der Spalten.

# ## Aufgabe 4

# Schreiben Sie eine Funktion `select`, die einen beliebigen 2D-Array sowie die gewünschte Zeile und Spalte als **Input** bekommt. Als Output gibt diese dann das Angegebene Element zurück. 
# 
# Beispiel: `select(data, row=4, col=2)` gibt das Element aus der 4. Zeile und der 2. Spalte zurück.
