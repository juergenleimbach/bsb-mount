import win32api

def get_used_drive_letters():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    letters = [d[0] for d in drives]
    return letters

#a = get_used_drive_letters()
#print (a)

def get_unused_drive_letters():
    alphabet = map(chr, range(ord('A'), ord('Z')+1))
    used = get_used_drive_letters()
    unused = list(set(alphabet)-set(used))
    return unused

#b= get_unused_drive_letters()
#print (b)

def get_highest_unused_drive_letter():
    unused = get_unused_drive_letters()
    highest = list(reversed(sorted(unused)))[0]
    return highest

preferred = r'H'
reserved = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
unbenutzt = get_unused_drive_letters()
kleinster = list(sorted(unbenutzt))
print (reserved)
if preferred in unbenutzt:
    print (kleinster.index(preferred))
else:
    print (kleinster[kleinster.index('B')+1])
    print (kleinster)

c = get_highest_unused_drive_letter()

#print (c)
