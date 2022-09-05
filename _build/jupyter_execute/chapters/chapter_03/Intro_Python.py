#!/usr/bin/env python
# coding: utf-8

# # Einführung in Python

# ```{admonition} Online-Resourcen
# :class: tip, dropdown
# 
# Es gibt im Internet eine Vielzahl an guten Einführungen zum Thema Programmieren in Python. 
# 
# Hier zwei Beispiele:
# 
# - Detaillierte Python-Kurs:  [hier](https://www.python-kurs.eu/python3_variablen.php)
# 
# - Links mit weiteren Ressourcen: [hier](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
# 
# Insbesondere zu als Anfänger ist die Menge an Tutorial überwältigend und es fällt schwer zu beurteilen, was davon geeignet und für unsere Zwecke sinnvoll ist. Je mehr Erfahrung und Übung Sie jedoch bekommen, desto einfacher fällt es zielgerichtet im Internet nach Hilfe zu suchen. 
# 
# ```
# 
# 

# ### Einfache Arithmetik

# Wie bereits im vorangegangenen Kapitel gesehen, können wir mit Python ganz einfache Berechnungen durchführen 

# In[3]:


1 + (5 * 12) / 3 - 12


# Wie man sieht, kann man - analog zu einem Taschenrechner (oder Excel) - die bekannten arithmetischen Operatoren verwenden.
# 
# `+` = Addition 
# 
# `-` = Subtraktion
# 
# `*` = Multiplikation
# 
# `/` = Division
# 
# `**` =  Potenzieren (❗ die Schreibweise für $3^4$ in Python lautet $3{**}4$)

# Dieses Vorgehen ist jedoch meist nicht sinnvoll und wenig vorteilhaft gegenüber einem Taschenrechner. 
# 
# Als Analogie können wir uns kurz Excel (oder ein alternatives Tabellenkalkulationsprogramm) vorstellen. Dort schreiben wir auch typischerweise nicht in eine Zelle eine komplette Formel mit fest codierten Werten.
# 
# ![Excel schlecht](../assets/Excel_bad.png)
# 
# Stattdessen würden sie die Werte auf verschiedene Zellen aufteilen und in einer Ergebniszelle verknüpfen. Dieses Vorgehen hat den Vorteil, dass die Annahmen für das Ergebnis viel transparenter sind. So wird z.B. deutlich, dass es sich bei der $12$, die in der Berechnung zwei Mal vorkommt um tatsächlich zwei verschiedene Annahmen handelt, die nur zufällig den selben Wert haben.  
# 
# ![Excel gut](../assets/Excel_good.png)

# ### Zuweisen von Variablen

# Das Äquivalen in Python ist die Nutzung von Variablen. Wir können Werte als Variablen abspeichern[^1], in dem wir das "`=`"-Symbol benutzen. 
# 
# 
# [^1]: diese Formulierung ist nicht ganz korrekt, jedoch für unsere Zwecke ausreichend.
# 
# Wir schreiben also 
# 
# ```
# variable = wert
# ```
# 
# `variable` kann hier jeden Namen annehmen[^2]. Für `wert` können wir Ganzahlen, Dezimalzahlen, Wörter oder auch ganz andere Objekte - z.B. Graphen oder Dataframes die wir teilweise noch kennenlernen werden - einsetzen. 
# 
# [^2]: Ausnahmen sind in Python bereits belegte Wörter, sog. Keywords, diese sind hier aufgeführt [keywords](https://www.w3schools.com/python/python_ref_keywords.asp).
# 
# Hier ein paar Beispiele:

# In[5]:


zahl = 42
wort = "Spaghetti"
satz = "Deutscher Meister wird nur der BVB"


# Namen für Variablen sollten sinnvoll und prägnant (d.h. nicht zu lang) sein. In Python gibt es darüber hinaus die Konvention (siehe [PEP 8](https://peps.python.org/pep-0008/#function-and-variable-names)), dass Variablen klein geschrieben werden und mehrere Wörter mit "`_`" getrennt werden. 
# 
# Beispiel:

# In[7]:


sehr_wichtige_variabel = 321


# Diese Konvention ist für die Funktion eines Programms nicht entscheiden, jedoch erleichtert dies die Lesbarkeit des Codes.

