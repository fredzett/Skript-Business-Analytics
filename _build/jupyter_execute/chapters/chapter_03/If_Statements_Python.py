#!/usr/bin/env python
# coding: utf-8

#  # Entscheidungsstrukturen

# In unserem Ausgangsbeispiel wollten wir berechnen, ob sich ein Projekt lohnt. Auch wenn wir im vorherigen Kapitel bereits viele Verbesserungen ggü. dem ursprünglichen Programm gemacht haben, so haben wir die eigentliche Frage noch nicht beantwortet. Dies wollen wir nun nachholen.
# 
# Die Frage, die wir untersuchen wollten und die unser Programm beantworten sollte, lautete: 
# 
# > "Lohnt es sich, die Investition zu tätigen?"
# 
# Die Antwort auf diese Frage ist theoretisch - und dies haben Sie spätestens im 3. Semester im Rahmen der Investitionsrechnung gelernt - simple zu beantworten:
# 
# Ist der Kapitalwert > 0, so lohnt sich eine Investition, da wir mit dieser "Wert schaffen", d.h. wir auf heute diskontiert mehr Cash-Rückflüsse generieren, als wir in Summe investieren. 
# 
# Es wäre also hilfreich, wenn unser Programm uns die Rückmeldung gäbe, ob der Kapitalwert größer 0 ist. Unser Programm müsste also in der Lage sein, folgende Analyse durchzuführen:
# 
# - Wenn Kapitalwert größer 0, dann gib positive Rückmeldung (z.B. "das Projekt ist super!")
# - Wenn Kapitalwert kleiner oder gleich 0 dann gib negative Rückmeldung (z.B. "das Projekt ist schlecht! Finger weg")
# 
# Für eine solche Analyse benötigen wir das Konstrukt eines sog. "`if statement`". Schauen wir uns zunächst an, wie dieses Konstrukt in Python funktioniert und implementiert wird und es so dann auf unser Beispiel anwenden.
# 

# ## Einfache if-Statements

# In Python können wir "wenn-dann"-Konstrukte relativ einfach implementieren. 
# 
# Die einfachste Form des Konstruktes funktioniert in Python wiefolgt:
# 
# ```
# if <bedingung>:
#     <mach etwas>
# ```
# 
# **Beispiel 1:**

# In[35]:


zahl = 10
if zahl == 10:
    print("Eine 10!")


# **Beispiel 2:**

# In[36]:


zahl = 12
if zahl == 10:
    print("Eine 10!")


# Wir sehen, dass der Code scheinbar nichts macht. Dies liegt daran, dass die Bedingung (`zahl == 10`) in diesem Fall nicht erfüllt ist (weil: `zahl == 12`). Wir sollten also noch angeben, was wir für den Fall machen wollen, dass die Bedingung nicht erfüllt ist. Eine sog. Default-Bedingung. Dies machen wir mit dem `else`-Statement. Wir schreiben dann:
# 
# ```
# if <bedingung>:
#     <mach etwas> 
# else:
#     <mach etwas anderes>
# ```
# 
# **Beispiel:**

# In[37]:


zahl = 12
if zahl == 10:
    print("Eine 10!")
else:
    print("Keine 10!")


# Wir können `if-statements` natürlich auch in andere Konstrukte integrieren. Häufig verwenden wir ein solches Statement, um Entscheidungen für Listen (oder andere iterierbare Objekte) herbeizuführen. 
# 
# **Beispiel:**

# In[38]:


werte = [100, 0, 20, 300]
for el in werte:

    # einfache Wenn-Bedingung
    if el == 0:
        print("Wir habe eine 0 gefunden")


# Das "`if-statment`" beginnt immer mit dem Keyword `if` und wird gefolgt von einer Bedingung. In Python kann ich folgende logische Bedingungen abfragen:
# 
# - gleich: `a == b`; fragt ab, ob die Bedingung "a hat den gleichen Wert wie b" erfüllt ist
# - nicht gleich: `a != b`; fragt ab, ob die Bedingung "a hat nicht den gleichen Wert wie b" erfüllt ist
# - weniger als: `a < b`; fragt ab, ob die Bedingung "a ist kleiner als b" erfüllt ist
# - weniger oder gleich: `a <= b`; fragt ab, ob die Bedingung "a ist kleiner oder gleich b" erfüllt ist
# - größer als: `a > b`; fragt ab, ob die Bedingung "a ist größer als b" erfüllt ist
# - größer oder gleich: `a >= b`; fragt ab, ob die Bedingung "a ist größer oder gleich b" erfüllt ist
# 
# 
# ````{margin} 
# ```{admonition} Wichtig
# :class: warning
# Die gleich-Bedingung wird mit "`==`" abgefragt und nicht mit dem einfache "`=`"-Zeichen, da dieses bereits für die Zuweisung von Variabeln belegt ist!
# ```
# ````

