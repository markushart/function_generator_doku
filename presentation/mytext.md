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
* Und zu Zig-Zag und Ramp kommen wir jetzt ...

## Rampe 
* SCLKGEN generiert 68tel Systemtakt
* Counter zählt in richtung dir
* wird dann zurückgesetzt, wenn cycticks oder 0 erreicht wird, dadurch lässt sich die Zykluszeit darstellen
* rauf-/runterzählen = Rampe
* aber 24 bit breiter counter muss auf 12 bit breiten Ausgang für DAC gemapped werden
* daher Formel
* addieren und multiplizieren in einem Takt möglich, division nicht, daher Division
* gehen wir einmal den Ablauf durch ... (Folien durchgehen)

## Zick-Zack 
* analog zu Rampe, änderungen grün
* cycticks wird halbiert mit bitshift
* D wird getoggelt bei count = 0 oder count = cycticks / 2

## Config
* interpretieren von jeweils 4 byte als ein befehl
* state machine, 5 Zustände:
* IDLE: default zustand
* SHIFT: 
    * einlesen des nächsten bit bei UART_rdy
    * byte_count == 3 -> Interprete
    * byte_count != 3 -> IDLE
* INTERPRETE: 
    * wenn byte einen bekannten befehl enthält -> Calculate
* CALCULATE:
    * berechnen bestimmter konfigurationssignale aus Befehl (z.B. thresh)
    * immer -> Output
* OUTPUT:
    * weitergeben der konfigurationssignale an Ausgänge von Config
    * immer -> IDLE

## Test Versuchsaufbau

## Test Durchführung
* drei verschiedene tests:
    * alle UART Befehle -> erfolgreich
    * jeden Funktionsbaustein bei 100hz
    * Frequenzbereich mit Zick Zack in 10er Potenzen

## Test - Ergebnisse 100 Hz
    * Frequenz ist korrekt, verlauf auch
    * aber Uhigh und Ulow zu niedrig
        * möglicherweise weil Uref = Uv

## Test Frequenzbereich
    * f < fmin -> höhere Frequenz, denn mehr als 2²⁴ Werte sind nicht möglich
    * f > fmax -> zick-zack komponente kann das dir signal niemals toggeln, weil ct = 1 und ct / 2 = 0 
    * 100 kHz: Verlauf sehr ungenau, seltsamerweise keine Treppenstufen
    * 350 kHz: Verlauf ebenso ungenau, dafür aber Treppenstufen
        * geringere Frequenz
        * evtl. parasitäre Kapazität, müsste noch getestet werden
    
## Fazit
   * abschließend möchte ich meine ergebnisse noch zusammenfassen
   * ...
   *

## Referenzen
   * am ende habe ich hier noch ein Link zu einem Git-Repository
   * Python IF
   * Liste mit Hex Befehlen
   * Wenn Sie noch weitere Fragen haben, stellen sie die gerne jetzt oder schreiben sie mir. Ich bedanke mich für Ihre Aufmerksamkeit und wünsche Ihnen noch einen guten Tag.
