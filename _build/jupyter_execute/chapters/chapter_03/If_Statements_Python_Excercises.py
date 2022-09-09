#!/usr/bin/env python
# coding: utf-8

#  # Übungen 3

# ## Aufgabe 1
# 
# Sie haben eine Liste mit Wörtern. Erstellen Sie eine neue Liste, die nur diejenigen Wörter beinhaltet, die nicht mit "vor" oder "Vor" beginnen. 
# 
# (Hinweis: die einzelnen Wörter sind vom Typ `str`. Schauen Sie sich die `str`-Methoden `lower` und `startswith` an, um dieses Problem zu lösen)

# In[5]:


wörter = ["vorstellen", "Vorbereitung", "essen", "vorgeben", "Haferflocken", "Kunstgalerie"]


# ## Aufgabe 2

# Schreiben Sie eine Funktion `check_zahl`, welche als Input eine beliebige Zahl zwischen 0 und 30 erhält und als Ergebnis ausgibt, ob die Zahl 
# 
# - größer als 10, aber kleiner als 20 (Output: "A")
# - größer oder gleich 20 (Output: "B")
# - gleich 5, 14 oder 27 (Output: "C")
# - kleiner oder gleich 10 (Output: "ERROR")
# 
# Beispiel: 
# ```{code} Python
# zahl = 14
# check_zahl(zahl)
# >>> "C"
# 
# zahl = 12
# check_zahl(zahl)
# >>> "A"
# ```

# 