# Schauen wir uns an, was das Ergebnis einer solchen Bedingung ist. 

# In[39]:


a = 3
b = 4
a == b


# In[40]:


a < b


# Das Ergebnis einer Bedingung ist immer `True` oder `False`. Wir haben es also mit einem neuen uns bisher noch nicht bekannten Datentyp zu tun. Das Ergebnis einer Bedingung liefert den Datentyp `bool` zurück; dieser kann nur die genannten Werte `true` und `false` annehmen. Der Datentyp ist sehr nützlich, weil wir - insbesondere auch in der Datenanalyse - oft Bedingungen prüfen müssen. 

# In[41]:


condition_result = a > b 
type(condition_result)


# Wir können mit dem Datentyp `bool` auch ganz normale Rechenoperationen durchführen. Dies stellt sich oft als nützlich heraus, wie wir noch feststellen werden. Python behandelt `True` wie eine 1 und `False` wie eine 0. 
# 
# **Beispiel:**

# In[42]:


bools = [True, False, True, False, False, False]
sum(bools)


# Wir können über die logischen Operatoren `and` und `or` auch verbinden. Wir könnten also z.B. abfragen:
# 
# > wenn bedingung1 erfüllt oder bedingung2 erfüllt, dann mache etwas
# 
# **Beispiel**

# In[43]:


for el in werte:
    if el == 0 or el == 20:
        print("Klasse! Der Wert beträgt 0 oder 20.")


# ## Komplexere if-statements

# Oft werden wir Probleme und Fragestellungen haben, bei denen die Wenn-Dann-Abfrage komplexer ist. Im obigen Beispiel liefert unser Code z.B. keine Antwort auf die Frage, ob eine 0 oder eine 20 gefunden wurde, sondern nur, dass einer der beiden Werte gefunden wurde. 
# 
# Es ist deshalb oft hilfreich mehrere Wenn-Dann-Abfragen zu verbinden. Dies können wir mit `elif` tun. 

# In[44]:


for el in werte:
    if el == 0:
        print("Wir haben eine 0 gefunden")
    elif el == 20:
        print("Wir haben eine 20 gefunden")
    else:
        print("Nix gefunden")


# ## List comprehsions und if statments
# 
# Wir können das Konstrukt der Wenn-Dann-Bedingungen auch im Rahmen einer `list comprehension` nutzen. Dies ist in Python sehr üblich und liest sich oft wesentlich kompakter. Ein häufiger Anwendungsfall ist das Filtern von Listen. 
# 
# **Beispiel:** 
# 
# Wir haben eine Liste mit Zahlen, benötigen aber nur die positiven Zahlen. 

# In[45]:


werte = [100, 200, 300, -100, 200, 20, 40, -10, 0, 12]
werte_positiv = [el for el in werte if el > 0]
werte_positiv


# **Beispiel:**
# 
# Wir haben eine Liste mit Wörtern und wollen Wörter, die ein bestimmtes Kriterium nicht erfüllen, aussortieren

# In[46]:


wörter = ["Umsatz", "Gewinn", "Preis", "Absatz"]
wörter_filtered = [el for el in wörter if "z" in el]
wörter_filtered


# Greifen wir nun unser Ausgangsbeispiel wieder auf und ergänzen dieses um eine Wenn-Dann-Abfrage. Hier zunächst die Code-Blöcke, die wir bereits implementiert hatten

# In[47]:


def berechne_kapitalwert(cashflows, zins):
    KW = sum([cf/(1+zins)**t for t, cf in enumerate(cashflows)])
    return KW


# In[48]:


# Annahmen im Base Case
i = 0.04
cf_szenario = {"base": [-10000, 5000, 4000, 3000], 
            "high": [-10000, 6000, 5000, 4000],
            "low": [-10000, 4000, 3000, 1000],}

szenarien = ["base", "high", "low"]
ergebnisse = [berechne_kapitalwert(cf_szenario[szenario], i ) for szenario in szenarien]
ergebnisse


