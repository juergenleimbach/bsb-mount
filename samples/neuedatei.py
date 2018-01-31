from pathlib import Path
import base64

def config_new(sichern):
   file = '../config/config.dat'
   oeffne = open(file,"w")
   for zeile in range(len(sichern)):
      if zeile == 0:
         werte[zeile] = ("["+werte[zeile]+"]")
      elif zeile == 2:
         werte[zeile] = werte[zeile].encode('utf-8')
         werte[zeile] = base64.b64encode(werte[zeile])
         werte[zeile] = werte[zeile].decode('utf-8')
      oeffne.write(werte[zeile]+"\n")
   oeffne.close()
werte = ['config', 'j.leimbach', 'GEHEIM', '10.22.10.1']
config_new(werte)
