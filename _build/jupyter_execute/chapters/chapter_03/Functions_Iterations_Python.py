#!/usr/bin/env python
# coding: utf-8

# # Iterationen und Funktionen

# Wir haben im [vorherigen Kapitel](../chapter_03/Intro_Python.ipynb) festgestellt, dass der von uns teilweise verbesserte Code immer noch sehr repetitiv ist. Dafür gab es zwei Gründe
# 
# 1. Der Code ist repetitiv, d.h. Wiederholungen von sehr ähnlichen Dingen
# 
# 2. Der Code ist unflexibel, d.h. bei kleinen Veränderungen der Fragestellung bereits unbrauchbar
# 
# Wir werden in diesem Kapitel zwei wichtige Coding-Konzepte vorstellen, die uns helfen, den Code weiter zu verbessern und die angesprochenen Probleme des bisherigen Codes zu verbessern. 
# 
# Wir beginnen mit dem Konzept der `Funktionen`, bevor wir uns dem Konzept der `Iterationen` widmen.
# 

# ## Funktionen (build-in)

# Wir können Funktionen einsetzen, um Teile des Codes wiederverwendbar zu machen bzw. um bereits geschriebenen Code von anderen wiederzuverwenden. Das Konzept ist sehr mächtig und wir werden sowohl bereits implementierte Funktionen nutzen, als auch eigene Funktionen schreiben lernen. 
# 
# Lassen Sie uns wieder eine Analogie aus Excel nutzen. Stellen Sie sich vor, wir haben eine Spalte mit vielen Werten und wir wollen wissen, um wieviele Werte es sich handelt, d.h. wir wollen die `Anzahl` an Werten bestimmen. Wir könnten diese Information z.B. benötigen, um einen Durchschnitt zu berechnen. 
# 
# ![Zahlen](../assets/RndNumbers.png)

# Natürlich könnten wir die Anzahl an Werten selber und manuell zählen (es sind 10 Werte). Diese Lösung ist aber wenig sinnvoll, da wir so einen manuellen Schritt in unser "Programm" einbauen. Besser wäre es, wenn wir die Anzahl an Werten automatisiert bestimmen. Wir könnten uns über diese eigentlich triviale Aufgabe nun Gedanken machen. Jedoch müssen wir dies nicht, da es für diese spezielle Frage bereits eine Lösung in Excel gibt. Wir können die Funktion `Anzahl()` nutzen, die Excel bzw. Microsoft bereits für den Anwender zur Verfügung gestellt hat. Die Funktion berechnet, wie viele Zellen in einem Bereich Zahlen enthalten. 
# 
# ![Werte2](../assets/RndNumbers_Solution.png)
# 

# Ein Großteil der Funktionalität von Excel geht auf die breite Palette an bereits verfügbaren Funktionen zurück. 
# 
# Schauen wir uns nun das Äquivalent in Python an. Wir können die Anzahl an Elementen in z.B. einer Liste über die Funktion `len` ermitteln. 
# 
# **Beispiel**

# In[67]:


werte = [10, 12, 13, 12, 5, 4, 2] # Liste mit Werten
len(werte) # Gibt die Anzahl an Elementen in der Liste "werte" zurück


# Zum Aufrufen einer Funktion benötigen wir in Python 
# 
# - den Namen der Funktion
# - die benötigten Parameter für die Funktion
# 
# Der Name der Funktion lautet `len`. Die Funktion wird dann aber erst ausgeführt (bzw. aufgerufen), in dem der Funktion die benötigten Parameter übergeben werden. Bei der Funktion `len` ist dies z.B. eine Liste, deren Anzahl an Elementen bestimmt werden soll. 
# 
# Wenn wir eine bestehende Funktion nutzen wollen, schreiben wir also immer:
# 
# ```
# <funktionsname>(<parameter>, ...)
# ```
# 
# Die "`...`" stehen hier für weitere Parameter, die ggf. für eine Funktion benötigt werden. Das Vorgehen ist also prinzipiell sehr ähnlich zum Vorgehen bei Excel. 

