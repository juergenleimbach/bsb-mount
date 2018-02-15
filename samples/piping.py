import subprocess
import platform


hostname = "10.22.10.1"
osstring = platform.platform()
if osstring[0] == "W":
    os_command = '-n'
    os_error = rb'nicht erreichbar'

if osstring[0] == "D":
    os_command = '-c'
    os_error = rb'Unreachable'

print ('Prüfen ob angegebener Rechner existiert.')
output = subprocess.Popen(["ping",os_command,'1',hostname], stdout = subprocess.PIPE).communicate()[0]

#print (output)

if (os_error in output):
    print ('Host nicht gefunden')
else:
    print ('Host gefunden')
