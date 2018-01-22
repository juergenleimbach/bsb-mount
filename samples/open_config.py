# Datei oeffnen und Werte zeilenweise in Array speichern
# Es muss bekannt sein, wieviele Werte zur Verfügung gestellt
# werden
gelesen = ['config']
fobj = open("config.dat")
for line in fobj:
    gelesen.append(line.rstrip())
fobj.close()
#range(2)
for i in range(2,4):
    print (i)
    gelesen[i] = gelesen[i][6:]
    #i = i+1
    print (i)
print (gelesen[2])
print (gelesen[3])
# print (gelesen[3][6:])
