# Ermittelt freie Laufwerksbuchstaben ab Laufwerk H
# und gibt die Buchstaben zurück, die für
# HOME
# TAUSCH
# ALLE Klassen
# BIBLIOTHEK
# möglichst genutzt werden sollen.
# sind entsprechende Buchstaben belegt, wird jeweils auf den nächsten ausgewichen
def laufwerkszuteilung_windows():
    import win32api
    alphabet = map(chr, range(ord('A'), ord('Z')+1))
# Die folgenden Laufwerksbuchstaben werden nicht verwendet.
# zum einen, weil es sich um traditionelle Laufwerksbuchstaben handelt (A,B - Diskettenlaufwerke)
# bzw. (C,D,E - Plattenpartitionen oder Medienlaufwerke)
# oder Reserve für USB-Sticks etc.
    nicht_nutzen = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Im Schulnetz werden bestimmte Laufwerke bevorzugt:
# H fuer das Homelaufwerk des Benutzers
# M fuer das Verzeichnis aller Klassen
# T ist das Tauschverzeichnis 
    bevorzugt = ['H', 'M', 'P', 'T']
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    benutzt = [d[0] for d in drives]
    unbenutzt = list(sorted(set(alphabet) - set(benutzt) - set(nicht_nutzen)))
# Nur Debug: Ausgabe der unbenutzten Laufwerke
    print (len(unbenutzt))
#    print (len(bevorzugt))
    rueck = unbenutzt
    help = []
    for i in range(0,len(unbenutzt)):
        print (bevorzugt[0], 'Index', i)
        if unbenutzt[i] >= bevorzugt[0]:
            help.append(unbenutzt[i])
            rueck = list(sorted(set(rueck) - set(help)))
            print (rueck)
            print (help)
"""
        if bevorzugt[0] >= unbenutzt1[i]:
            rueck.append(unbenutzt[0])
            unbenutzt = list(sorted(set(unbenutzt) - set(rueck)))
        print (rueck)
        print (unbenutzt)
"""

"""
    if bevorzugt[0] in unbenutzt:
        rueck = ['H']
    else:
        rueck = [unbenutzt[0]]
    print (rueck, 'ist frei')
    block = ['H', 'I', 'J', 'K']
#    unbenutzt = list(sorted(set(unbenutzt) - set(block) - set(rueck)))
    unbenutzt = list(sorted(set(unbenutzt) - set(rueck)))
    print (unbenutzt)
    if bevorzugt[1] in unbenutzt:
        rueck.append('M')
    else:
        rueck.append(unbenutzt[0])
    print (rueck, 'ist frei')
    block = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
#    unbenutzt = list(sorted(set(unbenutzt) - set(block) - set(rueck)))
    unbenutzt = list(sorted(set(unbenutzt) - set(rueck)))
    if bevorzugt[2] in unbenutzt:
        rueck.append('P')
    else:
        rueck.append(unbenutzt[0])        
    print (rueck, 'ist frei')
    block = ['P', 'Q', 'R', 'S']
    unbenutzt = list(sorted(set(unbenutzt) - set(block) - set(rueck)))
    if bevorzugt[3] in unbenutzt:
        rueck.append('T')
    else:
        rueck.append(unbenutzt[0])        
    return rueck
"""    
frei = laufwerkszuteilung_windows()
print (frei, 'uebergebene Werte')                         
