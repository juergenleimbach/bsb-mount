# Datei oeffnen und Werte zeilenweise in Array speichern
# Es muss bekannt sein, wieviele Werte zur Verfügung gestellt
# werden
gelesen = []
# Datei öffnen, Zeiger auf Dateianfang
fobj = open('../config/config.dat')
# Zeilenweises Einlesen in Schleife und anhängen der Zeilen
# an Array gelesen
i=0
vergl = 'config'
for line in fobj:
    gelesen.append(line.rstrip())
    i=i+1
fobj.close()
j=0
print (gelesen[0])
#print (vergl)
for i in range(j,i):
    if gelesen[0] in "config123":
        gelesen[i] = gelesen[i][6:]
    print (gelesen[i])