# Wir können unser obiges Formelbeispiel also verbessern, in dem wir die Annahmen in verschiedene Variablen speichern und dann miteinander zu einem Ergebnis kombinieren. 

# In[11]:


input1 = 1
input2 = 5
input3 = 12
input4 = 3
input5 = 12
ergebnis = input1 + (input2 * input3) / input4 - input5
ergebnis


# **Beispiel: Berechnung Kapitalbarwert**
# 
# Lassen Sie uns unser neugewonnenes Wissen direkt mithilfe eines konkreten Anwendungsfalles ausprobieren. Wir wollen berechnen, ob sich eine Investition lohnt. Hierfür haben wir untenstehende Annahmen gegeben:
# 
# - Investition ($I_0$): -10.000
# - Cashflows ($CF_t$) in den Jahren 1 bis 3: 5.000, 4.000 und 3.000
# - Zinssatz ($i$): 4%
# 
# ````{margin} 
# ```{admonition} Hinweis
# :class: note
# Der Kapitalbarwert ([hier](https://de.wikipedia.org/wiki/Kapitalwert)) lässt sich berechnen als die Summe der Barwerte der einzelnen Ein- und Auszahlungen. 
# 
# $$KW_0 = \sum_{t=0}^{T} \frac{CF_t}{(1+i)^t}$$
# ```
# ````
# 
# Wir suchen den Kapitalbarwert ($KW_0$) der Investition und können dies mit untenstehendem Code umsetzen.
# 
# 

# In[13]:


I_0 = -10000
CF_1 = 5000
CF_2 = 4000
CF_3 = 3000
i = 0.04
KW = I_0 + CF_1/(1+i)**1 + CF_2/(1+i)**2 + CF_3/(1+i)**3
KW


# Die Umsetzung war einfach und hat viele Vorteile gegenüber einer Variante, in der wir keine Variablen nutzen. Jedoch hat der bis hierin vorgestellte Ansatz immer noch relativ viele Nachteile, z.B.:
# 
# 1. jeder Cashflow benötigt eine eigene Variable. Bei großen Zahlenreihen ist dies viel manueller Aufwand (und auch fehleranfällig)
# 
# 2. die Formel für den Kapitalwert muss für jeden zusätzlichen Cashflow angepasst
# 
# 
# Im Folgenden wollen wir versuchen unseren Code Schritt für Schritt zu verbessern bzw. zu optimieren. 

# ### Wichtige Regeln in Python

# [to come]
# 
# 1. Einrücken / Leerzeichen haben eine Bedeutung
# 
# 2. Lange Zeilen kann ich unterbrechen mit `\` oder durch `( )`
# 
# 3. Hilfe durch ??

# ### Datentypen

# Jede Variable kann unterschiedliche Datentypen annehmen. In unseren obigen Beispielen haben wir bereits einige kennengelernt. 
# 
# 1. Die Variable `zahl` hat den Wert `42` angenommen. `42` ist vom Typ `integer`, d.h. eine Ganzzahl
# 2. Die Variablen `wort` und `satz` sind vom Typ `str`, d.h. ein Text
# 3. Die Variable `KW` ist vom Typ `float`, d.h. eine Dezimalzahl
# 
# Wir können den Datentyp einer Variable feststellen, in dem wir `type` nutzen. 
# 
# Beispiel:

# In[18]:


a = 42
type(a)


# In[19]:


a = 42.0 
type(a)


