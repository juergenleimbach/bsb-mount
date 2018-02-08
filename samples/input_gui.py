# Initialisieren der grafischen Elemente
from tkinter import *
from pathlib import Path
import base64
#import win32wnet
#import win32netcon
import os


# Globale Konstanten und Variablen
file = '../config/config.dat'
beschriftung = ['Konfiguration', 'Anmeldename', 'Passwort', 'Server/Freigabe']
vorgabe = ['config', 'Anmeldename', 'GEHEIM', '10.22.10.1']

# Speichern / neu-erstellen der Konfigurationsdatei
# wird nur gebraucht, wenn Datei nicht existiert
def config_new(sichern):
   oeffne = open(file,"w")
   for zeile in range(len(sichern)):
      if zeile == 0:
         sichern[zeile] = ("["+sichern[zeile]+"]")
      elif zeile == 2:
         sichern[zeile] = sichern[zeile].encode('utf-8')
         sichern[zeile] = base64.b64encode(sichern[zeile])
         sichern[zeile] = sichern[zeile].decode('utf-8')
      oeffne.write(sichern[zeile]+"\n")
   oeffne.close()

# Funktion zum Speichern der eingegebenen Werte in einer Datei
# Wird innerhalb der Funktion liesein() aufgerufen,
# liesein() wird hier nicht beendet
def config_speichern(sichern):
   oeffne = open(file,"w")
   werte = []
   for zeile in range(len(sichern)):
      werte.append(sichern[zeile].get())
      if zeile == 0:
         werte[zeile] = ("["+werte[zeile]+"]")
      elif zeile == 2:
         werte[zeile] = werte[zeile].encode('utf-8')
         werte[zeile] = base64.b64encode(werte[zeile])
         werte[zeile] = werte[zeile].decode('utf-8')
      oeffne.write(werte[zeile]+"\n")
   oeffne.close()
   
# Einlesen der Werte aus einer existierenden Datei
def config_lesen():
    oeffne = open(file,"r")
    werte = []
    zeilenzaehler = 0
    hilfsspeicher = ''
    for zeile in oeffne:
      werte.append(zeile.strip())
      if zeilenzaehler == 0:
         for zeichen in range(1, len(werte[zeilenzaehler])-1):
            hilfsspeicher = hilfsspeicher + werte[zeilenzaehler][zeichen]
         werte[0] = hilfsspeicher
      if zeilenzaehler == 2:
         werte[zeilenzaehler] = werte[zeilenzaehler].encode('utf-8')
         werte[zeilenzaehler] = base64.b64decode(werte[zeilenzaehler])
         werte[zeilenzaehler] = werte[zeilenzaehler].decode('utf-8')
      zeilenzaehler = zeilenzaehler + 1
    oeffne.close()
    return (werte)

# Funktion zum Einlesen der Werte in einem Fenster
# Grafische Oberfläche: Tkinter
def liesein():
# Fenster erzeugen
   master = Tk()
   master.title('mount drive')
   master.geometry('350x120')
# Rahmen Radiobutton
   frameRadiobutton = Frame(master=master)
   frameRadiobutton.place(x=260, y=3, width=110, height=80)
   auswahl = StringVar()
   radiobutton1 = Radiobutton(master=frameRadiobutton, anchor='w', text='Schüler', value = 'shome', variable = auswahl)
   radiobutton1.place(x=5, y=5, width=100, height=20)
   radiobutton2 = Radiobutton(master=frameRadiobutton, anchor='w', text='Lehrer', value = 'lhome', variable = auswahl)
   radiobutton2.place(x=5, y=25, width=100, height=20)
   radiobutton1.select()

# Malen des Fensters mit Beschriftung und Werten
   eingabefeld = []
   for i in range(len(beschriftung)):
      Label(master, text=beschriftung[i]).grid(row=i)
      eingabefeld.append(Entry(master))
      eingabefeld[i].grid(row=i, column=3)
      if i == 2:
         eingabefeld[i].config(show="*")
      eingabefeld[i].insert(25,vorgabe[i])
# Festlegung der notwendigen Buttons
# Erster Button: weiter führt das Programm aus ohne Werte zu speichern
   Button(master, text='weiter',
             command=master.quit).grid(row=i+1, column=0)
# Zweiter Button: speichern sichert eingegebene Werte in der Konfigurationsdatei
# Funktionsaufruf lesen
# Aufruf noch offen - füllt Tabelle mit einer vorgegebenen Konfiguration
   Button(master, text='lesen', command=config_lesen).grid(row=i+1,column=1)
# Funktionsaufruf: config_speichern
# Aufruf über lambda, damit die Werte der Eingabefelder übergeben werden können
   Button(master, text='speichern',
             command=(lambda ein=eingabefeld:
                      config_speichern(ein))).grid(row=i+1,column=3)
   
   master.mainloop()
   return eingabefeld

pruefe = Path(file)
# es wird geprüft, ob eine Konfigurationsdatei existiert
# wenn ja wird sie verwendet, wenn nein wird sie angelgt
if not pruefe.is_file():
   config_new(vorgabe)
# Initialisierung lokaler Array: eingabefelder
# Vorgabewerte (DEFAULTS) stehen in der Datei ../config/config.dat

with open(file) as oeffne:
    oeffne.seek(0)
    first_char = oeffne.read(1) #get the first character
    if not first_char:
        config_new(vorgabe) 

oeffne.close()

vorgabe = config_lesen()

weiter = liesein()

for i in range(len(weiter)):
   weiter[i] = weiter[i].get()
print("am ende")
for i in range(len(weiter)):
   print (i, weiter[i])
home = {}
home["letter"] = r'h:'
weiter[3] = '\\\\' + weiter[3] + '\\' + weiter[1] + '$'

print (home)

#win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK,
#                             home["letter"], weiter[3], None,
#                             weiter[1], weiter[2])
directory = "/Users/j.leimbach/home"
if not os.path.exists(directory): os.makedirs(directory)
#os.system("mount_smbfs //schule.bs-bebra.de;j.leimbach:jliJL123d@10.22.10.1/j.leimbach$ /Users/j.leimbach/home")
os.system("mount_smbfs //j.leimbach:jliJL123@10.22.10.1/j.leimbach$ /Users/j.leimbach/home")
