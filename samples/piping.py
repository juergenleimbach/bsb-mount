import subprocess
import platform


hostname = "10.22.10.8"
osstring = platform.platform()
if osstring[0] == "W":
    output = subprocess.Popen(["ping.exe",'-n','1',hostname],
                              stdout = subprocess.PIPE).communicate()[0]

    print(output)

    if (rb'nicht erreichbar' in output):
        print("Offline")
    else:
        print ('Online')