# ```{admonition} Hilfe zu Funktionen
# :class: tip, dropdown
# Wir können zu nahezu allen Funktionen Hilfe nachschlagen. 
# 
# Dies machen wir entweder, in dem wir ein "`?`" hinter die Funktion schreiben. Wenn Sie z.B. wissen wollen, was die Funktion `len` tut, dann schreiben Sie in eine Code-Zelle `len?` und Ihnen werden Erläuterungen dazu angezeigt.
# 
# In einem Jupyter Notebook können Sie alternativ auch den Funktionsnamen + "`()`" und dann einmal `shift` + `tab` drücken. 
# 
# Darüber hinaus können Sie sich noch die Dokumentation von Funktionen anschauen, die Sie meist online finden werden. 
# ```

# In Python gibt es viele Funktionen, die wir nutzen können, um uns eigenen Programmieraufwand zu sparen. Die vollständige Liste aller sog. build-in Funktionen kann [hier](https://www.w3schools.com/python/python_ref_functions.asp) nachgeschlagen werden. Hierbei handelt es sich jedoch nur um Funktionen, die bereits in Python enthalten sind. Darüber hinaus können wir andere Bibliotheken installieren, um das Spektrum signifikant zu erweitern; dies werden wir in den nächsten Kapiteln auch tun.   

# ## Iterationen

# Das Wiederholen von identischen oder sehr ähnlichen Code-Ausschnitten ist aufwändig und fehleranfällig und sollte deshalb nicht vom Menschen, sondern vom Computer übernommen werden. 
# 
# Auch an dieser Stelle wollen wir uns wieder einer Analogie aus Excel bedienen. Die Stärke von Excel ist unter anderem dadurch begründet, dass wir Operationen vielfach durchführen können, ohne diese mehrfach sexplizit formuliert zu haben. Wir können stattdessen einmal formulierte Operationen "nach unten" oder "zur Seite ziehen". Dadurch kann eine Operation automatisch für eine andere Zelle angewandt werden. 
# 
# Hier ein Beispiel in Excel, die eine Formel für viele Zellen anwendet.
# 
# ![xls-for-loop](../assets/xls_for_loop.gif)
# 
# Das Beispiel zeigt, dass wir dadurch viel manuellen Aufwand, aber auch viele potenzielle Fehlerquellen vermeiden. 
# 
# Auch viele Programmiersprachen haben deshalb Konzepte, um diese Wiederholungen zu vermeiden. Wir werden uns nun zwei Konzepten in Python widmen:
# 
# 1. For-Loops
#    
# 2. List comprehensions
# 

# ### For-Loops

# Mit einer `For-Loop` können wir (iterierbare) Datentypen durchlaufen. Schauen wir uns ein Beispiel an, um zu verdeutlichen, was damit gemeint ist. 
# 
# **Beispiel**

# In[68]:


liste_namen = ["Julia", "Aishe", "Fred", "John"]
for name in liste_namen:
    print("Hallo", name)


# Das Äquivalent in Excel würde wiefolgt aussehen:
# 
# ![xls-for-loop2](../assets/xls_for_loop2.gif)

# Im obigen Python-Beispiel definieren wir eine Variabel `liste_namen`. Diese ist vom Datentyp `list`. Listen sind in Python immer iterierbar, d.h. wir können diese mittels einer `for-loop` durchlaufen. Wir tun dies in dem wir schreiben 
# 
# `for <name> in <liste_name>:`
# 
# Dies zeigt Python an, dass wir die Liste `liste_namen` durchlaufen wollen und für jedes Element - wir bezeichnen es hier als `name` - etwas tun möchten. Unter dieser Definition schreiben wir dann - eingerückt mit `4 Leerzeichen` bzw. `tab` - , was wir konkret tun möchten. In unserem Falle wollen wir nur etwas ausgeben lassen. Hierfür nutzen wir eine der build-in Funktionen (`print`). Wenn wir Zwischenergebnisse innerhalb einer `for-loop` nicht in Variabeln "abspeichern", sondern nur anzeigen lassen wollen, müssen wir immer die (build-in) Funktion `print` nutzen.  

