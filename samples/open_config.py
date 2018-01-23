# Datei oeffnen und Werte zeilenweise in Array speichern
# Es muss bekannt sein, wieviele Werte zur Verfügung gestellt
# werden
gelesen = []
# Zeilen, die mit einem dieser Zeichen beginnen, werden bei der Tupel-Erzeugung
# ignoriert
ignorelist = ['[','#']
# Datei öffnen, Zeiger auf Dateianfang
fobj = open('../config/config.dat')
# Zeilenweises Einlesen in Schleife und anhängen der Zeilen
# an Array gelesen
i=0
for line in fobj:
    gelesen.append(line.strip())
    #gelesen.append(line.rstrip())
    i=i+1
fobj.close()
j=0
print (gelesen[0][0])
for i in range(j,i):
    if gelesen[i][0] not in ignorelist:
        gelesen[i] = gelesen[i][6:]
    print (gelesen[i])
