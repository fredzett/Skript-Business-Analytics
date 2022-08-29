#!/usr/bin/env python
# coding: utf-8

# # Umsetzung in Python

# ## Vorarbeiten
# 
# Bevor wir loslegen, müssen zunächst Module importiert werden, die wir im Rahmen der Analyse benötigen. Im Kapitel [TO COME]() werden wir die Hintergründe hierzu erläutern. Python (wie die meistern Programmiersprachen) wird von Hause aus weitestgehend ohne Funktionalität für Datenanalyse oder Visualisierung bereitstellt. Die dafür benötigten Funktionen können dann jedoch via sogenannter Module importiert werden. Die einzelnen Module werden im weiteren Verlaufe des Skriptes bzw. der Lehrveranstaltung eingeführt und erläutert. 

# In[19]:


# Modul `BusinessAnalytics` muss bei erster Nutzung zunächst installiert werden:
#  - google colab: via `!pip install BusinessAnalytics`
#  - jupyter notebook: via `%pip install BusinessAnalytics``
from BusinessAnalytics import get_stock_data, plot
import pandas as pd # Modul für DataFrames
import numpy as np
import matplotlib.pyplot as plt


# ## Schritt 1: Fragestellung
# 
# Dieser Schritt unterscheidet sich nicht von den konzeptionellen Überlegungen im [vorherigen Kapitel](Introduction_Fallstudie.md). Die konkrete Fragestellung lautet also:
# 
# **Wie wahrscheinlich ist es, dass wir bei einer Investition in den DAX einen Verlust nach X Jahren erleiden?**
# 
# Machen wir uns nun an die konkrete Beantwortung der Frage via Python

# ## Schritt 2: Beschaffung der Daten
# 
# Unsere Analyse fußt auf historischen Dax-Kursen. Diese müssen wir nun in Python einlesen. Hierfür gibt es prinzipiell zwei Ansätze (die dann auf verschiedene Art und Weisen umgesetzt werden können):
# 
# 1. manuelles Herunterladen und Abspeichern der Daten als (z.B.) `csv`-Datei und dann einlesen der Datei
# 2. direktes Einlesen der Daten via Python-Code ohne Zwischenspeichern einer Datei
# 
# Prinzipiell haben beide Varianten Vor- und Nachteile. In [vorherigen Kapitel](Introduction_Fallstudie.md) wurde [hier](download-yahoo) aufgezeigt, wie wir die konkreten DAX-Daten als Datei abspeichern. In unserem Fall verzichten wir darauf und wählen Variante 2, d.h. wir laden die Daten direkt in Python. Wir müssen dafür den Yahoo-Ticker für den DAX (`^GDAXI`) sowie Start- und Enddatum der benötigten Daten angeben. 

# In[81]:


dax_data = get_stock_data(ticker="^GDAXI", start="30-12-1987", end="31-07-2022")


# Was macht der obige Programmcode? 
# 
# Mit der Funktion `get_stock_data` laden wir die Yahoo-Daten herunter. Das Ergebnis ist ein sog. `Dataframe` (stellen Sie sich eine Art Excel-Tabelle vor), in dem alle Yahoo-Daten gespeichert sind. Diesen Dataframe "speichern"[^1] wir unter dem Namen `dax_data`.  Dieser Name ist beliebig; jeder andere Name wäre hier auch möglich gewesen. Es ist jedoch gute Programmier-Praxis beschreibende Namen zu wählen. Wir werden in diesem Skript englische Namen wählen, da dies ebenfalls übliche Praxis ist. 
# 
# [^1]: Der Begriff abspeichern ist an dieser Stelle nicht ganz korrekt bzw. präzise. Eigentlich weisen wir den Output einer Variable zu. Der Computer allokiert dann Speicher für diese Information. In Python beinhaltet die Variable dann die Referenz auf diese Speicheradresse. Für unsere Zwecke sind diese Details jedoch nicht wichtig. In diesem Skript und Kurs werden wir  bewusst unpräzise formulieren, um die Verständlichkeit beim Lesen zu erhöhen. 

# Schauen wir uns die Daten an. Dies machen wir, in dem wir in eine Code-Zelle den Namen der Variable schreiben:

# In[82]:


dax_data


# Bei großen Datenmengen bietet es sich an, nur einen Teil der Informationen anzuzeigen. Wir können z.B. nur die ersten 5 Zeilen ausgeben lassen mit Hilfe der "Funktion" `head`:

# In[83]:


dax_data.head()