# Jede For-Schleife in Python hat also immer die folgende grundsätzliche Strukur:
# 
#     >>> for <element> in <objekt>:
#             mach irgendetwas
#         
# Hierbei muss `objekt` iterierbar sein. `element` können wir uns als eine Art Platzhalter für das jeweilige Element vorstellen. Wir können hier auch jeden anderen Namen wählen. Wir sollten uns jedoch angewöhnen sinnvolle und beschreibende Namen zu wählen. 

# Lassen Sie uns unser neu gewonnenes Wissen kombinieren und folgende Aufgabe in Python lösen. 
# 
# **Aufgabe:**  
# Wir haben eine Liste mit Namen und wollen bestimmen, wieviel Buchstaben jeder Name hat. 
# 
# **Lösung**  
# Wir können dafür die Liste der Namen durchlaufen und für jedes Element der Liste, die Länge des Namen mit der Funktion `len` bestimmen. 

# In[69]:


namen = ["Julia", "Aishe", "Fred", "Schwerthelm", "John", "Manuela"]

for name in namen:
    n_buchstaben = len(name) # Bestimme Anzahl an Element in Namen
    print(name, n_buchstaben) # Gib Anzahl aus


# Alternativ könnten wir die Länge der Buchstaben auch in einer neuen Liste speichern - dies ist immer dann sinnvoll, wenn wir die Zwischenergebnisse später in unserem Code noch benötigen. 
# 
# **Beispiel**  
# Wir erstellen dafür eine leere Liste ("`[]`"), die wir dann mit jeder Iteration mit der Anzahl an Buchstaben befüllen. Dafür benutzen wir die "Funktion" `.append`, die der Datentyp `list` bereitstellt. 

# In[70]:


namen = ["Julia", "Aishe", "Fred", "Schwerthelm", "John", "Manuela"]
anzahl_buchstaben = [] # Leere Liste
for name in namen:
    n_buchstaben = len(name) # Bestimme Anzahl an Element in Namen
    anzahl_buchstaben.append(n_buchstaben) # 

# Ausgabe der neuen Liste
anzahl_buchstaben


# 
# 
# ````{admonition} enumerate
# :class: tip
# Wir können mittels der (build-in) Funktion `enumerate` zusätzlich zum einzelnen Element der Liste auch die Position des Elements in der Liste ausgeben lassen. Wir generieren dadurch eine Art Zähler.
# 
# ```{code} Python
# zahlen = [12, 14, 230]
# for i, zahl in enumerate(zahlen):
#     print(i, zahl)
# >>> 0 12
# >>> 1 14
# >>> 2 230
# ```
# 
# ````

# ### List comprehension

# Eine Besonderheit in Python sind die sog. `list comprehensions`. Mit diesen können die Ergebnisse einer `for-loop` direkt in einer neuen Liste abgespeichert werden.[^1]
# 
# Wir können das obige Beispiel mit dem Konzept der `list comprehension` einfacher und kompakter darstellen. 
# 
# [^1]: Hinweis: wir können innerhalb der `list comprehension` auch noch mehr machen. Dies werden wir in den nächsten Kapiteln noch sehen. 

# In[71]:


namen = ["Julia", "Aishe", "Fred", "Schwerthelm", "John", "Manuela"]
anzahl_buchstaben = [len(name) for name in namen]

# Ausgabe der neuen Liste
anzahl_buchstaben


# ```
# >>> [mach irgendetwas for <element> in <objekt>]
# ```

# In Python werden - wenn möglich - typischerweise `list comprehension` bevorzugt, da dies den Code insgesamt übersichtlicher und lesbarer macht. 

# ## Optimierung des Beispiels

# Wir haben nun das nötige Wissen, um unser Ausgangsbeispiel signifikant zu optimieren. Schauen wir uns dafür nochmal einen Ausschnitt unseres Codes an. 

# In[72]:


# Annahmen im Base Case
i = 0.04
cash_flows = [-10000, 5000, 4000, 3000] 

KW = cash_flows[0] + cash_flows[1]/(1+i)**1 + cash_flows[2]/(1+i)**2 + cash_flows[3]/(1+i)**3
KW


