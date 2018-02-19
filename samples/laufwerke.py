# Ermittelt freie Laufwerksbuchstaben ab Laufwerk H
# und gibt die Buchstaben zurück, die für
# HOME
# TAUSCH
# ALLE Klassen
# BIBLIOTHEK
# möglichst genutzt werden sollen.
# sind entsprechende Buchstaben belegt, wird jeweils auf den nächst 
def laufwerkszuteilung_windows():
    import win32api
    alphabet = map(chr, range(ord('A'), ord('Z')+1))
    nicht_nutzen = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    bevorzugt = ['H', 'K', 'T']
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    benutzt = [d[0] for d in drives]
    unbenutzt = list(sorted(set(alphabet) - set(benutzt) - set(nicht_nutzen)))
    if bevorzugt[0] in unbenutzt:
        rueck = ['H']
        print ('ist frei')
    else:
        rueck = [unbenutzt[0]]
    block = ['H', 'I', 'J']
    unbenutzt = list(sorted(set(unbenutzt) - set(block)))
    if bevorzugt[1] in unbenutzt:
        rueck.append('K')
    else:
        rueck.append(unbenutzt[0])
    block = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
    unbenutzt = list(sorted(set(unbenutzt) - set(block)))
    if bevorzugt[2] in unbenutzt:
        rueck.append('T')
    else:
        rueck.append(unbenutzt[0])
    print (unbenutzt)
    
    return rueck

frei = laufwerkszuteilung_windows()
print (frei)                         