# Nachdem wir die Daten nun in Python eingelesen haben, beginnen wir mit dem nächsten Schritt, der Aufbereitung der Daten. 

# ## Schritt 3: Aufbereitung der Daten

# Yahoo hat insgesamt 8.906 Tage mit Dax-Daten bereitgestellt. Jede Zeile beinhaltet Informationen eines Tages. An den Spaltenüberschriften erkennen wir, welche Daten vorliegen. 
# 
# - Open: Eröffnungskurs des Tages
# - High: Höchstkurs des Tages
# - Low: Tiefstkurs des Tages
# - Close: Schlusskurs des Tages
# - Adj. Close: Schlusskurs des Tages adjustiert um z.B. Dividendeneffekte
# - Volume: Handelsvolumen an dem Tag 
# - ticker: Yahoo-Ticker des Datenpunktes
# 
# Für unsere Zwecke benötigen nur einen Dax-Kurs pro Tag. Wir werden deshalb den `Ad. Close`-Kurs nehmen und alle anderen Daten mit Ausnahme des Datums wieder herausnehmen. Zusätzlich werden wir die Spalten noch umbenennen in "Datum" und "Preis" und fehlende Datenpunkte (gekennzeichnet als `NaN` ("not a number")) löschen[^2]. 
# 
# [^2]: An dieser Stelle entfernen wir fehlende Datenpunkte ohne weitere Analyse, weshalb die Datenpunkte überhaupt fehlen. Für viele Analysen sollte man dem Grund für die fehlenden Daten jedoch hinterhergehen, um sicherzustellen, dass (i) die Datenquelle ggf. nicht verlässlich ist und/oder (ii) die Ergebnisse nicht verfälschen werden.

# In[84]:


dax_data = (dax_data
            .filter(items=["Date", "Adj Close"], axis=1) # Filtern der benötigten Spalten
            .rename({"Date": "Datum", "Adj Close": "Preis"}, axis=1) # Umbenennen der Spaltennamen
            .dropna() # Fehlende Datenpunkte entfernen
            )
# Ergebnis anzeigen lassen
dax_data


# Bevor wir die Daten für unsere Zwecke weiter aufbereiten, schauen wir uns diese an, um sicherzustellen, dass die Kursentwicklung plausibel aussieht. 

# In[85]:


plot(data=dax_data, x="Datum", y="Preis", 
     colors="red",
     title="Tägliche Entwicklung DAX\n(1988 - 2022)",
     show_legend=False);


# Mit der Funktion `plot` können wir die Daten visualisieren, d.h. Graphen bzw. Plots daraus generieren. Wir müssen dafür nur die Datenquelle (hier: `dax_data`) und die X- sowie die Y-Achse angeben ("Datum" und "Preis").  Optional haben wir noch angegeben, dass die Linie rot sein soll und der Plot eine Überschrift, aber keine Legende haben soll. 

# Die Entwicklung - wir können diese mit Charts auf Finanzportalen vergleichen - sieht plausibel aus. Wir haben offensichtlich die richtigen Daten von Yahoo heruntergeladen. 
# 
# Im nächsten Schritt müssen wir nun die Renditen berechnen, da wir diese für beide Ansätze - "Zurück in die Vergangenheit" und "historischer Zufall" - benötigen. Wir erstellen deshalb eine neue Spalte ("Rendite"), in der wir die tägliche Rendite (Hinweis: $r_t = \frac{P_t}{P_{t-1}} -1$) speichern. Dies können wir z.B. mit der Funktion `pct_change` berechnen. 

# In[86]:


dax_data = (dax_data
            .assign(Rendite=dax_data["Preis"].pct_change()) # Erstelle neue Spalte "Rendite"
            .dropna() # Entferne NaN-Spalten, da für ersten Kurs kein Vorkurs existiert
            )
# Ergebnis anzeigen lassen (hier: erste 10 Zeilen)
dax_data.head(10)


# ### Ansatz 1: Zurück in die Vergangenheit

