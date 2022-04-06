# Text, den ich bei der Präsi sagen will

## Titelfolie
* Hallo miteinander, ich bin Markus Hartlage, ich studiere im 6. Semester Ingenieurinformatik und ich stelle euch heute meine Studienarbeit vor.
* Der Titel lautet ...
* Ziel der Arbeit war es, eine VHDL Komponente zu entwickeln, an deren Ausgang je nach Konfiguration verschiedene Ausgangsspannung anliegen können
* Ich werde zunächst das von mir entwickelte Konzept vorstellen und dann ein paar der wichtigsten Teilkomponenten beschreiben
* Am ende zeige ich dann noch die Ergebnisse des Funktionstests

## Konzept - Anforderungen
* Als erstes habe ich mit Hanno und Kevin einige Anforderungen an den Generator erarbeitet
* Er soll die vier verschiedenen Funktionsverläufe ausgeben können, die ich hier geplottet habe: aufzählen ...
* An diesen Signalen kann man jetzt den high- und low wert und die freq konfigurieren
* zusätzlich ist es möglich, den dutycycle des square signals einzustellen und die Richtung der Rampensteigung
* Die Konfiguration erfolgt über eine UART Schnittstelle

## Konzept - Aufbau
* kommen wir jetzt zum Aufbau des Generators
* schwarz = Komponenten innerhalb des FPGA, die ich entwickelt habe
* grün = peripherie
* wenn man dem Signalfluss, ausgehend vom Uart-IF folgt, dann sieht man, dass die vom User kommenden Bytes zuerst in den Config Baustein gelangen.
* config baustein hält aktuelle Einstellungen für jeden der folgenden vier Funktionsbausteine
* Jeder dieser Bausteine verfügt über ein eigenes Ausgangssignal
* Dies wird vom Mux mithilfe des waveform Signals an die Komponente DAC weitergeleitet
* DAC setzt Protokoll des Pmod DA2 um
    * serialisierung der paralleln Daten
* Pmod DA2 gibt schließlich analogwert aus

* Im folgenden werden wir die Einzelkomponenten etwas näher betrachten
* Der Constant Funktionsbaustein leitet einfach das aktuell konfigurierte high Signal an seinen Ausgang weiter
* Square zählt Taktzyklen ab, vergleicht mit Schwellwert Thresh und gibt high aus wenn thresh > Zähler
* Und zu Zig-Zag kommen wir jetzt ...

## 

## 
* Frequenzbeschriftung testergebnisse
* sum squared error vergleich
