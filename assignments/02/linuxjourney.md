# 1. Aufgabe
Exercises<br>
Try some other Linux commands and see what they output:

$ date <br>
- Mi 30 Okt 2024 17:33:47 CET <br> <br>
$ whoami <br>
- cemilhantozak

## Quiz
What should be outputted to the display when you type echo Hello World? <br>
- Hello World <p>

# 2. Aufgabe
## Quiz
How do I find what directory you are currently in? <br>
pwd <br>
- /Users/cemilhantozak

# 3. Aufgabe
Exercises <br>
Run the cd command without any flags, where does it take you? <br>
- (base) cemilhantozak@Cems-Air

## Quiz
If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use? <br>
- cd ..

# 4. Aufgabe
Exercises<br>
Run ls with different flags and see the output you receive.
<br><br>
### ls -R: recursively list directory contents<br>
- opens all my files, to long of a code to put it in here <br>
### ls -r: reverse order while sorting<br>
- mysuperduperfile
index.html
Zahlenraten.ipynb
Untitled4.ipynb
Untitled3.ipynb
Untitled2.ipynb
Untitled1.ipynb
Untitled.ipynb
Rplot.pdf
Public
Pictures
Parallels
Music
Movies
Library
Foto.jpg
Downloads
Documents
Desktop
Bewerbungsfoto
Applications (Parallels)
Abgabe_Tozak.R <br>
### ls -t: sort by modification time, newest first
-Downloads
mysuperduperfile
Desktop
Bewerbungsfoto
Foto.jpg
Library
Documents
Zahlenraten.ipynb
Untitled1.ipynb
Untitled4.ipynb
Untitled3.ipynb
Untitled2.ipynb
Untitled.ipynb
Pictures
index.html
Applications (Parallels)
Abgabe_Tozak.R
Rplot.pdf
Music
Movies
Parallels
Public

# 5.Aufgabe
Exercises <br>
Create a new file<br>
-(base) cemilhantozak@Cems-MacBook-Air ~ % touch neuedatei
<p>
Note the timestamp 
 <p/> 
(base) cemilhantozak@Cems-MacBook-Air ~ % ls -l
- -rw-r--r--    1 cemilhantozak  staff       0  6 Nov 13:30 neuedatei <br>
Touch the file and check the timestamp once again <br>
(base) cemilhantozak@Cems-MacBook-Air ~ % touch neuedatei <br>
(base) cemilhantozak@Cems-MacBook-Air ~ % ls -l
- -rw-r--r--    1 cemilhantozak  staff       0  6 Nov 13:31 neuedatei