# Im ersten Ansatz haben wir uns überlegt, dass wir für jeden Tag, an dem wir hätten investieren können (implizite Annahme: zu adjustierten Schlusskursen) untersuchen, wie diese Investition sich über die Zeit entwickelt hätte. Dafür müssen wir uns die Renditen für jeden Tag genauer anschauen. 
# 
# ```{admonition} Beispiel für drei Anlagen
# :class: tip
# 
# **Beispiel 1:**
# Hätten wir bspw. am Handelstag vor dem 4.1.1988 investiert, dann hätten wir nach dem ersten vollen Handelstag eine Rendite von $(10-0.0484) - 1$ gemacht. Nach zwei Tagen hätten wir eine Rendite von $(1-0.0484)\times(1+0.0414) - 1 \ldots$ usw.
# 
# **Beispiel 2:**
# Hätten wir bspw. am Handelstag vor dem 5.1.1988 investiert, dann hätten wir nach dem ersten vollen Handelstag eine Rendite von $(1+0.0414) - 1$ gemacht. Nach zwei Tagen hätten wir eine Rendite von $(1+0.0414)\times(1+0.0099) - 1\ldots$ usw.
# 
# **Beispiel 3:**
# Hätten wir bspw. am Handelstag vor dem 6.1.1988 investiert, dann hätten wir nach dem ersten vollen Handelstag eine Rendite von $(1+0.0099) - 1$ gemacht. Nach zwei Tagen hätten wir eine Rendite von $(1+0.0099)\times(1+0.0084) - 1\ldots$ usw.
# ```
# 
# Jede Anlage beginnt also immer genau einen Tag später. Der Anfangszeitpunkt ist somit immer .genau eine Zeile später. Dies können wir in Python sehr einfach abbilden. 
# 
# Untenstehend ein Beispiel für unsere drei Beispielanlagen:

# In[87]:


beispiel = (dax_data
            .drop(columns=["Datum", "Preis"]) # Spalten Datum und Preis werden nicht mehr benötigt
            .assign(Periode=range(1,len(dax_data)+1), # Periode der Investition (1 bis letzte Zeile)
                    Anlage1=dax_data["Rendite"].shift(0),  # Renditen für Startdatum 5.1.1988
                    Anlage2=dax_data["Rendite"].shift(-1), # Renditen für Startdatum 6.1.1988
                    Anlage3=dax_data["Rendite"].shift(-2)) # Renditen für Startdatum 7.1.1988
            )
beispiel


# Schauen wir uns den Programmcode an, dann sehen wir, dass wir für jedes weitere Startdatum die Spalte "Rendite" immer um eine Zeile versetzen (engl. "shift") müssen. 
# 
# Jedoch benötigen wir nicht die Renditen, sondern die kumulierten Produkte (engl. cumulative product) der Renditen, d.h.:
# 
# $$(1+r_t)\times(1+r_{t+1})\ldots\times(1+r_{t+N}) - 1 = \ldots$$ 
# 
# Dafür müssen wir den obigen Programmcode nur geringfügig verändern:

# In[88]:


beispiel = (dax_data
            .drop(columns=["Datum", "Preis"]) # Spalten Datum und Preis werden nicht mehr benötigt
            .assign(Periode=range(1,len(dax_data)+1), # Periode der Investition (1 bis letzte Zeile)
                    Anlage1=(1 + dax_data["Rendite"].shift(0)).cumprod() - 1,  # kum. Produkt der Renditen für Startdatum 5.1.1988
                    Anlage2=(1 + dax_data["Rendite"].shift(-1)).cumprod() - 1, # kum. Produkt der Renditen für Startdatum 6.1.1988
                    Anlage3=(1 + dax_data["Rendite"].shift(-2)).cumprod() - 1)  # kum. Produkt der Renditen für Startdatum 7.1.1988
            )
beispiel


# 
# Nun ist es natürlich sehr mühsam, diesen Vorgang für alle möglichen Startzeitpunkte (d.h. 8734x) zu wiederholen. Glücklicherweise müssen wir dies auch nicht, sondern können diesen Vorgang automatisieren via Python[^3].
# 
# Bevor wir dies tun, sollten wir jedoch noch eine Mindestlaufzeit definieren, für die unsere Anlagen laufen müssen, um berücksichtigt zu werden. Ansonsten haben unsere letzten Anlagen nur wenige Datenpunkte; z.B. hätte eine Anlage mit den Startpunkt 28.7.2022 nur einen Datenpunkt.
# 
# Wir nehmen deshalb an, dass wir für mindestens 1000 Handelstage - d.h. ca. 5 Jahre - investieren möchten.
# 
# [^3]: Sie können sich an dieser Stelle bereits merken, dass repetitive Vorgänge im Programmiercode im Grunde nicht vorkommen sollten, da diese nahezu immer automatisiert werden können. Dies werden wir in den nächsten Kapiteln noch lernen. 
# 
# Hier folgt der Code für

# In[7]:


