#!/usr/bin/env python
# coding: utf-8

# # Übungen 2

# Hinweis: die (build-in) Funktion `zip` könnte ihnen bei den folgenden Aufgaben helfen. 

# ## Aufgabe 1

# Sie wollen ihren Kunden Rechnungen schicken und dafür die Anrede zu Beginn des Schreibens automatisieren. Schreiben Sie eine Funktion, die die untenstehenden Daten als Input nutzt und für jeden Kunden eine Anrede nach folgendem Prinzip ausgibt:
# 
# "Hallo Vorname Zuname"

# In[5]:


vornamen = ["Hans", "Manuela", "Peter", "Nathalie"]
nachnamen = ["Horst", "Mühlweber", "Packendorf", "Nursucher"]


# ## Aufgabe 2

# Ihr Unternehmen hat in den letzten Wochen außergewöhnlich viele Kunden verloren. Ihr Chef wird nervös und bittet Sie - auf Basis der unten angegebenen Daten - zu berechnen, wieviel % Umsatz ihr Unternehmen dadurch verloren hat. Da die Zahlen evtl. noch einmal aktualisiert werden, sollten Sie idealerweise eine Funktion dafür schreiben. 
# 
# Sie haben zwei Listen mit Daten, die zueinander passen. In der ersten Liste ist mit 1 angegeben, falls ein Kunde gekündigt hat. In der zweiten Liste ist der entsprechende Umsatz der Kunden angegeben. 

# In[16]:


kündigung = [1, 0, 0, 1, 1, 0 , 0, 1, 1, 1, 0, 0, 0, 0] # 1 = hat gekündigt, 0 = nicht gekündigt
umsatz = [10, 20, 10, 20, 30, 22, 10, 145, 15, 23, 29, 17, 78, 63]


# ## Aufgabe 3

# In Aufgabe 1 auf Übungsblatt 1 (siehe [hier](blatt1:aufgabe1)) haben Sie eine Umrechnung vorgenommen. Schreiben Sie eine Funktion, die diese Umrechnung vornimmt und als Input Rohstoff A hat und die Menge von Rohstoff B ausgibt.  

# 