# Wie können wir den Code nun optimieren? Schauen wir uns den Code genauer an, dann stellen wir fest, dass 
# 
# 1. wir die Berechnung einzelnen Barwerte insgesamt 4 Mal wiederholen, d.h. wir schreiben zu jedem Zeitpunkt $\frac{CF_t}{(1+i)^t}.
# 
# 2. wir summieren die berechneten Barwerte auf, in dem wir jeweils "`+`" schreiben. 
# 
# Wir können den Code nun verbessern, in dem wir für die Berechnung der einzelnen Barwerte eine `for-loop` bzw. eine `list comprehension` nutzen. Dadurch vermeiden wir repetitiven Code. Die Addition der einzelnen Barwerte können wir dann über die Funktion `sum` durchführen. Dadurch machen wir unseren Code flexibler z.B. für den Fall, wenn ein Projekt weniger oder mehr Cashflows beinhaltet. 
# 
# Hier der Code in zwei einzelnen Schritten
# 
# 1. Berechnung der Barwerte
# 
# 2. Summierung der Barwerte
# 
# 
# 

# In[73]:


# Annahmen im Base Case
i = 0.04
cash_flows = [-10000, 5000, 4000, 3000] 


# In[74]:



# Berechnung der Barwerte und speichern in neuer Liste
barwerte = [cf/(1+i)**t for t, cf in enumerate(cash_flows)]

# Berechnung der Summe der Barwerte
KW = sum(barwerte)
KW


# Wir können sogar noch einen Schritt weitergehen und beide Berechnung zusammenführen.

# In[75]:


KW = sum([cf/(1+i)**t for t, cf in enumerate(cash_flows)])
KW


# Die optimierte Lösung ist sehr viel kompakter und funktioniert auch für jede beliebige andere Anzahl an Cashflows, d.h. wir haben einen Lösungsansatz gefunden, der für eine beliebige Anzahl an Cash Flows und einen anzugebenden Zinssatz den Kapitalwert berechnet. 

# ## Definition von eigenen Funktionen

# Wir haben uns bereits einige Funktionen angeschaut, die von Python bereitgestellt werden. Lassen Sie uns nun damit beschäftigen, wie wir eigene Funktionen schreiben. Bevor wir dies tun wollen wir jedoch kurz darauf eingehen, weshalb dies sinnvoll ist. Aus unserer Sicht gibt es zwei gute Gründe, weshalb wir eigene Funktionen schreiben sollten. Zum einen macht dies den Code lesbarer und zum anderen führt dies zu weniger repetitivem und damit kompakteren Code. 
# 
# 
# [HINWEIS: WARUM REITEN WIR AUF LESBARKEIT VON CODE RUM -> unser zukunftiges Ich wird Code oft nicht mehr verstehen und kann diesen deshalb nicht anpassen]
# 
# 
# Nehmen wir unser Beispiel der Bewertung eines Projektes. Stellen wir uns vor, dass wir nun für alle drei Szenarien den Kapitalwert ermitteln wollen.[^2]  
# 
# [^2]: an dieser Stelle der Hinweis, dass sich hierfür Excel vermutlich besser eignet, wir dieses Beispiel aus didaktischen Gründen aber fortführen werden. 
# 
# Der Code dafür könnte wiefolgt aussehen:
# 

# In[76]:


# Annahmen im Base Case
i = 0.04
cf_szenario = {"base": [-10000, 5000, 4000, 3000], 
            "high": [-10000, 6000, 5000, 4000],
            "low": [-10000, 4000, 3000, 1000],}

# Kapitalwert Szenario 1
cash_flows = cf_szenario["base"]
KW_base = sum([cf/(1+i)**t for t, cf in enumerate(cash_flows)])

# Kapitalwert Szenario 2
cash_flows = cf_szenario["high"]
KW_high = sum([cf/(1+i)**t for t, cf in enumerate(cash_flows)])


# Kapitalwert Szenario 3
cash_flows = cf_szenario["low"]
KW_low = sum([cf/(1+i)**t for t, cf in enumerate(cash_flows)])


