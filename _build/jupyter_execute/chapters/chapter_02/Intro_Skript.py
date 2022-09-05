#!/usr/bin/env python
# coding: utf-8

# # Nutzung dieses Skripts
# 
# Programmieren lernt man nicht, indem man Büchern darüber liest oder Youtube-Tutorials passiv konsumiert. Um Programmieren ernsthaft zu lernen, muss man es üben und zusätzlich zur Theorie einfach ausprobieren. In diesem Sinne ist das Erlernen einer Programmiersprache nicht so unterschiedlich vom Lernen einer gesprochenen Sprache - auch wenn Sie feststellen werden, dass die "Grammatik" und das "Vokabular" einer Programmiersprache sehr viel simpler ist, als die einer gesprochen Sprache.
# 
# Um Lösungen und Ansätze zu verstehen, muss man diese ausprobieren, adaptieren und alternative Ansätze implementieren. Wir haben dieses Skript deshalb bewusst so aufgesetzt, dass Sie interaktiv mitmachen können. So können Sie per Knopfdruck alle Programmierbeispiele selber ausführen, ausprobieren und adaptieren. 
# 
# ```{admonition} Navigationsleiste
# :class: tip, dropdown
# 
# ![Rocket Button](../assets/Navbar.gif)
# 
# ```

# ## Cloud Coding (🚀)

# 
# 
# Alle Programmierbeispiele erkennen Sie an der speziellen Formatierung. Hier sind zwei Beispiele:
# 
# **Programmierbeispiel 1**

# In[1]:


zahlen = [1, 2, 3]
ergebnis = sum(zahlen)
ergebnis


# **Programmierbeispiel 2**

# In[2]:


import pandas as pd
data = {"Preise": [100, 200, 300], 
        "Produkte": ["Produkt 1", "Produkt 2", "Produkt 3"]}
df = pd.DataFrame(data)
df


# Nahezu jede Seite, die ein solches Beispiel beinhaltet, kann dann per Knopfdruck in einer Cloudumgebung geöffnet werden. In dieser Cloudumgebung (siehe hier: [google colab](https://colab.research.google.com/)) kann der Programmcode dann ausgeführt und beliebig verändert werden. Sie verändern dabei eine in ihrer Cloud gespeicherte lokale Variante dieser Seite, nicht jedoch das originale Kapitel dieses Buchs. 
# 
# Dazu klicken Sie einfach auf das Raketensymbol 🚀 oben rechts auf der Seite. Dieses Symbol ist auf allen Seiten enthalten, auf denen Programmierbeispiele enthalten sind (mit einigen wenigen Ausnahmen).

# ## Download von Kapitel
# 
# Darüber hinaus können Sie sich jedes Kapitel auch lokal herunterladen. So können alle Seiten als `pdf` heruntergeladen und gespeichert werden. Darüber hinaus können Seiten mit Programmierbeispielen auch als sogenannte `ipynb`-Files heruntergeladen werden.  Dies ist dann sinnvoll, wenn Sie sich entscheiden Python lokal auf ihrem Computer zu installieren und die Beispiele lokal ausprobieren wollen. Sie können die Dateien dann via `Jupyter Notebook` öffnen und bearbeiten.

# 
