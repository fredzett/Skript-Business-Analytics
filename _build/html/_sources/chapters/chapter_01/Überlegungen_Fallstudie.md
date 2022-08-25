# Wie riskant sind Aktien?

## Ausgangslage

Sie haben ihr Studium beendet und gelten in ihrer Familie nun als Expert*in für finanzielle Fragestellungen. Ihr Onkel, der überraschend einen größeren Geldbetrag geerbt hat, kommt auf Sie zu und fragt Sie, wie er das Geld sinnvoll anlegen könne. Sie raten Ihm dazu das Geld in einen breiten Aktienindex (passiv) zu investieren. Ihr Onkel winkt direkt ab, weil ihm Aktien "viel zu riskant" seien. Da könne man ja auch sehr viel Geld bei verlieren. 

Einerseits wollen Sie ihrem Onkel nicht raten das Geld in Immobilien oder in Festgeld zu investieren. Anderseits kommen Sie selber ins Grübeln, ob eine Investition in Aktien nicht vielleicht doch zu riskant ist. Sie beschließen deshalb der Frage empirisch nachzugehen. 

Konkret wollen Sie versuchen zu analysieren, wie riskant eine Investition in Aktien tatsächlich ist. 


Obgleich es sich bei unserer Fragestellung um eine "persönliche" Analyse handelt, steht diese doch stellvertretend für ein typisches **Business Analytics**-Problem, bei dem es darum geht ein konkretes Problem bzw. eine konkrete Fragestellung datenbasiert zu beantworten. 

Für unsere Analyse bedarf es daher einer Fragestellung, die konkret bzw. "operationalisierbar" ist

Dies gilt für die bisherige Fragestellung leider noch nicht. Was bedeutet "riskant" bzw. "Risiko"? In welche Aktien wollen wir investieren?

Aus Vereinfachungsgründen definieren wir **Risiko** in unserem Fall als die **Wahrscheinlichkeit einen Verlust zu erleiden**. Wir fragen uns also konkret: wie wahrscheinlich ist es, dass ihre Investition innerhalb eines (noch zu bestimmenden) Zeitraums an Wert verliert. Der Einfachheit halber nehmen wir an, dass wir in den DAX (siehe [Wikipedia](https://de.wikipedia.org/wiki/DAX)) investieren. 

Die konkrete Fragestellung lautet also: **Wie Wahrscheinlich ist es, dass wir in den DAX investieren und dabei einen Verlust erleiden?**

Lassen Sie uns nun konret überlegen, wie wir diese konkrete Frage empirisch beantworten können. 

## Schritt 1: Beschaffung der Daten

Die formulierte Frage ist natürlich nicht sicher bzw. eindeutig zu beantworten. Wir bräuchten dafür die DAX-Stände der nächsten Jahren; wir müssten also die Zukunft vorhersehen. Wir haben die _perfekten_ Daten nicht.  

````{margin} 
```{admonition} Hinweis
:class: note
Jede Analyse basiert immer auf Annahmen. Diese können prinzipiell nicht falsch sein, sondern sinnvoll oder weniger sinnvoll. Ziel einer datenbasierten Analyse sollte es sein, sinnvolle und konsistente Annahmen zu treffen und diese auch transparent zu machen. 
```
````

In unserem Falle können wir jedoch `historische Daten` nutzen. Statt in die Zukunft zu schauen, treffen wir also eine Annahme. Für die Zwecke unserer Analyse nehmen wir an, dass die historischen Daten ein guter Schätzer für die Zukunft sind. 

Historische Daten für Aktien sind glücklicherweise - zumindest für unsere Zwecke - einfach und frei zugänglich. Die Beschaffung der Rohdaten stellt also kein Problem dar. 

```{admonition} "How to": Download von Aktienkursen
:class: tip, dropdown

Aktienkursdaten sind - zumindest für unsere Zwecke - einfach und kostenlos zugänglich. Wir werden als Quelle [Yahoo Finance](https://de.finance.yahoo.com/quote) nutzen. Wir können hier (auch historische) Daten von allen wesentlichen Aktien und Indices einsehen und herunterladen. Die heruntergeladenenen Daten können in Form einer `csv-Datei` gespeichert werden. 

Hier ein Beispiel zum Download historischer DAX-Kurse: 

![](../assets/Yahoo_download.gif)
<break></break>

Im weiteren Verlauf werden wir noch lernen, dass wir die Kurse via Python noch einfacherer und ohne manuelles Abspeichern von Daten einlesen können. 
```

## Schritt 2: Aufbereitung der Daten

Die historischen Kursdaten als Datenquelle ("Rohdaten") stellen kein Hürde dar. Der Download der Rohdaten ist einfach  (siehe "how to"), liefert jedoch nur bedingt eine Antwort auf unsere Frage. In {numref}`dax-ref` erkennen wir zwar, dass der DAX seit Beginn und bis zum Juli 2022 stark gestiegen ist (Anfangsstand: $1.000$, Endstand: $13.484$) und wir unser Geld in etwa um den Faktor $13x$ vermehrt hätten. Es gab jedoch offensichtlich auch Zeiträume in denen eine Investition an Wert verloren hätte. So hat der Dax z.B. seit seinem Höchsstand von $16.271,75$ im Januar 2022 bis heute deutlich an Wert verloren. Hätte man am Tag des Höchsttandes investiert, hätte man aktuell einen deutlichen Verlust gemacht. 

```{figure} ../assets/Dax.png
:name: dax-ref
Entwicklung Dax 1987 bis heute
```

Wir müssen die Rohdaten deshalb für unsere Zwecke aufbereiten. Was benötigen wir für unsere Zwecke konkret? Um diese Frage zu beantworten müssen wir darüber nachdenken, wie wir die Frage **"Wie Wahrscheinlich ist es, dass wir in den DAX investieren und dabei einen Verlust erleiden?** beantworten wollen. 

### Ansatz 1: Zurück in die Vergangenheit

Das Grundproblem ist, dass wir zwar historische Daten haben, wir aber theoretisch an jedem Tag in der Vergangenheit "zufällig" unser Geld hätten investieren können. Abhängig vom Tag des Beginns der Investition (und natürlich dem Tag des Verkaufs) produziert unsere Strategie immer unterschiedliche "Gewinne". 

````{margin} 
```{admonition} Hinweis
:class: note

Wenn ich zum Tag $t$ eine Aktie zum Preis $P_t$ kaufe und am Tag $T$ zum Preis $P_T$ verkaufe, dann lässt sich die Rendite wiefolgt berechnen:

$r_T = \frac{P_T}{P_{t}} - 1$
```
````

- Beispiel 1: hätten wir am 10.6.1991 (Stand: $1.698$) investiert und am 26.03.2001 (Stand: $5.726$) verkauft, dann hätten wir eine **Rendite von ca. $+237$%** gemacht.  


- Beispiel 2: hätten wir am 12.04.2007 (Stand: $7.808$) investiert und am 19.12.2008 (Stand: $4.696$) verkauft, dann hätten wir eine **Rendite von ca. $-40$%** gemacht. 

Die zwei Beispiele sind zufällig gewählt. Es hätte sehr viele mehr verschiedene Zeitpunkte und Zeiträume gegeben in der man hätte anlegen können. Dabei ist der _optimalen_ Anlagezeitpunkt und Zeitraum leider erst im Nachhinein bekannt. 

Um unsere Frage zu beantworten, müssen wir deshalb **Zurück in die Vergangenheit** gehen und für jeden möglichen Anfangszeitpunkt (d.h. jeder Handelstag seit Beginn des DAX in 1987) über jeden möglichen Anlagezeitraum investieren. Da wir in die Vergangenheit schauen, haben wir die Daten, um unsere Wertentwicklung für jede dieser Investitionen zu beobachten. 

Lassen Sie uns zunächst anhand eines einfachen und fiktiven Beispiels durchspielen, welche Vergangenheitsanalyse wir durchführen wollen. Nehmen wir an, wir hätten $10$ historische Kurse eines Index, dessen Entwicklung in {numref}`index-ref` dargestellt sind. 


```{figure} ../assets/Index_Beispiel.png
:name: index-ref
Entwicklung Index über 10 Perioden
```

Wir fragen uns nun, wie Wahrscheinlich es war, einen Verlust zu vereinnahmen. Wir wollen mindestens 5 Perioden investieren (d.h. wir wissen noch nicht wie lange wir investieren wollen, sind uns jedoch sicher, dass wir innerhalb von 5 Perioden nicht verkaufen werden)

Die für unsere Überlegung benötigten Daten sind in {numref}`index-table` abgebildet.


```{table} Beispiel: Index mit 10 historischen Kursen
:name: index-table
|         	|    1 	|    2 	|    3 	|     4 	|     5 	|    6 	|    7 	|     8 	|     9 	|    10 	|
|---------	|-----:	|-----:	|-----:	|------:	|------:	|-----:	|-----:	|------:	|------:	|------:	|
| Kurs    	|  102 	|  105 	|  109 	|   108 	|   106 	|  107 	|  109 	|   106 	|   101 	|   111 	|
| Rendite 	| 2,0% 	| 3,0% 	| 4,0% 	| -1,0% 	| -2,0% 	| 1,0% 	| 2,0% 	| -3,0% 	| -5,0% 	| 10,0% 	|
```

````{margin} 
```{admonition} Hinweis
:class: note
Wir gehen davon aus, dass wir immer zu Beginn einer Periode investieren. Würden wir in Periode 7 kaufen, würde das Kritierum nicht mehr erfüllt, da wir bis Periode 11 halten müssten, wir aber nur historische Daten bis Periode 10 haben.
```
````

Wir könnten insgesamt **6** verschiedene Investitionszeitpunkte definieren, die das Kriterium "mindestens 5 Perioden investieren" erfüllen. 

- Anlage 1: Kaufen in Periode 1
- Anlage 2: Kaufen in Periode 2
- ...
- Anlage 6: Kaufen in Periode 6

Wie ermitteln wir jetzt die Wertentwicklung unserer verschiednen Anlagen über die Zeit?



Nehmen wir an, dass wir je $1.00$ EUR investieren. Anlage 1 würde uns in der ersten Periode $2$% Rendite bringen. Aus unserer Anfangsinvestition würden also $1\times(1+0.02) = 1.02$ EUR werden. Dieser neue Wert von $1.02$ EUR würden sich in der nächsten Periode (Periode 2) mit $3$% verzinsen, so dass wir am Ende von Periode 2 insgesamt $1.02 \times (1.03) = 1.0506$ EUR hätten usw... 

Allgemeiner können wir sagen, dass sich die Performance einer Strategie ($R_T$) über die Multiplikation der Perioden-Renditen berechnen lässt. 

Beispiel für Anlage 1 für 5 Perioden ($I_0$ = Anfangsinvestition; hier: $1$ EUR): 

$$ I_0 \times(1+0.02)\times(1+0.03)\times(1+0.04)\times(1-0.01)\times(1-0.02) - 1 = 0.06$$

Über eine Haltedauer von 5 Perioden hätte man mit Anlage 1 demnach aus $1.00$ EUR insgesamt $1.06$ EUR gemacht, d.h. $6$ct verdient bzw. $6$% Rendite gemacht. 

Allgemeiner können wir schreiben: die Performance einer Strategie ($R_T$) lässt sich über die Multiplikation der Perioden-Renditen ermitteln. 

$$
R_T = I_0 \times \prod_{t=1}^T (1+r_t) - 1
$$

In {numref}`anlagen-ref` ist die Wertentwicklung der 6 Anlagen bei einer Anfangsinvestition von je $1.00$ EUR dargestellt. 

```{figure} ../assets/Anlagen_perf.png
:name: anlagen-ref
Entwicklung der sechs Anlagen
```

Im obigen Beispiel sehen wir, dass es für unseren Beispielindex Phasen gab, bei denen wir einen Verlust gemacht hätten. Z.B. hat Anlage 4 nach Periode 6 einen Verlust von ca. $8$ct. Auf der anderen Seite gab es Phasen, in denen man Gewinn gemacht hat. Z.B. Anlage 1 nach 10 Perioden. 

Unser Beispiel zeigt, dass wir zur Beantwortung unserer Frage **Renditen** benötigen und diese für alle möglichen Investitionszeitpunkte und Zeiträume miteinander multiplizieren müssen. In der praktischen Umsetzung schauen wir uns an, wie dies sehr simple möglich ist. 

### Ansatz 2: Historischer Zufall

Im vorrangeganen Beispiel haben wir gesehen, wie wir auf Basis von Vergangenheitsdaten fiktive Anlagen getätigt haben, die in der Form aber real möglich gewesen wären. Man hätte in der Vergangenheit tatsächlich in Periode 1 für z.B. 5 Perioden anlegen können. In diesem Fall hätte man tatsächlich eine Rendite von $6$% gemacht. 

Der Nachteil dieses Ansatzes ist jedoch, dass es uns z.B. nicht möglich ist 6 unterschiedliche Anlagen mit einem Investitionshorizont von jeweils 10 Perioden abzubilden. Diese Anlagen wären in der Realität schlicht nicht möglich gewesen, da es in unserem Beispiel nur eine Anlage gibt, für die ein Investitionshorizont von 10 Perioden möglich war  (Anlage 1). 

Im zweiten Ansatz "Historischer Zufall" umgehen wir dieses Problem. Anstatt reale historische Performance abzubilden 

Im ersten Ansatz, wir nennen diesen **"Zurück in die Zukunft"**

**Ansatz 2: historischer Zufall**