def calculate_anlagen(data, min_laufzeit):
    '''Funktion, um Renditen aller Anlagen zu berechnen
    
    Input: 
    - data: Datensatz, mit Renditedaten
    - min_laufzeit: Angabe über Mindestlaufzeit einer Anlage

    Output: Dataframe mit Daten aus "data" und Renditedaten für jede Anlage
    '''

    ## Vorarbeiten
    rows = len(data) # Anzahl Zeilen im Datensatz
    data_new = data.copy() # Erstelle Kopie des Datensatz, um bei Fehlern Daten nicht zu überschreiben
    
    ## Berechne Renditen aller Anlagen, die Kriterium min_laufzeit erfüllen
    anlagen = {f"Anlage_{i+1}":(data_new["Rendite"].shift(-i))
                           for i in range(0,len(data_new)-min_laufzeit)} # Berechne Renditen alle Anlagen
    anlagen = pd.DataFrame(anlagen) # Speicher Anlagen in Dataframe
    
    ## Berechne kumulierte Rendite
    anlagen = (1+anlagen).cumprod() - 1

    ## Verbinde ursprüngliche Daten mit neuen Anlagen-Daten
    data_combined = pd.concat((data_new, anlagen), axis=1).reset_index(drop=True) 
    
    ## Gib Daten aus
    return data_combined#.reset_index(drop=True)


# Den obigen Programmcode nutzen wir nun, um einen neuen Dataframe zu erstellen, in dem das kumulierte Produkt der Renditen aller Anlagen berechnet wurde. 

# In[146]:


min_t = 1000
data_anlagen = (dax_data
                .drop(columns=["Datum", "Preis"]) # Spalten Datum und Preis werden nicht mehr benötigt
                .assign(Periode=range(1,len(dax_data)+1)) # Periode der Investition (1 bis letzte Zeile)
                .pipe(calculate_anlagen, min_laufzeit=min_t) # Berechne Renditen aller Anlagen
               )
data_anlagen.head(10)


# Als Ergebnis sehen wir einen Datensatz, der die kumulierten Produkte der Renditen von Anlage 1 bis Anlage 7737 beinhaltet.  Diesen können wir mithilfe des folgenden Programmcode auch graphisch Darstellen.

# In[134]:


def plot_anlagen(data):
    '''Funktion, um Anlagen zu Plotten
    
    Hinweis: Hilfefunktion, da `plot`-Funktion ansonsten zu lange rechnet

    '''
    data_plot = data.filter(like="Anlage").to_numpy()
    
    fig, ax = plt.subplots()
    plt.plot(data_plot, color="green", linewidth=0.025,alpha=0.05)
    ax.set_xlabel("Periode")
    ax.set_ylabel("Rendite der Anlage")
    fig.suptitle(f"Wertentwicklung aller Anlagen in DAX\n(Anlagezeitraum mindestens {min_t} Tage)")

    xmin, xmax = ax.get_xlim()
    ax.hlines(0, xmin, xmax, colors="black", linestyles="--", label="Verlustlinie")
    ax.annotate("Verlustlinie", (xmax, 0.1), ha="right")
    return None


# In[133]:


# Hinweis: die Berechnung kann ja nach Computer einige Minuten dauern
plot_anlagen(data_anlagen);


# ## Schritt 4: Analyse für Ansatz 1

# Wir sehen bereits, dass ca. ab Periode 4.000 keine Anlage (unabhängig vom Startpunkt) noch einen Verlust - d.h. Rendite von unter 0% - gemacht hat. 
# 
# Lassen Sie uns diese Verlustwahrscheinlichkeit nun aber konkret, wie im vorherigen Kapitel erläutert, berechnen. 
# 
# Hierzu müssen wir für jeden Handelstag die Anzahl der Portfolien addieren, die eine Rendite von unter 0% gemacht haben und durch die Anzahl aller Portfolien teilen. 
# 
# Im Programmcode ist dies sehr einfach abzubilden:

# In[170]:


data_anlagen = (data_anlagen
                .assign(Verlustwahrscheinlichkeit= (data_anlagen.filter(like="Anlage", axis=1) < 0).sum(axis=1) / len(data_anlagen))
)
data_anlagen[["Periode", "Verlustwahrscheinlichkeit"]]


# An der Tabelle sehen wir, dass die Verlustwahrscheinlichkeit nach einem Tag bei ca. 40% liegt. Jedoch sehen wir, dass die Verlustwahrscheinlichkeit in den letzten Perioden 0% beträgt. D.h. in unserem Datensatz gab es z.B. keine Anlage, die nach 8733 Perioden noch eine Rendite von unter 0% gemacht hatte. Noch klarer wird die Berechnung, wenn wir die Verlustwahrscheinlichkeit plotten. 

# In[24]:


def plot_verlustwahrscheinlichkeit(data):
     ax = plot(data=data, x="Periode", y="Verlustwahrscheinlichkeit",
          colors="red",
          title="historische Verlustwahrscheinlichkeit Anlage in DAX",
          show_legend=False);
     day0 = np.argmax(data["Verlustwahrscheinlichkeit"] == 0)
     day01 = np.argmin(np.abs(data["Verlustwahrscheinlichkeit"] - 0.1))
     ax.annotate(f"Tag {day0}: Verlustwahrscheinlichkeit = 0%",(day0,0.01), ha="left" , color="red")
     ax.hlines(y=0.1, xmin=0, xmax=day01, colors="black", linestyles="--", linewidth=0.5)
     ax.annotate(f"Tag {day01}: Verlustwahrscheinlichkeit = 10%",(day01,0.10), ha="left" , color="black")
     return None


# In[194]:


plot_verlustwahrscheinlichkeit(data_anlagen)


# ## Fazit: Ansatz 1

# Mit unserer empirischen Analyse konnten wir die Ausgangsfrage beantworten. Die Verlustwahrscheinlichkeit bei Investition in den DAX ist real. Allerdings beschränkt sich dies historische auf einen kurzen Anlagehorizont. So gab es auf Basis der historischen Daten keinen Zeitpunkt einer Anlage, bei der man nach mehr als 3.444 Tagen (ca. 17 Jahre) noch einen Verlust gemacht hätte. Selbst bei der Hälfte der Anlagedauer, d.h. nach ca. 9 Jahren, betrug die Verlustwahrscheinlichkeit nur noch 10%. 
# 
# Hat man einen langfristigen Investitionsansatz, so ist das Risiko einer Investition in den DAX deutlich geringer, als dies oft aus dem Bauch heraus angenommen wird.
# 
# ````{margin} 
# ```{admonition} Analyse basiert auf Annahmen!
# :class: warning, dropdown
# Wichtig ist an dieser Stelle jedoch zu betonen, dass die Analyse auf vielen Annahmen beruht. Einige davon können wir ändern, um zu schauen, wie sensitiv die Analyse auf diese Annahme reagiert (z.B. könnten wir auch den Tagestiefstpreis nehmen). Andere müssen wir aus Mangel an Alternativen so treffen, können jedoch  kritisch sein (z.B. basiert unsere Analyse auf Yahoo-Daten, die ggf. Fehler beinhaltet). Andere Annahmen sind grundsätzlicher Natur: wir basieren unsere Analyse auf historischen Daten und ziehen daraus Schlüsse für die Zukunft. Dies setzt voraus, dass die Kursentwicklungen in der Zukunft ähnlich sind, wie in der Vergangenheit. Jedoch kann die Zukunft auch ganz andere Entwicklungen beinhaltet, die wir so nicht vorhersehen (z.B. könnte die wirtschaftliche und politische Stellung Deutschlands sich in der Zukunft negativ entwickeln)
# ```
# ````

# Untenstehend die Analyse zusammengefasst in einem Schritt:

# In[43]:


min_t = 1000
price = "Adj Close"
dax_data = get_stock_data(ticker="^GDAXI", start="30-12-1987", end="31-07-2022")
(dax_data
    .filter(items=["Date", price], axis=1) # Filtern der benötigten Spalten
    .rename({"Date": "Datum", price: "Preis"}, axis=1) # Umbenennen der Spaltennamen
    .assign(Rendite=dax_data.iloc[:,1].pct_change()) # Erstelle neue Spalte "Rendite"
    .dropna() # Entferne NaN-Spalten, da für ersten Kurs kein Vorkurs existiert
    .drop(columns=["Datum", "Preis"]) # Spalten Datum und Preis werden nicht mehr benötigt
    .assign(Periode=lambda _df: range(1,len(_df)+1)) # Periode der Investition (1 bis letzte Zeile)
    .pipe(calculate_anlagen, min_laufzeit=min_t) # Berechne Renditen aller Anlagen
    .reset_index(drop=True) # Erstelle den Index des Dataframes neu (weil, NaN-Zeilen gelöscht wurden)
    .assign(Verlustwahrscheinlichkeit=lambda _df: (_df.filter(like="Anlage", axis=1) < 0).sum(axis=1) / len(_df)) # Berechne Verlustwahrscheinlichkeit
    .pipe(plot_verlustwahrscheinlichkeit) # Erstelle Plot
    );

