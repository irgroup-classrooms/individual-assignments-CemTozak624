# Aufgabe 2: Document and describe the different data fields.
- In der Tabelle gibt es insgesamt 4 Spalten:
  - Die erste Spalte heißt "#" gibt lediglich die Nummerierung der Zeilen da, insgesamt gibt es 2389 davon.
  - Die zweite Spalte heißt "char" gibt die Rasse oder den Namen des Characters an, wovon sich manche Daten überschneiden
  - Die dritte Spalte heißt "dialog". Hier geht es um Zitate von den jeweiligen Characteren, wovon die allermeisten einzigartige Daten sind
  - die vierte und letzte Spalte heißt "movie". Hieraus kann man balesen, welcher Character in welchem Film vorgekommen ist.
 
# Aufgabe 3: Identify "dirty" data fields and clean them up. Use regex replace, spreadsheets, OpenRefine or whatever you like.
Die folgenden Sätze sind Beispiele dafür, wie "dirty data" bereinigt wurde. Es gab viele weitere Sätze, die ähnliche Muster und Probleme aufwiesen. Mit den gezeigten Methoden können diese ebenfalls korrigiert werden.

---

### 2. Problem

#### Falscher Satz: Gandalf?

```
value.replace("  ", "")
```
#### Korrigierter Satz: Gandalf?
---

### 3. Problem

#### Falscher Satz: And I've gone and had too much. , It must be getting late.

```
value.replace(". ,", ".")
```
#### Korrigierter Satz: And I've gone and had too much. It must be getting late.

---

### 4. Problem

#### Falscher Satz: What?Gandalf?See what?
```
value.replace("?", "? ")
```

#### Korrigierter Satz:What? Gandalf? See what?

---

### 5. Problem

#### Falscher Satz: , Show yourself.

```
value.replace(", ", "")
```

#### Korrigierter Satz: Show yourself.

---
```
:)
```

### 6. Problem

#### Falscher Satz: Rally to me!To meeee!

```
value.replace("!", "! ")
```

#### Korrigierter Satz: Rally to me! To meeee!

--- 

### 7. Problem

#### Falscher Satz: Murderer) 

```
value.replace(")", "")
```
#### Korrigierter Satz: Murderer

