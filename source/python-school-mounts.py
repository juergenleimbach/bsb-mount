def getmyadress():
# Ermitteln der aktuellen IP für vorhandene Internetverbindung
# u.a. zur Feststellung des Standorts (Schule, Zuhause)
    import socket
    return ([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
     
def aushaengen ():
# Falls vorhanden werden Netzlaufwerke getrennt - achtung ! Netzstruktur und
# gewollte LW müssen bekannt sein.
    import win32wnet
    import win32netcon
# Die Kombination try: ... except: pass stellt sicher, dass das Programm auch
# ausgeführt wird, wenn es im Normalfall anghalten würde, weil die Laufwerke
# H: (HOME) und L: (Lehrertausch) nicht eingehängt wurden.
    try:
        win32wnet.WNetCancelConnection2('H:',1,0)
        win32wnet.WNetCancelConnection2('L:',1,0)
    except:
        pass

gelesen = ['config']
fobj = open("config.dat")
for line in fobj:
    gelesen.append(line.rstrip())
fobj.close()
for i in range(2,4):
    gelesen[i] = gelesen[i][6:]
    i = i+1
    
    
import win32wnet
import win32netcon
import os
myaddr = getmyadress()
aushaengen ()
home = {}
if myaddr == '10.28.0.1':
    home["letter"] = r'h:'
    home["user"] = gelesen[2]
#    home["user"] = os.getenv('username')
    home["passw"] = gelesen[3]
    home["path"] = '\\\\10.22.10.1\\' + os.getenv('username') + '$'
    print (home["path"])
win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, home["letter"], home["path"], None, home["user"], home["passw"])

teachers = {}
if myaddr == '10.28.0.1':
    teachers["letter"] = r'l:'
    teachers["path"] = r'\\10.22.10.1\BSBEBRA_Tausch$'
    teachers["user"] = gelesen[2]
    teachers["passw"] = gelesen[3]
win32wnet.WNetAddConnection2(win32netcon.RESOURCETYPE_DISK, teachers["letter"], teachers["path"], None, teachers["user"], teachers["passw"])
