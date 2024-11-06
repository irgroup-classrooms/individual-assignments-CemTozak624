Hier ist die vollständig formatierte Markdown-Datei zum Kopieren und Einfügen:

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

---

# 6. Aufgabe
### Exercises
Führe den `file`-Befehl auf einigen verschiedenen Verzeichnissen und Dateien aus und notiere die Ausgabe:

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % file Abgabe_Tozak.R
```
- Abgabe_Tozak.R: Unicode text, UTF-8 text

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % file zahlenraten.ipynb
```
- zahlenraten.ipynb: JSON data

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % file Rplot.pdf
```
- Rplot.pdf: PDF document, version 1.4, 1 pages

### Quiz
**Frage**: Welchen Befehl kann man verwenden, um den Dateityp einer Datei zu bestimmen?  
**Antwort**: `file`

---

# 7. Aufgabe
### Exercises
Führe den `cat`-Befehl für verschiedene Dateien und Verzeichnisse aus. Versuche anschließend, mehrere Dateien mit `cat` gleichzeitig anzuzeigen.

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % cat zahlenraten.ipynb
```
- {
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

### Quiz
**Frage**: Wie kann man den Inhalt einer Datei anzeigen?  
**Antwort**: `cat`

---

# 8. Aufgabe
### Exercises
Führe den `less`-Befehl auf einer Datei aus, navigiere im Dokument und suche nach einem spezifischen Wort. Gehe schnell zum Anfang oder Ende der Datei.

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % less /Users/cemilhantozak/Downloads/Übung_2.sql 
```
- /****************************************************************************
   2. Übung SQL DIS 13                     TH-Köln, Prof. Dr. Matthias Groß
 ****************************************************************************/

...

### Quiz
**Frage**: Wie beendet man den `less`-Befehl?  
**Antwort**: `q`

---

# 9. Aufgabe
### Exercises
Navigiere durch den Verlauf deiner vorherigen Befehle mit den Pfeiltasten nach oben und unten. Experimentiere mit der `ctrl-R`-Suche im Verlauf.

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % less /Users/cemilhantozak/Downloads/Übung_2.sql    
```
bck-i-search: l_

### Quiz
**Frage**: Wie löscht man das Terminal?  
**Antwort**: `clear`

---

# 10. Aufgabe
### Exercises
Kopiere einige Dateien, achte darauf, nichts Wichtiges zu überschreiben.

```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % cp /Users/cemilhantozak/Downloads/Übung_2.sql /Users/cemilhantozak/Downloads/Bewerbung
(base) cemilhantozak@Cems-MacBook-Air ~ % cp *.jpg /Users/cemilhantozak/Downloads/Pictures
```

### Quiz
**Frage**: Welches Flag wird benötigt, um ein Verzeichnis zu kopieren?  
**Antwort**: `-r`

---

# 11. Aufgabe
### Exercises
Benenne eine Datei um und verschiebe sie in ein anderes Verzeichnis.

**Umbenennen der Datei:**
```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % mv /Users/cemilhantozak/Downloads/Übung_1 Aufgabe1
```

**Verschieben der Datei:**
```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % mv Aufgabe1 /Users/cemilhantozak/Downloads/Bewerbung
```

### Quiz
**Frage**: Wie benennt man eine Datei von `cat` zu `dog` um?  
**Antwort**: `mv cat dog`

---

# 12. Aufgabe
### Exercises
Erstelle einige Verzeichnisse und verschiebe Dateien in diese Verzeichnisse.

**Neues Verzeichnis erstellen:**
```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % mkdir books paintings movies
```

**Datei verschieben:**
```bash
(base) cemilhantozak@Cems-MacBook-Air ~ % mv art-logo.png /Users/cemilhantozak/books
```

### Quiz
**Frage**: Welcher Befehl wird zum Erstellen eines Verzeichnisses verwendet?  
**Antwort**: `mkdir`

---
```
