#!/usr/bin/env python
# coding: utf-8

# # Übungen: Pandas

# ## Aufgabe 1: Einlesen einer Exceldatei
# 
# Lesen Sie eine beliebige Exceldatei via `pd.read_excel` ein. 
# 
# Wenn Sie Google Colab nutzen, laden Sie dafür zunächst eine Datei in die Umgebung 
# 
# 
# ```{admonition} Upload Google Colab
# :class: tip, dropdown
# ![](../assets/read_xls_colab.gif)
# 
# ```

# ## Aufgabe 2: Einlesen via Clipboard
# 
# Manchmal haben wir Daten, die wir schnell für eine kurze, einmalige Analyse in Pandas überführen würden. Z.B. eine Exceltabelle, für die wir schnell etwas ausrechnen möchten. Wir können in diesem Fall auch einfach via `pd.read_clipboard` die Daten in Pandas überführen. 
# 
# Recherchieren Sie, was die Funktion macht und erstellen ein Dataframe auf Basis dieser Logik. 

# Lesen Sie die beiden Sales-Datensätze ein (File-Links finden Sie im [vorherigen Notebook](../chapter_04/Intro_Pandas.ipynb)) und beantworten Sie folgende Fragen

# ## Aufgabe 3

# Nutzen Sie die bestehenden Datensätze:
# 
# - wie groß ist die maximale Verkaufsmenge je Produkt und je Tag
# - wieviel Transaktionen gab es je Produkt pro Tag

# ## Aufgabe 4

# Sie haben folgende ergänzende Information: die variablen Stückkosten je Produkt betragen:
# 
# - Produkt 1: 6 EUR
# - Produkt 2: 2 EUR
# - Produkt 3: 9 EUR
# - Produkt 4: 4 EUR
# - Produkt 5: 13 EUR
# 
# Berechnen Sie die gesamten Deckungsbeiträge je Produkt.

# ## Aufgabe 5

# Laden Sie die folgenden Aktienkursdaten der Firma **Uniper** in ein Dataframe und führen Sie folgende Berechnungen durch:
# 
# 1. Ergänzen Sie den Datensatz um die tägliche Aktienkursrendite (Hinweis: $\frac{P_t}{P_{t-1}} - 1$)
# 2. Berechnen Sie die kumulierte Rendite seit Beginn des Jahres und fügen diese als zusätzliche Spalte hinzu
# 3. Ergänzen Sie eine Spalte "Wochentag" (Tipp: wandeln Sie die Spalte mit dem Datum sinnvoll um; `pd.to_datetime` kann hier ggf. helfen)

# 

# In[37]:


link_uniper = "https://query1.finance.yahoo.com/v7/finance/download/UN01.DE?period1=1640995200&period2=1664236800&interval=1d&events=history&includeAdjustedClose=true"


# In[ ]:




