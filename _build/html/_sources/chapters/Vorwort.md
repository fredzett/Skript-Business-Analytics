# Vorwort

Bei diesem (Online-)Skript handelt es sich um Selbstlernmaterial zum Modul **(Advanced) Business Analytics**. Da es sich bei dem genannten Modul um ein komplett neu konzipiertes Modul handelt, "lebt" das Dokument noch und wird bei Bedarf aktualisiert und angepasst. 

Das Skript ist explizit so verfasst, dass es sich zum Selbststudium eignet; dies ist beim Verfassen des Skripts zumindest immer meine ausdrückliche Intention gewesen. Alle Code-Beispiele können via Knopfdruck selbst ausprobiert und adaptiert werden. Das Dokument ist somit zu Teilen interaktiv und sollte deshalb auch nicht nur passiv konsumiert werden. Ob mein Vorhaben tatsächlich gelungen ist, können jedoch schlussendlich nur Sie beurteilen. Sollten Sie also Fragen oder Anmerkungen bzw. technische Probleme haben oder - und dies bleibt leider nie aus - Fehler entdecken, dann bin ich dankbar für Ihr Feedback. Sprechen Sie mich entweder in den Veranstaltungen zum Modul direkt an oder schreiben mir eine Email (felix.zeidler@fh-bielefeld.de). Auch wenn es mir vermutlich nicht immer gelingen wird, Ihnen direkt zu antworten, bin ich dankbar für jede Art von Rückmeldung. 

`test`

## Warum ein Modul zum Thema "Business Analytics"

Bevor wir inhaltlich in ein spannendes und (teilweise) neues Themenfeld einsteigen, möchte ich zunächst die Beweggründe für die Konzeption dieses neuen Moduls erläutern. 

**Business Analytics** umfasst drei wichtige Elemente, die nicht getrennt von einander adressiert werden sollten: 

1.  **Datenkompetenz**: in einer digitalen (Unternehmens)Welt werden Entscheidungen zunehmend datenunterstützt getroffen. Studierende der Betriebswirtschaftlehre sollten deshalb Kompetenzen im Umgang mit und der Analyse von Daten erlernen. 

2. **Technologiekompetenz**: die Nutzung von Daten und die teilweise Automatisierung von (Entscheidungs-)prozessen ist eng verknüpft mit der Nutzung von IT-Technologie. Das Themenfeld **Business Analytics** sollte deshalb nicht ausschließlich auf qualitativer "strategischer" Ebene gelehrt werden, sondern sollte sich ganz konkret mit der praktischen Datenaufbereitung und -analyse sowie Visualisierung beschäftigen. Ganz platt formuliert, sollten Studierende der Betriebswirtschaftlehre nicht nur wissen, was Business Analytics ist, sondern vielmehr auch lernen, wie Business Analytics geht.

3. **Fachexpertise**: wir werden später noch feststellen, dass Business Analytics nicht einheitlich definiert ist und somit viele Facetten hat. Nach unserem Verständnis dient Business Analytics dazu, unternehmerische Entscheidungen durch die sinnvolle Nutzung von Daten zu unterstützen. Wir wollen also konkret Daten und Informationen berücksichtigen, die einen Bezug zu betriebswirtschaftlichen Fachfunktionen - z.B. Marketing, Vertrieb, Finanzen, HR oder Controlling - haben. 

Nun ist es so, dass das Thema "Business Analytics" oder Datenanalyse und -kompetenz nicht neu ist. Darüber hinaus gibt es viel gute Quellen, um sich dem Thema inhaltlich zu widmen. Zum einem gibt es bereits viele Studiengänge und spezielle Kurse in eher technischen Fachbereichen wie der Informatik oder dem Ingenieurwesen, die sich dem Thema explizit widmen. Zum zweiten gibt es auch sehr gute Online-Quellen, die das Thema bespielen. Wieso also ein weiteres Angebot? 

Die Antwort auf die Frage ist einfach und banal: es gibt bisher kein Angebot, was zu gleichen Teilen (i) auf die speziellen inhaltlichen und didaktischen Anforderungen der Betriebswirtschaftlehre eingeht und (ii) den Anspruch hat über die qualitativen und strategischen Aspekte hinaus auch die technische Dimension von Business Analytics zu vermitteln. 

Warum ist das so?

Sie werden wenig überrascht sein, dass die digitale Transformation der Welt und explizit auch der Wirtschaft im vollem Gange ist und mit hohem Tempo nahezu alle Bereiche unseres Leben verändert. Für Unternehmen bedeutet dies u.a. dass Prozesse digitalisiert und (teilweise) automatisiert werden. Ein (Neben-)Effekt daraus ist, dass die für Unternehmen verfügbare Datenmenge (dramatisch und mit rasender Geschwindigkeit) steigt. Dies ist grundsätzlich branchenunabhängig und gilt für den Online-Retailer genauso wie für ein "klassisches" Bauunternehmen. Zu Beginn dieser Entwicklung[^1] wurde zunächst darauf hingewiesen, dass Daten einen (immateriellen) Wert für Unternehmen darstellen, der zwar meist nicht konkret erfasst wird oder werden kann, jedoch von hoher Bedeutung ist. So titelte der Economist in einer seiner Titelgeschichten "The world’s most valuable resource is no longer oil, but data" (Economist, 06.05.2007). Betrachtet man die Wertentwicklung von Unternehmen in den letzten Jahrzehnten, so scheint sich dies tatsächlich zu bestätigen. Die wertvollsten Unternehmen der Welt sind nicht mehr - wie Jahrzehnte der Fall - Öl- und Gasunternehmen, sondern vielmehr die großen Tech-Unternehmen Google, Facebook, Amazon und Apple, die auf wahren Datenschätzen sitzen. Betrachtet man diese Unternehmen jedoch genauer, so fällt auf, dass sich diese vom Wettbewerb nicht nur oder ausschließlich durch bloße Datenverfügbarkeit abgrenzen, sondern vielmehr durch die Kompetenz diese Daten auch für inhaltlich bessere Entscheidungen oder Produkte zu nutzen.  

[^1]: der Beginn dieser Entwicklung ist selbst im Rückblick nicht mehr klar zu benennen. Die hier skizzierten Entwicklungen sind schleichend und dann mit exponentieller Geschwindigkeit eingetreten. Für unsere Zwecke ist der Zeitpunkt des Beginns dieser Entwicklung unerheblich. Wichtig ist, dass in den letzten 10 bis 20 Jahren eine dramatische Veränderung eingetreten ist, die voraussichtlich auch noch nicht beendet ist. Der Begriff Business Analytics ist auch davor bereits genutzt worden und deshalb grundsätzlich nicht neu, jedoch hat sich die Bedeutung in den letzten Jahren erhöht.


Insofern ist die Analogie "Daten = Öl" irreführend. Wert von (unternehmerischen) Daten entsteht eben erst durch die sinnvolle Nutzung von Daten. Die genannten Tech-Unternehmen haben deshalb viel Geld und Aufwand in die Nutzung von Daten gesteckt und dies ist nicht zuletzt auch ein Grund für den Boom der "künstlichen Intelligenz", die es u.a. ermöglicht große Datenmengen zu bearbeiten und zu nutzen.

Hochschulen müssen sich nun fragen, wie mit dieser Entwicklung umzugehen ist. Welche Kompetenzen müssen vermittelt und gelehrt werden, um neue Realitäten abzubilden? Was bedeutet  dies konkret für das Curriculum?  Die bisher gefundenen Antworten auf diese Fragen sind aus meiner Sicht - und diese ist natürlich begrenzt, ggf. selbstreferntiell und kann nicht das komplette Hochschuluniversum umfassen - nicht zufriedenstellen. Was ist der Grund dafür? 

Zu beobachten ist zum einen, dass die Kompetenz mit Daten umzugehen zumeist in "technischen" Studiengängen gelehrt wird. Dort entstehen neue Module und Studiengänge wie "Data Science". In der Betriebswirtschaftlehre wird das Thema nahezu ausschließlich qualitativ gelehrt. Dies ist aus meiner Sicht nicht nur schade, sondern - mit Blick auf die zukünftige Entwicklung des Faches - ein großer inhaltlicher und auch strategischer Fehler.

Gerade auch Studierende der Betriebswirtschaftslehre sollten (i) Kompetenzen im Umgang mit Daten und Datenanalyse entwickeln. Jedoch sind diese Kompetenzen eben (ii) nicht identisch mit denen der technischen Studiengängen. 

Widmen wir uns zunächst dem ersten Aspekt: auch Kaufleute sollten Kompetenzen im Umgang mit Daten und Datenanalyse entwickeln. Das Argument ist im Grunde so trivial wie naheliegend: Unternehmerische Entscheidungen werden von je her durch kaufmännische Analysen unterstützt. Da diese Analysen heute oft auf sehr großen (theoretisch verfügbaren) Datenmengen basieren, ist es naheliegend, dass auch Kaufleute den Umgang mit und die Nutzung von Daten systematisch erlernen. Sonst laufen Unternehmen Gefahr wichtige Daten bei der ökonomischen Beurteilung nicht zu berücksichtigen. Diese Aufgabe kann nicht (ausschließlich) von ökonomiefernen und rein technischen Spezialisten übernommen werden, da diese die fachspezifischen Besonderheiten und Eigenarten der kaufmännischen Daten nicht kennen. 

Kommen wir zum zweiten Aspekt: die notwendigen Kompetenzen sind nicht identisch mit denen der technischen Studiengänge. Es mag Bedenken geben, dass die Voraussetzungen zum Erlernen von Datenkompetenzen hohes mathematisches und technisches Vorwissen sind. Dies ist allerdings nicht notwendigerweise der Fall und beruht auch auf einer Fehlwahrnehmung. So wird das Thema **Datenanalyse** oft gleichgesetzt mit Statistik und künstlicher Intelligenz. Natürlich Bedarf es bei der Anwendung von komplexen Algorithmen eben den genannten Voraussetzungen, die Studierende der Betriebswirtschaftlehre typischerweise nicht mitbringen (müssen). Jedoch hat der zu beobachtende Fokus auf Algorithmen und Künstlicher Intelligenz im Grunde nichts mit den beobachtbaren unternehmerischen Realität zu tun. Dort geht es zu einem weitaus größeren Teil zunächst darum, sinnvolle Daten zu identifizieren, diese zu bereinigen, um dann Schlüsse daraus zu ziehen. Auch geht es oft darum Analysen sinnvoll zu visualisieren und zu präsentieren. Nur sehr selten geht es um die Anwendung von komplexen Modellen. 

Zusammenfassend gibt es in Unternehmen einen steigenden Bedarf an Kaufleuten, die auch über spezifische Datenkompetenzen verfügen. Diese Kompetenzen überschneiden sich jedoch nur zu einem geringen Teil mit denen aus technischen Studiengängen. 

## Lernziele des Moduls "Business Analytics"

Aufbauend auf der zuvor geführten Diskussion verfolgen wir mit diesem Modul drei inhaltliche Lernziele

1. Sie sollen den **Umgang mit Daten** erlernen und in der Lage sein Daten so aufzubereiten, dass diese sinnvoll zusammengefasst und analysiert werden können.  

2. Sie sollen **Schlüsse aus Daten ziehen** erlernen und in der Lage sein Entscheidungen durch die Analyse von Daten zu untermauern oder zu unterfüttern.  

3. Sie sollen **Daten und Analyse kommunizieren** können und in der Lage sein, Ergebnisse von Analyse oder den Entscheidungen zugrunde liegende Daten sinnvoll und adressatengerecht zu kommunizieren. Konkret umfasst dies die Fähigkeit, Daten und Analyse sinnvoll zu visualisieren und in eine "Data Story" zu verpacken.   

Die drei genannten Lernziele zielen auf die Vermittlung von Datenkompetenz ab. Wie oben beschrieben, handelt es sich dabei um eines der aus unserer Sicht drei Elemente von Business Analytics. 



Auch das zweite Element, die Technologiekompetenz, wollen wir vermitteln. Dies ist aus unserer Sicht jedoch kein Lernziel per se, sondern im Grunde "nur" Mittel zum Zweck. Es stellt sich nämlich die Frage, wie die o.g. Lernziele vermittelt werden sollen. Wie erläutert kann es im Grunde nicht darum gehen, dass Sie theoretisch verstehen oder nachvollziehen, wie Datenanalyse geht. Sie sollten sich die "Hände schmutzig machen" müssen und Datenanalyse praktisch erleben und durchführen. Unser Mittel zum Zweck wird die Programmiersprache **Python** sein. D.h. Sie werden lernen, Datenanalyse mit Hilfe von kleinen Programmen und Code-Bausteinen praktisch durchzuführen.[^2]

[^2]: in Abschnitt XY erläutern wir, weshalb wir gerade Python als geeignetes Mittel für die Datenanalyse erachten.

Zuletzt haben wir versucht, alle Beispiele und Fallstudien im Kontext von typischen betriebswirtschaftlichen Fachfunktionen sehen. Konkret heißt das, dass wir Daten analysieren werden, die z.B. aus dem Vertrieb, dem Marketing oder dem Finanzbereich entstammen. Auch wenn wir teilweise aus didaktischen Gründen simple und kleine Datensätze nutzen werden, so handelt es sich bei den Fragestellungen und Datensätzen grds. um realistische Beispiele. 