# In unserem Beispiel haben wir drei Szenarien, die alle drei eintreten könnten. Wir könnten diese mit Wahrscheinlichkeiten gewichten und eine Art Erwartungswert berechnen. Wir werden dann mit einer Wenn-Dann-Abfrage, checken, ob der Erwartungswert > 0 ist und sich die Investition lohnt.

# In[49]:


wahrscheinlichkeiten = [0.5, 0.1, 0.4] # Wahrscheinlichkeiten für Szenarien
erwartungswert = sum([p*kw for p, kw in zip(wahrscheinlichkeiten, ergebnisse)])
if erwartungswert > 0:
    print("Investition ist gut! Der EW beträgt", erwartungswert)
else:
    print("Die Investition ist schlecht. Der EW beträgt", erwartungswert)


# Der Code beinhaltet nun alles, was wir zur Lösung unserer Fragestellung benötigen. Lassen Sie uns diesen nun noch einmal optimieren, so dass wir diesen schnell adaptieren könnten, falls sich Annahmen änderten (z.B. anderer Zinssatz oder andere Wahrscheinlichkeiten). Wir machen dies in drei Schritten:
# 
# 
# 1. Wir lagern die Berechnung des Erwartungswertes in eine separate Funktion aus
# 2. Wir lagern die Wenn-Dann-Abfrage in eine Funktion aus
# 3. Wir schreiben eine Funktion für die gesamte Analyse, in der wir alle Einzelfunktionen nutzen

# In[50]:


def calc_erwartungswert(kapitalwerte, probs):
    erwartungswert = sum([p*kw for p, kw in zip(probs, kapitalwerte)])
    return erwartungswert

def print_result(erwartungswert):
    if erwartungswert > 0:
        print("Investition ist gut! Der EW beträgt", erwartungswert)
    else:
        print("Die Investition ist schlecht. Der EW beträgt", erwartungswert)


# In[51]:


def check_investment(cash_szenarien, i, probs):
    
    # 1. Schritt: Kapitalwerte der Szenarien berechnen
    kapitalwerte = [berechne_kapitalwert(cashflows, i ) for cashflows in cash_szenarien.values()]

    # 2. Schritt: Erwartungswert der Kapitalwerte berechnen (d.h. mit Wahrscheinlichkeiten gewichten)
    erwartungswert = calc_erwartungswert(kapitalwerte, probs)

    # 3. Schritt: Wenn-Dann-Abfrage, ob Erwartungswert (EW) > 0
    print_result(erwartungswert)


# Unsere gesamte Analyse erstreckt sich jetzt auf folgenden Code:

# In[52]:


i = 0.04
cf_szenario = {"base": [-10000, 5000, 4000, 3000], 
            "high": [-10000, 6000, 5000, 4000],
            "low": [-10000, 4000, 3000, 1000],}
probs = [0.5, 0.1, 0.4]
check_investment(cf_szenario, i, probs)


# Der gesamte Code ist jetzt hierarchisch aufgebaut. Die eigentliche Analyse erfolgt in einer Zeile (`check_investment(...)`). Um zu sehen, was diese Funktion tut, können wir uns diese anschauen und sehen, dass diese drei Funktionen aufruft. Diese können wir uns dann wieder im Detail anschauen etc. Dieses Vorgehen erleichtert es unseren Code les- und handhabbar zu machen. Wir können auch in 3 Monaten noch nachvollziehen, was unser Code macht und könnten Fehler schnell finden. 

# ## Fazit

# Wir sind einen großen Schritt gegangen und haben bereits wesentliche Konstrukte in Python kennengelernt, um komplexe Programme zu schreiben. 
# 
# - Mit der Einführung von Wenn-Dann-Abfragen, können Sie nun den Computer vordefinierte Entscheidungen durchlaufen lassen. 
# 
# - wir haben bei der Optimierung gesehen, dass wir Code - wenn sinnvoll - in Funktionen auslagern sollten, um diesen lesbarer zu machen. 
# 
# In den nächsten Kapiteln werden wir uns nun mit dem Importieren von externen Modulen beschäftigen, die uns viele wichtige Funktionen für eine ernsthafte Datenanalyse geben werden. Es ist jedoch wichtig, dass sie das bisher vorgestellte üben und nachvollziehen, um die weiteren Kapitel gut verfolgen zu können. 
