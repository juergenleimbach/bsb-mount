# Datei oeffnen und Werte zeilenweise in Array speichern
# Es muss bekannt sein, wieviele Werte zur Verfügung gestellt
# werden
gelesen = []
# Datei öffnen, Zeiger auf Dateianfang
fobj = open('../config/config.dat')
# Zeilenweises Einlesen in Schleife und anhängen der Zeilen
# an Array gelesen
i=0
vergl = ['[','#']
for line in fobj:
    gelesen.append(line.rstrip())
    i=i+1
fobj.close()
j=0
print (gelesen[0][0])
#print (vergl)
for i in range(j,i):
    if gelesen[i][0] not in vergl:
        gelesen[i] = gelesen[i][6:]
    print (gelesen[i])