# 
# 
# Für das Programm bzw. den Computer, aber auch für uns als Datenanalyst oder Programmierer, sind Datentypen aus unterschiedlichen Gründen wichtig: 
# 
# **1. Speichplatz des Datentyps**  
# 
# Jeder Datentyp benötigt unterschiedlich viel Speicher. So macht es für den Computer einen Unterschied, ob wir `42` oder `42.0` schreiben, da er für diese Variablen unterschiedlich viel Speicherplatz "freimacht". Im Rahmen unserer Beispiele ist der Unterschied nicht von Bedeutung. Jedoch kann die Nutzung von Datentypen, die weniger Speicherplatz benötigen sinnvoll sein, wenn wir mit großen Datenmengen umgehen wollen. Im Rahmen dieses Kurses ist das Speicherargument jedoch nicht von großer Bedeutung. 
# 
# **2. Fähigkeiten des Datentyps**  
# 
# Jeder Datentyp hat unterschiedliche "Fähigkeiten".[^3] Wir haben z.B. nicht weiter hinterfragt (bzw. es ist für uns intuitiv und logisch), dass wir die Operation "`+`" mit den Datentypen `integer` und `float` nutzen können. Wir kennen das aus der Mathematik, von Excel oder unserem Taschenrechner. In einer Programmiersprache muss diese "Fähigkeit" jedoch "hinterlegt" sein, d.h. es muss festgelegt sein, dass dies möglich ist. Andersherum können für andere Datentypen jede Art von Fähigkeit hinterlegen - wir werden in den weiteren Kapiteln noch viele dieser Fähigkeiten kennenlernen. 
# 
# [^3]: Sie können die "hinterlegten Fähigkeiten" ausgeben lassen (via: `dir(variable)`). Die Ausgabe ist für Programmieranfänger jedoch zunächst eher verwirrend und wenig hilfreich, weshalb wir an dieser Stelle nicht weiter darauf eingehen werden. 
# 
# Beispiel: für uns macht die Operation `"Text 1"` + `"Text 2"` wenig Sinn. Die Addition von zwei Texten (hier: vom Datentyp `str`) ergibt mathematisch keinen Sinn. Dennoch ist diese Operation in Python ohne Probleme möglich, weil diese - aus verschiedenen Gründen - hinterlegt ist. 
# 

# In[22]:


text1 = "Vorname "
text2 = "Nachname"
text1 + text2


# Die Addition von zwei Texten verbindet die beiden Texte zu einem Text.
# 
# **3. Eignung des Datentyps** 
# 
# Nicht jeder Datentyp ist für jede Fragestellung sinnvoll einsetzbar. So macht es keinen Sinn, dass wir Variablen, die für Berechnungen genutzt werden sollen z.B. als `str` definieren. Hierdurch können sich Fehler in das Programm einschleichen ohne dass wir vor einem Fehler gewarnt werden. 
# 
# Beispiel:

# 

# In[23]:


zahl1 = "1"
zahl2 = "2"
ergebnis = zahl1 + zahl2
ergebnis


# Die Operation ist in Python erlaubt und liefert uns deshalb keinen Fehler. In unserem Fall macht das Ergebnis jedoch keinen Sinn..
# 
# Wir müssen also darauf achten, dass wir Datentypen nutzen, die für unsere Fragestellung sinnvoll sind. Außerdem müssen wir uns immer fragen, ob die Nutzung von anderen Datentypen unser Programm verbessern.
# 
# Lassen Sie uns deshalb unser Kapitalwert-Beispiel aufgreifen und andere (neue) Datentypen mit weiteren Fähigkeiten kennenlernen. 
# 
# 

# #### Listen
# 
# Der Datentyp `list` (Liste) kann beliebig viele Variablen enhalten und wird mit "`[ ]`" erzeugt.
# 
# Beispiel:

# In[40]:


zahlen = [1,14, 3, 11]
zahlen


# Auf die einzelnen Elemente der Liste (hier: Variable `zahlen`) kann dann mittels eines Index zugegriffen werden:

# In[41]:


zahl1 = zahlen[0]
zahl1


# In[42]:


zahl2 = zahlen[1] 
zahl2


# ```{admonition} Index
# :class: warning
# Der Index beginnt in Python bei allen Datentypen, die mehrere Elemente beinhalten, immer mit `0`. D.h. das erste Element befindet sich immer an Position `0` und NICHT an Position `1`. 
# ```

# Listen haben verschiedene Fähigkeiten. Viele dieser Fähigkeiten (in diesem Falle sprechen wir von Methoden) können sie aufrufen, in dem "`.`" drücken. 
# 
# Beispiel: sortieren einer Liste erfolgt via "`.sort()`"

# In[43]:


zahlen.sort()
zahlen


# In Jupyter Notebooks und in Google Colab können Sie via `tab completion`, d.h. "`.`" + `tab` alle dieser Methoden anzeigen lassen. Hinweis: teilweise müssen Sie runterscrollen, um weitere Methoden anzeigen zu lassen. 
# 
# ![tab](../assets/liste_tab.png)

