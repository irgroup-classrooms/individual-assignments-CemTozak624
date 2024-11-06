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
