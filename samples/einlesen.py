def config_lesen():
    file = '../config/config.dat'
    oeffne = open(file)
    werte = []
    zeilenzaehler = 0
    for zeile in oeffne:
      werte.append(zeile.strip())
      print (werte[zeilenzaehler])
      zeilenzaehler = zeilenzaehler + 1
    oeffne.close()
    return (werte)
spalte = config_lesen()
