# Initialisieren der grafischen Elemente
from tkinter import *

# Funktion zum Speichern der eingegebenen Werte in einer Datei
# (bisher: print als ersatz)
# Wird innerhalb der Funktion liesein() aufgerufen,
# liesein() wird hier nicht beendet
def config_speichern(sichern):
   for i in range(len(sichern)):
      print((sichern[i].get()))

# Funktion zum Einlesen der Werte in einem Fenster
# Grafische Oberfläche: Tkinter
def liesein():
# Fenster erzeugen
   master = Tk()
# ueber der Array beschriftung wird die erste Zeile definiert
   beschriftung = ['Vorname', 'Nachname', 'Passwort', 'Configuration']
# Initialisierung lokaler Array: eingabefelder
   eingabefeld = []
   for i in range(len(beschriftung)):
      Label(master, text=beschriftung[i]).grid(row=i)
      eingabefeld.append(Entry(master))
      eingabefeld[i].grid(row=i, column=3)
# Festlegung der notwendigen Buttons
# Erster Button: weiter führt das Programm aus ohne Werte zu speichern
   Button(master, text='weiter',
             command=master.quit).grid(row=i+1, column=0)
# Zweiter Button: speichern sichert eingegebene Werte in der Konfigurationsdatei
# Funktionsaufruf lesen
# Aufruf noch offen - füllt Tabelle mit einer vorgegebenen Konfiguration
   Button(master, text='lesen',
             command=(lambda ein=eingabefeld:
                      config_speichern(ein))).grid(row=i+1,column=1)
# Funktionsaufruf: config_speichern
# Aufruf über lambda, damit die Werte der Eingabefelder übergeben werden können
   Button(master, text='speichern',
             command=(lambda ein=eingabefeld:
                      config_speichern(ein))).grid(row=i+1,column=3)
   master.mainloop()
   return eingabefeld

weiter = liesein()

print("am ende")
#for i in range(len(weiter)):
#   print((weiter[i].get()))
