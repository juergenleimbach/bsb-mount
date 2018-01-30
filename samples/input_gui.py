# Initialisieren der grafischen Elemente
from tkinter import *
import base64
import time

# Funktion zum Speichern der eingegebenen Werte in einer Datei
# (bisher: print als ersatz)
# Wird innerhalb der Funktion liesein() aufgerufen,
# liesein() wird hier nicht beendet
def config_speichern(sichern):
   file = '../config/config.dat'
   oeffne = open(file,"w")
   werte = []
   for zeile in range(len(sichern)):
      werte.append(sichern[zeile].get())
#      print (werte[zeile])
      if zeile == 0:
         werte[zeile] = ("["+werte[zeile]+"]")
      elif zeile == 2:
         werte[zeile] = werte[zeile].encode('utf-8')
         werte[zeile] = base64.b64encode(werte[zeile])
         werte[zeile] = werte[zeile].decode('utf-8')
#         oeffne.write(werte[zeile] +'\n')
#         cr = base64.b64decode(cr)
#         print (cr)
#         cr = cr.decode('utf-8')
#         print (cr)
      oeffne.write(werte[zeile]+"\n")

   oeffne.close()
   
def config_lesen():
    file = '../config/config.dat'
    oeffne = open(file)
    werte = []
    zeilenzaehler = 0
    for zeile in oeffne:
      werte.append(zeile.strip())
      if zeilenzaehler == 2:
         werte[zeilenzaehler] = werte[zeilenzaehler].encode('utf-8')
         werte[zeilenzaehler] = base64.b64decode(werte[zeilenzaehler])
         werte[zeilenzaehler] = werte[zeilenzaehler].decode('utf-8')
      print (werte[zeilenzaehler])
      zeilenzaehler = zeilenzaehler + 1
    oeffne.close()
    return (werte)

# Funktion zum Einlesen der Werte in einem Fenster
# Grafische Oberfläche: Tkinter
def liesein():
# Fenster erzeugen
   master = Tk()
# ueber der Array beschriftung wird die erste Zeile definiert
   beschriftung = ['Konfiguration', 'Anmeldename', 'Passwort', 'Server/Freigabe']
   vorgabe = ['config', 'j.leimbach', 'GEHEIM', '10.22.10.1']
# Initialisierung lokaler Array: eingabefelder
   eingabefeld = []
   for i in range(len(beschriftung)):
      Label(master, text=beschriftung[i]).grid(row=i)
      eingabefeld.append(Entry(master))
      eingabefeld[i].grid(row=i, column=3)
      eingabefeld[i].insert(10,vorgabe[i])
# Festlegung der notwendigen Buttons
# Erster Button: weiter führt das Programm aus ohne Werte zu speichern
   Button(master, text='weiter',
             command=master.quit).grid(row=i+1, column=0)
# Zweiter Button: speichern sichert eingegebene Werte in der Konfigurationsdatei
# Funktionsaufruf lesen
# Aufruf noch offen - füllt Tabelle mit einer vorgegebenen Konfiguration
   Button(master, text='lesen', command=config_lesen).grid(row=i+1,column=1)
#             command=(lambda ein=eingabefeld:
#                      config_speichern(ein))).grid(row=i+1,column=1)
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