# Wir stellen fest, dass der Code wieder sehr repetitiv ist. Wir könnten die jeweiligen Berechnungen deshalb z.B. in eine `for-loop` verlagen. Das sähe dann so aus:
# 
# (code:long)=

# In[77]:


szenarien = ["base", "high", "low"]
ergebnisse = []

for szenario in szenarien:
    cash_flows = cf_szenario[szenario]
    KW = sum([cf/(1+i)**t for t, cf in enumerate(cash_flows)])
    ergebnisse.append(KW)

ergebnisse


# Der Code sieht schon kompakter aus. Was aber, wenn wir weitere Projekte bewerten wollen? Wir müssten diesen Code mehrmals nutzen, um die jeweiligen Projekte zu bewerten. Genau für ein solches Szenario bietet sich an, die Funktionalität des Codes in eine eigene Funktion auszulagern. Wir müssten dann immer nur die Funktion aufrufen und nicht die vielen Zeilen Code wiederholen. 
# 
# Schauen wir uns an, wie wir Funktionen in Python schreiben. In Python ist jede Funktion wie folgt aufgebaut:
# ```
# >>> def funcname(parameter, ...):
#         mach irgendetwas
#         return ergebnis
# ```
# 
# Jede Funktion beginnt mit dem Wort "`def`" und einem Namen für die Funktion. Diesen können wir frei wählen. Der Name sollte beschreiben, was die Funktion tut. Darüber hinaus geben wir an, welche Informationen bzw. welche `parameter` die Funktion benötigt. Im inneren der Funktion definieren wir dann, was die Funktion tut. Das Ergebnis der Funktion wird dann via `return` ausgegeben. 
# 
# Sobald eine Funktion definiert ist, kann diese überall im Programm genutzt werden, indem diese über "`()`" aufgerufen wird. 
# 
# Schauen wir uns **zwei einfache Beispiele** an:

# In[78]:


# Definition der Funktion "begrüßung", diese hat benötigt keinen Parameter
def begrüßung():
    return "Herzlich Willkommen!"

begrüßung()


# In[79]:


# Definition der Funktion "addition"; diese benötigt zwei Parameter
def addition(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

# Ausführen der Funktion "addition"
addition(3,55)


# Es ist sehr einfach, in Python eigene Funktionen zu definieren. Wir sollten deshalb auch - wenn es sinnvoll erscheint - davon gebrauch machen. Schauen wir uns an, wie wir die Kapitalwertberechnung in eine Funktion "auslagern" können. 
# 
# Wir müssen uns Gedanken machen zu verschiedenen Dingen:
# 
# 1. Wie soll die Funktion heißen (Funktionsname)
# 2. Welche Informationen benötigt die Funktion (Funktionsparameter)
# 3. Welche Berechnungen soll die Funktion im inneren Durchführen (Funktionsinhalt)
# 4. Was soll die Funktion ausgeben (Funktionsoutput)
# 
# Für 1.: sollten wir einen Namen wählen, der beschreibt, was die Funktion macht. Wir wählen also z.B. `berechne_kapitalwert`. An dieser Stelle der Hinweis, dass es sehr üblich ist in englischer Sprache zu coden, d.h. für Variabeln und Funktionen englische Begriffe zu wählen. 
# 
# Für 2.: wir benötigen Cash Flows und Zinssatz, um die Berechnungen durchzuführen. 
# 
# Für 3: den Code zur Berechnung des Kapitalwertes haben wir bereits geschrieben. Dies ist auch ein sehr übliches Vorgehen. Wir schreiben Code, probieren aus etc. Sobald wir merken, dass der Code funktioniert und ausgelagert werden könnte, beginnen wir diesen in Funktionen auszulagern. 
# 
# Für 4: die Funktion sollten den Kapitalwert als Ergebnis ausgeben.
# 
# Der Code für unsere erste eigene Funktion könnnte also z.B. so aussehen:

# In[80]:


def berechne_kapitalwert(cashflows, zins):
    KW = sum([cf/(1+zins)**t for t, cf in enumerate(cashflows)])
    return KW


# Wir können unsere Funktion nun testen, in dem wir für `cashflows` und `zins` Werte einsetzen und die Funktion aufrufen. Wir können dies auf verschiedene Weise machen. Hier ein paar Beispiele, die funktionieren.

# **Beispiel 1: ohne vorherige Definition der Input-Variablen**

# In[81]:


berechne_kapitalwert([-100, 50,50], 0.3)


# **Beispiel 2: mit vorherige Definition der Input-Variablen**
# 
# Wichtig: die Namen der Variablen müssen nicht mit den Parameternamen übereinstimmen

# In[82]:


cash = [-100, 50, 50]
r = 0.3
berechne_kapitalwert(cash, r)


# **Beispiel 3: mit Nennung der Parameter**
# 
# In den vorherigen Beispielen haben wir die Parameternamen nicht genannt, sondern unsere Daten nur in korrekter Reihenfolge eingegeben: 1. cashflows, 2. zins. 
# 
# Wir können jedoch alternativ auch die Parameternamen angeben (sog. Keyword Argument). 

# In[83]:


cash = [-100, 50, 50]
r = 0.3
berechne_kapitalwert(cashflows=cash, zins=r)


# Bei diesem Vorgehen ist die Reihenfolger der Parameter dann unerheblich.

# In[85]:


berechne_kapitalwert(zins=r, cashflows=cash)


# Schauen wir uns nun an, was der Vorteil der Auslagerung von Code-Teilen in Funktionen konkret ist. Wir werden dazu unsere drei Szenarien (siehe [hier](code:long)) 

# In[87]:


szenarien = ["base", "high", "low"]
ergebnisse = [berechne_kapitalwert(cf_szenario[szenario], i ) for szenario in szenarien]
ergebnisse


# Der Code ist wesentlich kompakter, weil wir das Kernstück - die Berechnung des Kapitalwertes - ausgelagert haben in eine Funktion. Auch ist der Code viel einfacher zu lesen. Wir sehen auf den ersten Blick, dass wr für verschiedene Szenarien die Funktion `berechne_kapitalwert` aufrufen. Was diese tut ist durch den gewählten Namen der Funktion fast intuitiv klar. 

# ````{admonition} Iterieren von Dictionaries
# :class: tip, dropdown
# Alternativ könnten wir das `dictionary` mit den Cashflow-Szenarien auch direkt in der `list comprehension` ansprechen. Dies ist möglich, weil ein `dictionary` wie eine Liste auch iterierbar ist. So können wir die drei Schlüssel (`key`) via `dict.keys()` und die Werte via `dict.values()` abrufen. Ersteres würde die Schlüssel "`base`", "`high`" und "`low`" liefern. Letzteres die entsprechenden Cashflows zu den Szenarien, d.h. "`[-10000, 5000, 4000, 3000]`", "`[-10000, 6000, 5000, 4000]`" und "`[-10000, 4000, 3000, 1000]`".
# 
# ```{code} python
# ergebnisse = [berechne_kapitalwert(cash, i ) for cash in cf_szenario.values()]
# ```
# 
# ````

# ## Zusammenfassung und Ausblick

# Wir haben unser Eingangsbeispiel signifikant verbessert, in dem wir uns zwei wichtige Konzepte der Programmierung bzw. in Python angeschaut haben. 
# 
# 1. Funktionen: sind eine sinnvolle Möglichkeit um wiederkehrenden Code auszulagern und wiederverwendbar zu machen. Wir können sowohl bereits existierende Funktionen nutzen, die andere für uns zur Verfügung stellen, als auch eigene Funktionen definieren. 
# 
# 2. Iterationen: wir haben das Konzept der `for-loops` und der `list comprehension` kennengelernt. Wir sollten dieses Konzept immer dann anwenden, wenn wir Code repetitiv anwenden. 
# 
# Mit dem bisher vorgestellten Konzepten können Sie bereits sehr mächtige Programme schreiben. Natürlich bedarf es einem gewissen Maß an Übung, um die Syntax zu lernen, aber auch um die Anwendungsfälle zu identifizieren. Gehen Sie deshalb die Übungen dieses Kapitels sorgfältig durch. 
# 
# Im nächsten Kapitel werden wir uns mit weiteren wichtigen Konzepten auseinandersetzen. 

# 
