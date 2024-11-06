Hier ist die formatierte Markdown-Datei, die alle Aufgaben klar strukturiert und gut formatiert enthält. Kopiere den Inhalt in deine `.md` Datei:

```markdown
# 1. Aufgabe
### Exercises
Versuche einige Linux-Befehle und prüfe ihre Ausgabe:

```bash
$ date
```
- Mi 30 Okt 2024 17:33:47 CET

```bash
$ whoami
```
- cemilhantozak

### Quiz
**Frage**: Was sollte angezeigt werden, wenn man `echo Hello World` eingibt?  
**Antwort**: `Hello World`

---

# 2. Aufgabe
### Quiz
**Frage**: Wie finde ich heraus, in welchem Verzeichnis ich mich gerade befinde?  
**Antwort**: Mit dem Befehl `pwd`

```bash
$ pwd
```
- /Users/cemilhantozak

---

# 3. Aufgabe
### Exercises
Führe den `cd`-Befehl ohne Flags aus. Wohin führt er dich?

- (base) cemilhantozak@Cems-Air

### Quiz
**Frage**: Wenn du dich in `/home/pete/Pictures` befindest und zu `/home/pete` wechseln möchtest, was ist eine gute Abkürzung?  
**Antwort**: `cd ..`

---

# 4. Aufgabe
### Exercises
Führe den `ls`-Befehl mit verschiedenen Flags aus und prüfe die Ausgabe.

#### `ls -R`: rekursives Auflisten des Verzeichnisinhalts
- Öffnet alle meine Dateien. Zu lange, um den gesamten Code hier einzufügen.

#### `ls -r`: umgekehrte Reihenfolge beim Sortieren
- mysuperduperfile  
- index.html  
- Zahlenraten.ipynb  
- Untitled4.ipynb  
- Untitled3.ipynb  
- Untitled2.ipynb  
- Untitled1.ipynb  
- Untitled.ipynb  
- Rplot.pdf  
- Public  
- Pictures  
- Parallels  
- Music  
- Movies  
- Library  
- Foto.jpg  
- Downloads  
- Documents  
- Desktop  
- Bewerbungsfoto  
- Applications (Parallels)  
- Abgabe_Tozak.R

#### `ls -t`: nach Änderungszeit sortieren, neueste zuerst
- Downloads  
- mysuperduperfile  
- Desktop  
- Bewerbungsfoto  
- Foto.jpg  
- Library  
- Documents  
- Zahlenraten.ipynb  
- Untitled1.ipynb  
- Untitled4.ipynb  
- Untitled3.ipynb  
- Untitled2.ipynb  
- Untitled.ipynb  
- Pictures  
- index.html  
- Applications (Parallels)  
- Abgabe_Tozak.R  
- Rplot.pdf  
- Music  
- Movies  
- Parallels  
- Public

---

# 5. Aufgabe
### Exercises
Erstelle eine neue Datei:

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % touch neuedatei
```

**Merke dir den Zeitstempel**

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % ls -l
```
- `-rw-r--r--    1 cemilhantozak  staff       0  6 Nov 13:30 neuedatei`

**Aktualisiere den Zeitstempel der Datei und überprüfe ihn erneut:**

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % touch neuedatei
(base) cemilhantozak@Cems-MacBook-Air ~ % ls -l
```
- `-rw-r--r--    1 cemilhantozak  staff       0  6 Nov 13:31 neuedatei`
```

Dieser Markdown-Text ist so strukturiert, dass die Aufgaben und Fragen übersichtlich und gut lesbar sind. Befehle sind in Code-Blöcken und wichtige Fragen und Antworten sind klar hervorgehoben.
```

Quiz
How do you create a file called myfile?
- touch myfile

# 6.Aufgabe
###Exercises
Run the file command on a few different directories and files and note the output:
(base) cemilhantozak@Cems-MacBook-Air ~ % file Abgabe_Tozak.R
- Abgabe_Tozak.R: Unicode text, UTF-8 text

(base) cemilhantozak@Cems-MacBook-Air ~ % file zahlenraten.ipynb
- zahlenraten.ipynb: JSON data

(base) cemilhantozak@Cems-MacBook-Air ~ % file Rplot.pdf
- Rplot.pdf: PDF document, version 1.4, 1 pages

Quiz
What command can you use to find the file type of a file?
- file

# 7.Aufgabe

###Exercises
Run cat on different files and directories. Then try to cat multiple files.
(base) cemilhantozak@Cems-MacBook-Air ~ % cat zahlenraten.ipynb
- {
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

Quiz
What's a good way to see the contents of a file?
- cat

# 8.Aufgabe
Exercises
Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.
(base) cemilhantozak@Cems-MacBook-Air ~ % less /Users/cemilhantozak/Downloads/Übung_2.sql 
- /****************************************************************************
   2. Übung SQL DIS 13                     TH-Köln, Prof. Dr. Matthias Groß
 ****************************************************************************/

/* 
    Aufgaben mit ! erfordern das Nachschlagen in der Onlinehilfe
    Tragen Sie die Ergebnisse unter den Aufgaben ein und dokumentieren Sie
    ggfs. Besonderheiten
*/

-- Mehrere Tabellen abfragen
-- 1. Listen Sie alle Vorlesungen und die Namen der Professoren, die sie lesen, auf.
-- 2. Wie viele Professoren halten Vorlesungen?
-- 3. Welche Professoren halten keine Vorlesungen?
-- 4. Wie viele Vorlesungen liest der Professor mit der Personalnr. 2137
-- 5. Welche Vorlesungen hält Prof. Kant?
-- 6. Wie viele SWS hat Prof. Russel im Semester?
-- 7. Ermitteln Sie alle Professoren mit einer SWS>2 
-- 8. Welche Assistenten hat Prof. Sokrates?
-- 9. Wie viele Assistenten hat Prof. Kopernikus?
-- 10. Welche Vorlesungen (VorlNr) hat Zuhörer?
-- 11. Bei wem hatte Frau Carnap ihre Prüfung mit Note 1?
-- 12. Welche Note hat Frau Carnap in der Vorlesung Grundzüge?
-- 13. Ermitteln Sie die Voraussetzungen für alle Vorlesungen mit einem "th" im Titel
-- 14. Listen Sie die Voraussetzungen zu den Vorlesungen Erkenntnistheorie und Wissenschaftstheorie auf
-- Für später oder für die, die schon mal "group by" versuchen möchten!
-- 15. Wie viele Assistenten hat JEDER Prof?
-- 16. Ermitteln Sie die durchschnittliche Semesterzahl der Anwesenden je Vorlesung
-- 17. Ermitteln Sie die durchschnittliche Semesterzahl der Hörer je Professor
/Users/cemilhantozak/Downloads/Übung_2.sql (END)

Quiz
How do you quit out of a less command?
- q

# 9.Aufgabe
Exercises
Navigate through your previous command history with the Up and Down keys. Play around with ctrl-R reverse search.

(base) cemilhantozak@Cems-MacBook-Air ~ % less /Users/cemilhantozak/Downloads/Übung_2.sql    
bck-i-search: l_

Quiz
What is the command to clear the terminal?
- clear
- 