# Wir können unser Beispiel signifikant vereinfachen, in dem wir den Datentyp `list` nutzen, welcher alle unsere Cashflows umfasst. 

# In[44]:


cash_flows = [-10000, 5000, 4000, 3000]
i = 0.04
KW = cash_flows[0] + cash_flows[1]/(1+i)**1 + cash_flows[2]/(1+i)**2 + cash_flows[3]/(1+i)**3
KW


# #### Dictionary

# Ein weiterer sehr nützlicher Datentyp in Python ist das sog. Dictionary (`dict`). Dieses können wir uns vorstellen, wie ein tatsächliches Wörterbuch. Wir können hier zu jedem Element ein passendes anderes Element abspeichern. Ein Dictionary wird mit "`{}`" erzeugt. Die sogenannten `key:value`-Paare werden dann im Dictionary gespeichert und können von unterschiedlichen Datentypen sein und werden via `[key]` abgerufen. 
# 
# Beispiel:

# In[50]:


my_first_dict = {"Begrüßung": "Hallo", "liste_zahlen": [1,2,3,4], 2: 4.32}


# In[51]:


my_first_dict["Begrüßung"]


# In[52]:


my_first_dict["liste_zahlen"]


# In[55]:


my_first_dict[2] # Hier ist `2` kein Index, sondern ein sogenannte Schlüssel (engl. `Key``)


# Auch hier können wir via `tab completion`, d.h. "`.`" + `tab` alle Methoden anzeigen lassen.
# 
# ![tab_dict](../assets/tab_dict.png)

# Dictionaries eignen sich hervorragend, um Parameter und Annahmen zu speichern. Wir können unser Beispiel also weiterfassen und z.B. zwei verschiedene Szenarien rechnen:

# In[61]:


# Szenarien und Annahmen
cf_szenario = {"base": [-10000, 5000, 4000, 3000], 
            "high": [-10000, 6000, 5000, 4000],
            "low": [-10000, 4000, 3000, 1000],}
i = 0.04


# In[62]:


cash_flows = cf_szenario["base"]
KW = cash_flows[0] + cash_flows[1]/(1+i)**1 + cash_flows[2]/(1+i)**2 + cash_flows[3]/(1+i)**3
KW


# In[65]:


cash_flows = cf_szenario["high"]
KW = cash_flows[0] + cash_flows[1]/(1+i)**1 + cash_flows[2]/(1+i)**2 + cash_flows[3]/(1+i)**3
KW


# ### Zusammenfassung und Ausblick
# 
# Wir haben unsere ersten Zeilen programmiert und dabei unsere Beispielaufgabe Schritt für Schritt verändert und optimiert. Dabei haben wir folgende Dinge gelernt:
# 
# 1. einfache mathematische Operationen können in Python genutzt werden
# 
# 2. es gibt einige wenige Regeln, die wir beachten müssen, um keine "technischen" Fehler zu produzieren; insbesonder müssen wir darauf achten, dass wir keine Leerzeichen an den falschen Stellen setzen
# 
# 3. es gibt unterschiedliche Datentypen, die wir für unsere Analysen nutzen können und sollten. Nicht jeder Datentyp ist für jede Art der Problem geignet. Wir haben bisher `int`, `float`, `str`, `list` und `dict` kennengelernt. Bei diesen Datentypen handelt es sich um solche, die bereits standardmäßig in Python integriert sind (sog. `build-in types`[^4]). Wir werden im weiteren Verlauf noch sehr viel mächtigere Datentypen kennenlernen, die wir explizit für die Zwecke der Datenanalyse entwickelt wurden und sehr hilfreiche "Fähigkeiten" haben. 
# 
# Im folgenden Kapitel werden wir unser Beispiel weiter optimieren. Denn - so ehrlich müssen wir sein - unsere bisherige Optimierung lässt noch keinen großen Vorteil gegenüber einem Taschenrechner und insbesondere nicht gegenüber Excel erkennen.
# 
# [^4]: siehe [hier](https://docs.python.org/3/library/stdtypes.html) für weitere Informationen zu den `build-in types`. 

# 
