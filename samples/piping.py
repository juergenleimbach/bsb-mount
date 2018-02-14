import platform,subprocess,re
def Ping(hostname,timeout):
    if platform.system() == "Windows":
        command="ping "+hostname+" -n 1 -w "+str(timeout*1000)
    else:
        command="ping -i "+str(timeout)+" -c 1 " + hostname
    proccess = subprocess.Popen(command, stdout=subprocess.PIPE)
    matches=re.match('.*time=([0-9]+)ms.*', proccess.stdout.read(),re.DOTALL)
    if matches:
        return matches.group(1)
    else: 
        return False

otto = Ping('10.22.10.1',10)
print(otto)
